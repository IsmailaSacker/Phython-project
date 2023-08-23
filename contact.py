
# declearing a dictionary that will hold the input contacts
hold_data = {}

# the while loop that will hold the applicayion in a running state
while True:

    # this will display the menu
    print("Contact Menu")
    print("1. Add contact")
    print("2. Display Contact")
    print("3. Delete Contact")
    print("4. Exit Contact")

    response = input("Please enter 1 or 2 or 3 or 4: ")

    if response == "1":
        contact_name = input("Please enter the contact name: ")
        contact_no = input("Please enter the contact number: ")

        # The contact name and the number is save in the tuple
        hold_data[contact_name] = contact_no

        print(
            f"The Contact Name is: {contact_name} with the number {contact_no} has been saved successfully")

    elif response == "2":
        print("Display Contact")

        if hold_data:
            for contact_name, contact_no in hold_data.items():
                # This display the contact name and the contact number in the contact book
                print(
                    f"Contact Name: {contact_name} Contact No.: {contact_no}")

        else:
            print("No contact is saved for now")
        # deleting the contact in the contact book
    elif response == "3":
        contact_name = input("Please enter the name you wants to delete: ")

        for contact_name in hold_data:
            del hold_data[contact_name]
            print(
                f"The Contact Name: {contact_name} is deleted successfully. ")

        else:
            print(
                f"The Contact Name: {contact_name} does not exist in the contact book. ")

    elif response == "4":
        print("The Contact Book will exit. ")
        break

    else:
        print("Please you have entered a wrong reply, check the input and check again. ")


marked = [contact_name for contact_name in hold_data if contact_name.startswith(
    '__to_delete__')]
for contact_name in marked:
    del hold_data[contact_name]
    print(f"Contact '{contact_name}' deleted.")
