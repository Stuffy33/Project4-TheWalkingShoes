from django.test import TestCase

# Test taken from "Hello Django"
class TestViews(TestCase):
    def test_shoes_page(self):
        #Verify shoes page loads
        response = self.client.get('/shoes/shoess, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoess.html')
