from django import forms
from .models import ShoePair


class SubmitShoesForm(forms.ModelForm):
    #Shoe submission form
    class Meta:
        #generate fields for submission
        model = ShoePair
        fields = (
            'shoe_name',
            #'slug',
            'description',
            'category',
            'shoe_image',
            'shoe_size',
            'amount_of_pairs',
            'remaining_pairs',
            'price',
        )
        labels = {
            'shoe_name': 'Shoe name',
            #'slug': 'Repeat name. Do not include spaces.',
            'description': 'Description',
            'category': 'Category',
            'shoe_image': 'Select image',
            'shoe_size': 'Shoe size in UK sizes',
            'amount_of_pairs': "Number of pairs at launch",
            'remaining_pairs': "How many pairs remaining",
            'price': 'Price in Euros',
        }
