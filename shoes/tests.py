from django.test import TestCase
from .forms import SubmitShoesForm

# Test taken from "Hello Django"
class TestSubmitShoesForm(TestCase):
    #test submit form for Shoes
    def test_Shoe_name_required(self):
        #Verify print name is required
        form = SubmitShoesForm({'shoe_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('shoe_name', form.errors.keys())
        self.assertEqual(
            form.errors['shoe_name'][0], 'This field is required.')