"""
Midterm Practical Exam — Network Device Inventory Tool
Student: Lacanlale, Kyla G.
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():
    # print the menu, return the user's choice
    
        print("=== Network Device Inventory ===")
        print("1. Add a device")
        print("2. View all devices")
        print("3. Count active vs inactive devices")
        print("4. Find a device by name")
        print("5. Exit")
        print("6. Remove a device by name") #optional    

def add_device(device_list):
    # ask for name, IP, status — build the string, add to the list
    
    print("=== Network Device Inventory ===")

    device_list = []
    
    name = input("Device Name: ")
    ip_add = input("IP Address: ")
    status = input("Status: ")

    device_list.append(name, "-", ip_add, "-", status)
    devices.extend(device_list)

def view_devices(device_list):
    # loop through and print every device — handle empty list
   
    device_list = devices.copy()

    print("=== View All Devices ===")

    for device in device_list:
        print(device)

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_device(device_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()

        choice  = input("\nChoose an option: ")
        # # use if/elif to call the right function based on choice
        
        if choice == '1':
            add_device()
        elif choice == '2':
            view_devices()
        elif choice == '3':
            count_active_inactive()
        elif choice == '4':
            find_device()
        elif choice == '5':
            break
        elif choice == '6':
            pass
        else:
            print("Choice is invalid!")

        # set running = False when the user picks Exit

main()