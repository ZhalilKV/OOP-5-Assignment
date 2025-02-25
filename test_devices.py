import unittest
from smartphones import Smartphone, Laptop, Tablet
from cart import Cart

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Smartphone("TestPhone", 500, 10, 12, 6.5, 24)

    def test_display_info(self):
        self.assertEqual(self.device.display_info(), "Name: TestPhone, Price: $500.00, Stock: 10, Warranty: 12 months")

    def test_apply_discount(self):
        self.device.apply_discount(10)
        self.assertEqual(self.device.price, 450.0)

    def test_is_available(self):
        self.assertTrue(self.device.is_available(5))
        self.assertFalse(self.device.is_available(15))

    def test_reduce_stock(self):
        self.device.reduce_stock(5)
        self.assertEqual(self.device.stock, 5)

        with self.assertRaises(ValueError):
            self.device.reduce_stock(10)

class TestSmartphone(TestDevice):
    def setUp(self):
        self.device = Smartphone("Smartphone", 1000, 5, 24, 6.1, 20)

    def test_make_call(self):
        self.assertEqual(self.device.make_call(), "Making a call...")

    def test_install_app(self):
        self.assertEqual(self.device.install_app(), "Installing an app...")

class TestLaptop(TestDevice):
    def setUp(self):
        self.device = Laptop("TestLaptop", 1200, 3, 24, 16, 3.1)

    def test_run_program(self):
        self.assertEqual(self.device.run_program(), "Running a program...")

    def test_use_keyboard(self):
        self.assertEqual(self.device.use_keyboard(), "Typing on the keyboard...")

class TestTablet(TestDevice):
    def setUp(self):
        self.device = Tablet("TestTablet", 600, 8, 12, "2048x1536", 500)

    def test_browse_internet(self):
        self.assertEqual(self.device.browse_internet(), "Browsing the internet...")

    def test_use_touchscreen(self):
        self.assertEqual(self.device.use_touchscreen(), "Using the touchscreen for navigation...")

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.device1 = Smartphone("Smartphone1", 300, 10, 12, 6.5, 24)
        self.device2 = Smartphone("Smartphone2", 400, 5, 12, 6.5, 24)

    def test_add_device(self):
        self.cart.add_device(self.device1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.total_price, 600.0)

    def test_add_device_not_available(self):
        self.cart.add_device(self.device2, 10)  # Not enough stock
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.total_price, 0.0)

    def test_remove_device(self):
        self.cart.add_device(self.device1, 2)
        self.cart.remove_device(self.device1, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.total_price, 300.0)

    def test_checkout(self):
        self.cart.add_device(self.device1, 2)
        self.cart.checkout()
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.total_price, 0.0)

if __name__ == '__main__':
    unittest.main()