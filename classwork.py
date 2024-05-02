import datetime
import json
import os

class ReservationSystem:
    def __init__(self):
        self.users = self.load_users()
        self.locations = {}
        self.reservations = []

    def load_users(self):
        users = {}
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
        return users

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def register(self):
        print("Registration")
        print("..........................")
        username = input("Enter username: ")
        if username in self.users:
            print("Username already exists. Please choose a different username.")
            return
        password = input("Enter password: ")
        self.users[username] = password
        self.save_users()
        print("Registration successful.")

    def login(self):
        print("\nLogin")
        print("..........................")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users and self.users[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_location(self):
        name = input("Enter location name: ")
        city = input("Enter city: ")
        country = input("Enter country: ")
        if name in self.locations:
            print("Location already exists.")
            return
        self.locations[name] = {"city": city, "country": country}
        print("Location added successfully.")

    def remove_location(self):
        name = input("Enter location name to remove: ")
        if name in self.locations:
            del self.locations[name]
            print("Location removed successfully.")
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
        phone_number = input("Enter your phone number (e.g., XXX-XXX-XXXX): ")
        if not self.validate_phone_number(phone_number):
            print("Invalid phone number format. Please enter in XXX-XXX-XXXX format.")
            return

        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\nSelect Room Type:")
        print("..........................")
        print("1. Room with 1 bed")
        print("2. Room with 2 beds")
        print("3. Room with double bed")
        print("4. Suite")
        print("..........................")

        room_types = {"1": "Room with 1 bed", "2": "Room with 2 beds", "3": "Room with double bed", "4": "Suite"}
        room_type_choice = input("Enter your choice: ")
        if room_type_choice not in room_types:
            print("Invalid room type choice.")
            return

        selected_room = room_types[room_type_choice]

        prices = {"Room with 1 bed": 50, "Room with 2 beds": 80, "Room with double bed": 120, "Suite": 160}
        price = prices[selected_room]

        while True:
            nights = input("Enter the number of nights you would be staying: ")
            if nights.isdigit() and int(nights) > 0:
                nights = int(nights)
                break
            print("Invalid input. Please enter a positive integer.")

        total_cost = price * nights

        print("...............................")
        print(f"\nYou have selected: {selected_room}")
        print(f"Price per night: ${price}")
        print(f"Total cost for {nights} nights: ${total_cost}")

        reservation_details = {"name": name, "phone_number": phone_number, "date_time": date_time,
                               "selected_room": selected_room, "nights": nights, "total_cost": total_cost}
        self.reservations.append(reservation_details)
        print("Reservation successfully made.")
        print("...............................")

    def validate_phone_number(self, phone_number):
        return len(phone_number) == 12 and phone_number[:3].isdigit() and phone_number[4:7].isdigit() and phone_number[8:].isdigit()

    def main_menu(self):
        while True:
            print("\nWelcome to Reservation System")
            print(".......................")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            print(".......................")

            choice = input("Choice: ")

            if choice == '1':
                self.register()
            elif choice == '2':
                if self.login():
                    self.logged_in_menu()
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def logged_in_menu(self):
        while True:
            print("\nMain Menu")
            print(".......................")
            print("1. Location")
            print("2. Reservation")
            print("3. View Reservations")
            print("4. Logout")
            print("5. Exit")
            print(".......................")

            choice = input("Choice: ")

            if choice == '1':
                self.location_menu()
            elif choice == '2':
                self.make_reservation()
            elif choice == '3':
                self.view_reservations()
            elif choice == '4':
                print("Logging out...")
                break
            elif choice == '5':
                print("Exiting program...")
                exit()
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

            choice = input("Choice: ")

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

    def view_reservations(self):
        if self.reservations:
            print("\nReservations:")
            for reservation in self.reservations:
                print(reservation)
        else:
            print("No reservations found.")

if __name__ == "__main__":
    system = ReservationSystem()
    system.main_menu()
