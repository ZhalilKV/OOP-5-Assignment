# OOP-5-Assignment
# Inheritance in Python

## Overview
This project demonstrates the concept of inheritance in Object-Oriented Programming (OOP) using Python. It includes a shopping cart system for electronic devices, allowing users to browse, add items to their cart, and proceed to checkout. The system showcases how inheritance can be used to create specialized classes from a base class.

## Classes and Inheritance
### Base Class: `Device`
- Attributes: `name`, `price`, `stock`, `warranty_period`
- Methods: `display_info()`, `apply_discount()`, `is_available()`, `reduce_stock()`

### Derived Classes
1. **Smartphone** (inherits from `Device`)
   - Additional Attributes: `screen_size`, `battery_life`
   - Methods: `make_call()`, `install_app()`

2. **Laptop** (inherits from `Device`)
   - Additional Attributes: `ram_size`, `processor_speed`
   - Methods: `run_program()`, `use_keyboard()`

3. **Tablet** (inherits from `Device`)
   - Additional Attributes: `screen_resolution`, `weight`
   - Methods: `browse_internet()`, `use_touchscreen()`

### Cart Class
- Attributes: `items`, `total_price`
- Methods: `add_device()`, `remove_device()`, `print_items()`, `checkout()`

SAMPLE INPUT AND OUTPUT
Menu:
1. Show Devices
2. Show Cart
3. Exit
Select an option: 1
1. Name: iPhone 13, Price: $999.99, Stock: 10, Warranty: 12 months, Screen Size: 6.1 inches, Battery Life: 20 hours
2. Name: Samsung Galaxy S21, Price: $799.99, Stock: 15, Warranty: 12 months, Screen Size: 6.2 inches, Battery Life: 22 hours
3. Name: MacBook Pro, Price: $1299.99, Stock: 5, Warranty: 24 months, RAM Size: 16 GB, Processor Speed: 2.6 GHz
4. Name: Dell XPS 13, Price: $999.99, Stock: 8, Warranty: 24 months, RAM Size: 8 GB, Processor Speed: 3.1 GHz
5. Name: iPad Pro, Price: $799.99, Stock: 12, Warranty: 12 months, Screen Resolution: 2732x2048, Weight: 682 grams
6. Name: Samsung Galaxy Tab S7, Price: $649.99, Stock: 10, Warranty: 12 months, Screen Resolution: 2560x1600, Weight: 498 grams
Select a device to add to cart (number): 1
Enter quantity: 1

Menu:
1. Show Devices
2. Show Cart
3. Exit
Select an option: 2
Current Cart:
Name: iPhone 13, Price: $999.99, Stock: 10, Warranty: 12 months, Screen Size: 6.1 inches, Battery Life: 20 hours , Amount:  1
Total Price: $999.99

Menu:
1. Show Devices
2. Show Cart
3. Exit
Select an option: 3
Exiting the program.

UML DIAGRAM
![Снимок экрана 2025-02-25 204918](https://github.com/user-attachments/assets/fb880ed4-3fa4-49bb-9934-499720b4bcd0)

