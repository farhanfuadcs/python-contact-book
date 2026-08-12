import json

try:
    with open ("contacts.json","r") as file:
        contact=json.load(file)
except FileNotFoundError:
    contact={}
while True:
    user=input("1.Save Contact\n" \
        "2.Search Contact\n" \
        "3.Show Contact\n" \
        "4.Edit Contact\n" \
        "5.Delete Contact\n" \
        "What do you want to do(1-5): ")
    user=int(user)


    if user ==1:
        name=input("Enter the name: ").lower().strip()
        number=input("Enter the Phone Number: ")
        contact[name]=number
        with open("contacts.json", "w") as file:
            json.dump(contact, file)

    elif user ==2:
        searchname=input('Search your contact: ').lower().strip()
        if searchname in contact:
            print(f"The number of your searched contact is {contact[searchname]}")
        
        else: 
            print("Contact not found")
        with open("contacts.json", "w") as file:
            json.dump(contact, file)


    elif user ==3:
        print(contact)

    elif user ==4:
        edit=input("Which contact you want to edit: ").lower().strip()
        phone=input("Enter the number: ")
        contact[edit]=phone
        with open("contacts.json", "w") as file:
            json.dump(contact, file)


    elif user ==5:
        delete=input("Which contact you want to delete: ").lower().strip()
        if delete in contact:
            contact.pop(delete)
        else:
            print("No contact found by the name you searched")
        with open ("contacts.json","w") as file:
            json.dump(contact,file)
    else:
        print("Something went wrong type (1-5)")
