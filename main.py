
from smartphones import Smartphone, Laptop, Tablet
from cart import Cart

def create_devices():
    smartphones = []
    smartphones.append(Smartphone("iPhone 13", 999.99, 10, 12, 6.1, 20))
    smartphones.append(Smartphone("Samsung Galaxy S21", 799.99, 15, 12, 6.2, 22))
    smartphones.append(Laptop("MacBook Pro", 1299.99, 5, 24, 16, 2.6))
    smartphones.append(Laptop("Dell XPS 13", 999.99, 8, 24, 8, 3.1))
    smartphones.append(Tablet("iPad Pro", 799.99, 12, 12, "2732x2048", 682))
    smartphones.append(Tablet("Samsung Galaxy Tab S7", 649.99, 10, 12, "2560x1600", 498))
    
    return smartphones

def show_devices(devices):
    for index, device in enumerate(devices):
        print(f"{index + 1}. {device}")

def main():
    devices = create_devices()
    cart = Cart()

    while True:
        print("\nMenu:")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            show_devices(devices)
            device_choice = int(input("Select a device to add to cart (number): ")) - 1
            quantity = int(input("Enter quantity: "))
            if 0 <= device_choice < len(devices):
                cart.add_device(devices[device_choice], quantity)
            else:
                print("Invalid device selection.")

        elif choice == '2':
            print("Current Cart:")
            cart.print_items()
            print(f"Total Price: ${cart.get_total_price():.2f}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()