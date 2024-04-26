def process_temperatures(temp_list):
    # Convert temperatures from Celsius to Fahrenheit using list comprehension
    fahrenheit = [((9 / 5) * temp + 32) for temp in temp_list]
    print(f"Celsius to Fahrenheit: {fahrenheit}")

    # Filter out temperatures above 50 degrees Fahrenheit
    filtered_temps = [temp for temp in fahrenheit if temp < 50]
    print(f"Filtered temperatures (<50F): {filtered_temps}")


def inventory_processing():
    # Dictionary of fruit inventory
    inventory = {"apples": 10, "oranges": 15, "bananas": 5, "grapes": 0}

    # Print all items with stock
    print("Items in stock:")
    for fruit, quantity in inventory.items():
        if quantity > 0:
            print(f"{fruit}: {quantity}")

    # Dictionary comprehension to find items needing restocking
    restock = {k: v for k, v in inventory.items() if v == 0}
    print(f"Items to restock: {restock}")

    # Safely retrieve items with get
    lemons = inventory.get("lemons", "No lemons in stock")
    print(lemons)


def user_permissions():
    # Set operations for user permissions
    admin_permissions = {"read", "write", "delete"}
    user_permissions = {"read", "write"}

    # Check if a user has all necessary admin permissions
    if user_permissions.issubset(admin_permissions):
        print("User has some admin permissions")
    else:
        print("User lacks necessary admin permissions")

    # Determine missing permissions for full admin rights
    missing_permissions = admin_permissions - user_permissions
    print(f"Missing permissions for full admin: {missing_permissions}")

    # All possible permissions in the system
    all_permissions = admin_permissions | user_permissions
    print(f"All system permissions: {all_permissions}")


def system_configuration():
    # Tuple-based system configuration
    settings = [("resolution", "1920x1080", "display"), ("volume", 75, "audio"), ("brightness", 50, "display")]

    # Display settings using tuple unpacking
    print("Current system settings:")
    for name, value, setting_type in settings:
        print(f"{setting_type.capitalize()} - {name}: {value}")


def main():
    print("Processing Temperatures:")
    process_temperatures([10, 20, 0, -10])

    print("\nInventory Processing:")
    inventory_processing()

    print("\nUser Permissions:")
    user_permissions()

    print("\nSystem Configuration:")
    system_configuration()


if __name__ == "__main__":
    main()
