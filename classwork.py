import datetime
import json
import re

class ReservationSystem:
    def __init__(self):
        self.locations = self.load_locations()
        self.reservations = []

    def load_locations(self):
        try:
            with open("locations.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_locations(self):
        with open("locations.json", "w") as file:
            json.dump(self.locations, file)

    def add_location(self):
        name = input("Enter location name: ")
        city = input("Enter city: ")
        country = input("Enter country: ")
        if name in self.locations:
            print("Location already exists.")
            return
        self.locations[name] = {"city": city, "country": country}
        print("Location added successfully.")
        self.save_locations()

    def remove_location(self):
        name = input("Enter location name to remove: ")
        if name in self.locations:
            del self.locations[name]
            print("Location removed successfully.")
            self.save_locations()
        else:
            print("Location not found.")

    def display_locations(self):
        if self.locations:
            print("\nLocations:")
            for name, info in self.locations.items():
                print(f"Name: {name}, City: {info['city']}, Country: {info['country']}")
        else:
            print("No locations available.")

    def make_reservation(self):
        name = input("Enter your name: ")
        phone_number = self.get_valid_input("Enter your phone number (e.g., XXX-XXX-XXXX): ", self.validate_phone_number)
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\nSelect Room Type:")
        print("..........................")
        print("1. Room with 1 bed")
        print("2. Room with 2 beds")
        print("3. Room with double bed")
        print("4. Suite")
        print("..........................")

        room_types = {"1": "Room with 1 bed", "2": "Room with 2 beds", "3": "Room with double bed", "4": "Suite"}
        room_type_choice = self.get_valid_input("Enter your choice: ", lambda x: x in room_types.keys())

        selected_room = room_types[room_type_choice]

        prices = {"Room with 1 bed": 50, "Room with 2 beds": 80, "Room with double bed": 120, "Suite": 160}
        price = int(prices[selected_room])

        nights = self.get_valid_input("Enter the number of nights you would be staying: ", int)

        total_cost = int(price * nights)

        print("...............................")
        print(f"\nYou have selected: {selected_room}")
        print(f"Price per night: ${price}")
        print(f"Total cost for {nights} nights: ${total_cost}")

        reservation_details = {"name": name, "phone_number": phone_number, "date_time": date_time,
                               "selected_room": selected_room, "nights": nights, "total_cost": total_cost}
        self.reservations.append(reservation_details)
        print("Reservation successfully made.")
        print("...............................")

    def save_data(self):
        with open("reservations.json", "w") as file:
            json.dump(self.reservations, file)
        print("Data saved to file.")

    def authenticate(self):
        print("\nLogin")
        print(".......................")
        username = input("Enter username: ")
        password = input("Enter password: ")
        return username == "admin" and password == "password"

    def get_valid_input(self, prompt, validator):
        while True:
            user_input = input(prompt)
            if validator(user_input):
                return user_input
            print("Invalid input. Please try again.")

    def validate_phone_number(self, phone_number):
        pattern = r'^\d{3}-\d{3}-\d{4}$'
        return bool(re.match(pattern, phone_number))

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print(".......................")
            print("1. Location")
            print("2. Reservation")
            print("3. Save Data")
            print("4. View Saved Data")
            print("5. Exit")
            print(".......................")

            choice = self.get_valid_input("Choice: ", lambda x: x in ['1', '2', '3', '4', '5'])

            if choice == '1':
                self.location_menu()
            elif choice == '2':
                self.make_reservation()
            elif choice == '3':
                self.save_data()
            elif choice == '4':
                self.view_saved_data()
            elif choice == '5':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def location_menu(self):
        location_count = len(self.locations)
        print(f"\nLocation Menu ({location_count} locations)")

        while True:
            print(".......................")
            print("1. Add new location")
            print("2. Remove a location")
            print("3. Display locations")
            print("4. Back")
            print(".......................")

            choice = self.get_valid_input("Choice: ", lambda x: x in ['1', '2', '3', '4'])

            if choice == '1':
                self.add_location()
            elif choice == '2':
                self.remove_location()
            elif choice == '3':
                self.display_locations()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def view_saved_data(self):
        try:
            with open("reservations.json", "r") as file:
                data = json.load(file)
                print("\nSaved Reservation Data:")
                for reservation in data:
                    print(reservation)
        except FileNotFoundError:
            print("No saved data found.")

    def run(self):
        if self.authenticate():
            print("Authentication successful!")
            self.main_menu()
        else:
            print("Invalid username or password. Exiting program...")

if __name__ == "__main__":
    system = ReservationSystem()
    system.run()
