from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.http import HttpResponseRedirect
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.db.models.functions import Lower
# from django.core.paginator import Paginator

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .mixins import SuperUserRequiredMixin

from django.urls import reverse_lazy

from .models import Product, Category, ProductVariations
from .forms import ProductForm, VariationForm


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products.html'
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()

        if 'category' in self.request.GET:
            category = self.request.GET['category']
            queryset = Product.objects.filter(category__name=category)

        if 'brand' in self.request.GET:
            brand = self.request.GET['brand']
            queryset = Product.objects.filter(brand__icontains=brand)
        
        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request,
                               "You didn't enter any search criteria!")
            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(brand__icontains=query)
            queryset = Product.objects.filter(queries)
        
        return queryset

    def get_ordering(self):

        sort_by = None
        if 'sort' in self.request.GET:
            sort_by = self.request.GET['sort']
        if 'direction' in self.request.GET:
            direction = self.request.GET['direction']
            if direction == 'desc':
                sort_by = f'-{sort_by}'

        ordering = sort_by

        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_sorting'] = self.get_ordering()
        
        if 'q' in self.request.GET:
            categories = context['products'].values_list('category')
            context['current_categories'] = Category.objects.filter(id__in=categories)
            context['search_term'] = self.request.GET['q']

        return context


# Class Based Views

class ProductDetail(DetailView):
    '''Class to display the individual product details'''

    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class AddProduct(SuperUserRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add product. Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Successfully added product!')
        return reverse('product_detail', args=(self.object.id,))


class EditProduct(SuperUserRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit_product.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.info(self.request, f'You are editing {self.object.name}')
        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add product. Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Successfully updated product!')
        return reverse('product_detail', args=(self.object.id,))


class DeleteProduct(SuperUserRequiredMixin, DeleteView):

    model = Product
    context_object_name = 'product'
    template_name = 'products/delete_product.html'

    def get_success_url(self):
        messages.success(self.request, 'Successfully deleted product!')
        return reverse('products')


class AddProductVariation(SuperUserRequiredMixin, CreateView):
    model = ProductVariations
    form_class = VariationForm
    template_name = 'products/add_product_variation.html'

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs['product_id'])
        return super(AddProductVariation, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add product. Please ensure the form is valid.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['product_id'])
        return context

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Successfully added product variation!')
        return reverse_lazy('add_product_variation', args=(self.kwargs['product_id']))


class EditProductVariation(SuperUserRequiredMixin, UpdateView):
    model = ProductVariations
    form_class = VariationForm
    template_name = 'products/edit_product_variation.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.info(self.request, f'You are editing {self.object.name}')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.object.product.id)
        return context

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update product variation. Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Successfully updated product variation!')
        return reverse_lazy('add_product_variation', args=(self.kwargs['product_id']))


class DeleteProductVariation(SuperUserRequiredMixin, DeleteView):

    model = ProductVariations
    context_object_name = 'variation'
    template_name = 'products/delete_product_variation.html'

    def get_product(self):
        product = Product.objects.get(pk=self.object.product.id)
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.object.product.id)
        return context

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Successfully deleted product variation!')
        return reverse_lazy('add_product_variation', args=(self.get_product().pk,))


# def all_products(request):
#     """ A view to show all products, including sorting and search queries """

#     products = Product.objects.all()
#     query = None
#     categories = None
#     sort = None
#     direction = None

#     if request.GET:
#         if 'sort' in request.GET:
#             sortkey = request.GET['sort']
#             sort = sortkey
#             if sortkey == 'name':
#                 sortkey = 'lower_name'
#                 products = products.annotate(lower_name=Lower('name'))
#             if sortkey == 'category':
#                 sortkey = 'category__name'
#             if 'direction' in request.GET:
#                 direction = request.GET['direction']
#                 if direction == 'desc':
#                     sortkey = f'-{sortkey}'
#             products = products.order_by(sortkey)

#         if 'category' in request.GET:
#             categories = request.GET['category'].split(',')
#             products = products.filter(category__name__in=categories)
#             categories = Category.objects.filter(name__in=categories)

#         if 'brand' in request.GET:
#             brand = request.GET['brand']
#             products = products.filter(brand__icontains=brand)

#         if 'q' in request.GET:
#             query = request.GET['q']
#             if not query:
#                 messages.error(request,
#                                "You didn't enter any search criteria!")
#                 return redirect(reverse('products'))

#             queries = Q(name__icontains=query) | Q(
#                 description__icontains=query) | Q(brand__icontains=query)
#             products = products.filter(queries)

#     paginator = Paginator(products, 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     current_sorting = f'{sort}_{direction}'

#     template = 'products/products.html'
#     context = {
#         'page_obj': page_obj,
#         'products': products,
#         'search_term': query,
#         'current_categories': categories,
#         'current_sorting': current_sorting,
#     }

#     return render(request, template, context)


# def product_detail(request, product_id):
#     """ A view to show individual product details """

#     product = get_object_or_404(Product, pk=product_id)

#     template = 'products/product_detail.html'
#     context = {
#         'product': product,
#     }

#     return render(request, template, context)


# @login_required
# def add_product(request):
#     """ Add a product to the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, 'Successfully added product!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to add product. Please ensure the form is valid.')
#     else:
#         form = ProductForm()

#     template = 'products/add_product.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)


# @login_required
# def edit_product(request, product_id):
#     """ Edit a product in the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Successfully updated product!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to update product. Please ensure the form is valid.')
#     else:      
#         form = ProductForm(instance=product)
#         messages.info(request, f'You are editing {product.name}')

#     template = 'products/edit_product.html'
#     context = {
#         'form': form,
#         'product': product,
#     }

#     return render(request, template, context)


# @login_required
# def delete_product(request, product_id):
#     """ Delete product from the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)
#     product.delete()
#     messages.success(request, "Product deleted!")
#     return redirect(reverse('products'))


# @login_required
# def add_product_variation(request, product_id):
#     """ Add a variation to the product """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)

#     if request.method == 'POST':
#         form = VariationForm(request.POST, request.FILES)
#         if form.is_valid():
#             variation = form.save(commit=False)
#             variation.product = product
#             variation.save()
#             messages.success(request, 'Successfully added product variation!')
#             return redirect(reverse('add_product_variation', args=[product_id]))
#         else:
#             messages.error(request, 'Failed to add product. Please ensure the form is valid.')
#     else:
#         form = VariationForm()

#     template = 'products/add_product_variation.html'
#     context = {
#         'form': form,
#         'product': product
#     }

#     return render(request, template, context)


# @login_required
# def delete_product_variation(request, variation_id):
#     """ Delete product variation """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))

#     variation = get_object_or_404(ProductVariations, pk=variation_id)
#     product_id = variation.product.id
#     variation.delete()
#     messages.success(request, "Variation deleted!")
#     return redirect(reverse('add_product_variation', args=[product_id]))