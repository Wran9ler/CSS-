name = input(' Enter you name : \n')


def welcome():
    print('''    < Welcome, user {} >
        You can do some operations like:
            1. See all contacts in phonebook
            2. Create contact
            3. Search
            4. Remove contact
            5. Quit'''.format(name))

    user = int(input(" Enter  num of your operation "))
    return user


def phonebook():
    contact = {}

    while True:
        user = welcome()

        if user == 1:
            if bool(contact):
                for k, v in contact.items():
                    print(k, ':', v)
            else:
                print('Your contact book is empty, choose another function ')
        elif user == 2:
            contact_name = input('Please input your name, surname or username ')
            contact_phone = input('Please input your phone number ')

            if contact_phone not in contact.items():
                contact.update({contact_name: contact_phone})

                print('Contact successfully saved')
                print(' Your updated phone book is Shown below: ')
                for k, v in contact.items():
                    print(k, ':', v)
            else:
                print('That contact already exists in your phonebook')
        elif user == 3:
            contact_name = input(' Enter the name of the contact details you wish to view: ')
            if contact_name in contact:
                print('The contact is', contact_name, ':', contact[contact_name])
            else:
                print('That contact does not exist! Return to main menu to choose another function')
        elif user == 4:
            contact_name = input(' Enter the name of the contact you wish to delete: ')
            if contact_name in contact:
                print('The contact is', contact_name, ':', contact[contact_name])
                confirm = input(' Are you sure you wish to delete this contact? Yes/No: ')
                if confirm.capitalize() == 'Yes':
                    contact.pop(contact_name)
                    for k, v in contact.items():
                        print('Your updated phone book is Shown below: ')
                        print(k, ':', v)
                else:
                    print('Return to main menu')
            else:
                print('That contact does not exist! Return to main menu to choose another function')

        elif user == 5:
            print('<Thanks user {} for using phonebook>'.format(name))
            break

        else:
            print(' Incorrect entry!')


phonebook()
