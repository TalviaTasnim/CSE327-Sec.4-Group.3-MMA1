from django.test import SimpleTestCase
from alphaapp.forms import UserCreationForm, CustomerSignupForm





class TESTFORMS(SimpleTestCase):
    def test_from_validation(self):
        form=CustomerSignupForm(data={
            'first_name':'mdfaisal',
            'first_name':'mdfaisal',
            'email':'mdfaisal@gmail.com'


        })
        self.assertTrue(form.is_valid())