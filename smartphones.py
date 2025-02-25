# devices.py

from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f"{super().__str__()}, Screen Size: {self.screen_size} inches, Battery Life: {self.battery_life} hours"

    def make_call(self):
        return "Making a call..."

    def install_app(self):
        return "Installing an app..."

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"{super().__str__()}, RAM Size: {self.ram_size} GB, Processor Speed: {self.processor_speed} GHz"

    def run_program(self):
        return "Running a program..."

    def use_keyboard(self):
        return "Typing on the keyboard..."

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()}, Screen Resolution: {self.screen_resolution}, Weight: {self.weight} grams"

    def browse_internet(self):
        return "Browsing the internet..."

    def use_touchscreen(self):
        return "Using the touchscreen for navigation..."