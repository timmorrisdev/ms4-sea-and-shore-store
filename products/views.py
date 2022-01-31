from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.messages.views import SuccessMessageMixin
from .mixins import SuperUserRequiredMixin
from django.urls import reverse_lazy

from .models import Product, Category, ProductVariations
from .forms import ProductForm, VariationForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brand = request.GET['brand']
            products = products.filter(brand__icontains=brand)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(brand__icontains=query)
            products = products.filter(queries)

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    template = 'products/products.html'
    context = {
        'page_obj': page_obj,
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }



    return render(request, template, context)


# def product_detail(request, product_id):
#     """ A view to show individual product details """

#     product = get_object_or_404(Product, pk=product_id)

#     template = 'products/product_detail.html'
#     context = {
#         'product': product,
#     }

#     return render(request, template, context)


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


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


class AddProduct(SuperUserRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_message = 'Successfully added product!'
    # success_url = reverse_lazy('product_detail', args=(self.object.id))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to add product. Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('product_detail', args=(self.object.id,))


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:      
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse('products'))


@login_required
def add_product_variation(request, product_id):
    """ Add a variation to the product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = VariationForm(request.POST, request.FILES)
        if form.is_valid():
            variation = form.save(commit=False)
            variation.product = product
            variation.save()
            messages.success(request, 'Successfully added product variation!')
            return redirect(reverse('add_product_variation', args=[product_id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = VariationForm()


    template = 'products/add_product_variation.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def delete_product_variation(request, variation_id):
    """ Delete product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    variation = get_object_or_404(ProductVariations, pk=variation_id)
    product_id = variation.product.id
    variation.delete()
    messages.success(request, "Variation deleted!")
    return redirect(reverse('add_product_variation', args=[product_id]))
