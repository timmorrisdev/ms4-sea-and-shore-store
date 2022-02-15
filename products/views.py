from django.shortcuts import reverse
from django.contrib import messages
from django.db.models import Q

from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .mixins import SuperUserRequiredMixin

from .models import Product, Category, ProductVariations
from .forms import ProductForm, VariationForm


# Class Based Views
class ProductList(ListView):
    ''' Class to list products based on search parameters'''

    model = Product
    context_object_name = 'products'
    template_name = 'products/products.html'
    paginate_by = 4

    def get_ordering(self):

        # return ordering to the class using criteria from the products page
        sort_by = 'name'
        if 'sort' in self.request.GET:
            sort_by = self.request.GET['sort']
        if 'direction' in self.request.GET:
            direction = self.request.GET['direction']
            if direction == 'desc':
                sort_by = f'-{sort_by}'

        ordering = sort_by

        return ordering

    def get_queryset(self):
        queryset = super().get_queryset()

        # return queryset for product navigation by category
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            queryset = Product.objects.filter(category__name=category)

        # return queryset for product navigation by brand
        if 'brand' in self.request.GET:
            brand = self.request.GET['brand']
            queryset = Product.objects.filter(brand__icontains=brand)

        # return queryset for product search
        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request,
                               "You didn't enter any search criteria!")
            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(brand__icontains=query)
            queryset = Product.objects.filter(
                        queries).order_by(self.get_ordering())

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # return current sorting argument to context
        context['current_sorting'] = self.get_ordering()

        # return context data if a search is made
        if 'q' in self.request.GET:

            categories = context['products'].values_list('category')
            context['current_categories'] = Category.objects.filter(
                                             id__in=categories
                                            )
            context['search_term'] = self.request.GET['q']

        # return category to context for use in pagination
        if 'category' in self.request.GET:
            context['current_category'] = self.request.GET['category']

        return context


class ProductDetail(DetailView):
    '''Class to display the individual product details'''

    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class AddProduct(SuperUserRequiredMixin, CreateView):
    ''' Class-based view to add product

        Inherits SuperUserRequired mixin to
        prevent unauthorised access'''

    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add product. \
                                      Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Successfully added product!')
        if self.object.has_variations:
            return reverse('add_product_variation', args=(self.object.id,))
        else:
            return reverse('product_detail', args=(self.object.id,))


class EditProduct(SuperUserRequiredMixin, UpdateView):
    ''' Class-based view to edit product

        Inherits SuperUserRequired mixin to
        prevent unauthorised access'''

    model = Product
    form_class = ProductForm
    template_name = 'products/edit_product.html'

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        messages.info(self.request, f'You are editing {product.name}')
        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add product. \
                                      Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Successfully updated product!')
        return reverse('product_detail', args=(self.object.id,))


class DeleteProduct(SuperUserRequiredMixin, DeleteView):
    ''' Class-based view to delete product.

        Inherits SuperUserRequired mixin to
        prevent unauthorised access'''

    model = Product
    context_object_name = 'product'
    template_name = 'products/delete_product.html'

    def get_success_url(self):
        messages.success(self.request, 'Successfully deleted product!')
        return reverse('products')


class AddProductVariation(SuperUserRequiredMixin, CreateView):
    ''' Class-based view to add product variation

        Inherits SuperUserRequired mixin to
        prevent unauthorised access'''

    model = ProductVariations
    form_class = VariationForm
    template_name = 'products/add_product_variation.html'

    def form_valid(self, form):
        form.instance.product = Product.objects.get(
                                 pk=self.kwargs['product_id']
                                )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add product. \
                                      Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['product_id'])
        return context

    def get_success_url(self):
        messages.success(self.request, 'Successfully added product variation!')
        return reverse_lazy('add_product_variation',
                            args=(self.kwargs['product_id'],))


class EditProductVariation(SuperUserRequiredMixin, UpdateView):
    ''' Class-based view to edit product variation

        Inherits SuperUserRequired mixin to
        prevent unauthorised access'''

    model = ProductVariations
    form_class = VariationForm
    template_name = 'products/edit_product_variation.html'

    def get(self, request, *args, **kwargs):
        variation = self.get_object()
        messages.info(self.request, f'You are editing variation \
                                    {variation.name} on \
                                    {variation.product.name}')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.object.product.id)
        return context

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update product variation. \
                                      Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request,
                         'Successfully updated product variation!')
        return reverse_lazy('add_product_variation',
                            args=(self.get_product().pk,))


class DeleteProductVariation(SuperUserRequiredMixin, DeleteView):
    ''' Class-based view to delete product variation

        Inherits SuperUserRequired mixin to
        prevent unauthorised access'''

    model = ProductVariations
    context_object_name = 'variation'
    template_name = 'products/delete_product_variation.html'

    def get_product(self):
        ''' Class function to return current product
            object to be returned in the context '''
        product = Product.objects.get(pk=self.object.product.id)
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.object.product.id)
        return context

    def get_success_url(self):
        messages.success(self.request,
                         'Successfully deleted product variation!')
        return reverse_lazy('add_product_variation',
                            args=(self.get_product().pk,))
