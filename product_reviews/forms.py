from django import forms

from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    '''form to add product review '''
    class Meta:
        model = ProductReview
        fields = 'rating', 'title', 'review'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['category'].choices = name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
