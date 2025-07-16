# in memory data


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Rented"
        return f"{self.year} {self.brand} {self.model} - {status}"


class CarRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_available_cars(self):
        print("\n📋 Available Cars:")
        for idx, car in enumerate(self.cars):
            if car.available:
                print(f"{idx + 1}. {car}")

    def rent_car(self, car_number):
        if 0 <= car_number < len(self.cars):
            car = self.cars[car_number]
            if car.available:
                car.available = False
                print(f"\n✅ You have rented: {car}")
            else:
                print("❌ Sorry, that car is already rented.")
        else:
            print("❌ Invalid car number.")

    def return_car(self, car_number):
        if 0 <= car_number < len(self.cars):
            car = self.cars[car_number]
            if not car.available:
                car.available = True
                print(f"\n✅ You have returned: {car}")
            else:
                print("⚠️ That car wasn't rented.")
        else:
            print("❌ Invalid car number.")


# ==== MAIN PROGRAM ====
system = CarRentalSystem()

# Add some sample cars
system.add_car(Car("Toyota", "Corolla", 2020))
system.add_car(Car("Honda", "Civic", 2019))
system.add_car(Car("Ford", "Mustang", 2021))

while True:
    print("\n🚗 Car Rental System Menu:")
    print("1. Show available cars")
    print("2. Rent a car")
    print("3. Return a car")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.show_available_cars()

    elif choice == "2":
        system.show_available_cars()
        try:
            car_num = int(input("Enter the car number to rent: ")) - 1
            system.rent_car(car_num)
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == "3":
        try:
            car_num = int(input("Enter the car number to return: ")) - 1
            system.return_car(car_num)
        except ValueError:
            print("❌ Please enter a valid number.")

    elif choice == "4":
        print("👋 Thank you for using the Car Rental System!")
        break

    else:
        print("❌ Invalid choice. Try again.")
