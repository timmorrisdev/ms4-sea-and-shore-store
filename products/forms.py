from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductVariations


class ProductForm(forms.ModelForm):
    '''class to configure the Product Form'''

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class VariationForm(forms.ModelForm):
    '''class to configure the Product Variation Form'''

    class Meta:
        model = ProductVariations
        fields = ('category', 'name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
