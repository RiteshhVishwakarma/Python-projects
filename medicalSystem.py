import datetime

class MedicalSystem:
    def __init__(self):
        self.store = []

    def add_medi(self):
        print("Want to Exit? Type: done\n___________________________________________")
        while True:
            user = input("Add Medicine: ")
            if user.lower() == 'done':
                print("_______________\nExited\n________________")
                break
            print("Added Successfully!\n______________ ")
            current_time = datetime.datetime.now()
            self.store.append((user, current_time))

    def show(self):
        print("____________________________________")
        print("Available items are:\n")
        for i, (item, time_added) in enumerate(self.store, 1):
            print(f"{i}. {item} (added at {time_added})")
        print("____________________________________")

    def search(self):
        query = input("Enter the name of the item you want to search: ")
        found_items = [(item, time_added) for item, time_added in self.store if query.lower() in item.lower()]
        if found_items:
            print("\nSearch results:")
            for i, (item, time_added) in enumerate(found_items, 1):
                print(f"{i}. {item} (added at {time_added})")
        else:
            print("No items found matching the search.")

    def remove(self):
        item_to_remove = input("Enter the name of the item you want to remove: ")
        if any(item_to_remove == item[0] for item in self.store):
            self.store[:] = [item for item in self.store if item[0] != item_to_remove]
            print("\n______________________________________\nItem removed successfully...\n_________________________________________")
        else:
            print("Item not found in the list.")

    def update(self):
        item_to_update = input("Enter the name of the item you want to update: ")
        for i, (item, time_added) in enumerate(self.store):
            if item == item_to_update:
                new_item = input("Enter the new name for the item: ")
                self.store[i] = (new_item, time_added)
                print("\n______________________________________\nItem updated successfully...\n_________________________________________")
                return
        print("Item not found in the list.")

    def start(self):
        while True:
            print("\n1.Add Medi\n2.Show Medi List\n3.Search Medi\n4.Remove Medi\n5.Update Medi\n6.Exit")
            try:
                user = int(input("Choose: "))
            except ValueError:
                print("Enter a number value please!")

            if user == 1:
                self.add_medi()
            elif user == 2:
                self.show()
            elif user == 3:
                self.search()
            elif user == 4:
                self.remove()
            elif user == 5:
                self.update()
            elif user == 6:
                print("___________________________________\nBye!, Have a nice day...\n________________________________________")
                break
            else:
                print("Please choose a correct option.")

# Start the program
medical_system = MedicalSystem()
medical_system.start()
