from django import forms

from .models import ProductReview


RATING_CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))

class ProductReviewForm(forms.ModelForm):
    '''form to add product review '''
    class Meta:
        model = ProductReview
        fields = ('rating',
                  'title',
                  'review')
        
        # rating = forms.Select( widget=CustomClearableFileInput)
        widgets = {
            'rating': forms.Select(choices=RATING_CHOICES)
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
