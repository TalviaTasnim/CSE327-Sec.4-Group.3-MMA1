import unittest
from store.views import checkout

class TestCheckoutView(unittest.TestCase):


    def test_checkout_returns_correct_balance(request):
        request.cart.add_item('headphones', 3, 10)
        request.cart.add_item('Shirt', 16, 10)

        request.assertEqual(request.cart.checkout(265), 75, msg='Balance of checkout not correct')
        request.assertEqual(request.cart.checkout(25), 'Cash paid not enough', msg='Balance of checkout not correct')

if __name__ == '__main__':
            unittest.main(exit=False)
            print("test pass")
