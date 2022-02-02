USERS_EMAIL = []
USERS_STORAGE = {}


def create_user(email, name, password, phone, USERS_EMAIL, USERS_STORAGE):
    user_info = [email, name, password, phone]
    USERS_EMAIL.append(email)
    USERS_STORAGE[email] = {'name': name,
                            'password': password,
                            'phone': phone}
    print('Create user info  = ', user_info)

    return None


def user_info(USERS_EMAIL, USERS_STORAGE):
    if email in USERS_EMAIL:
        message = f"User_email: {user_e}\nUser_info: {USERS_STORAGE[user_e]}"
        return message
    else:
        message = f"No user with email: {email}"
        return message


def all_users_info(USERS_STORAGE):
    for k, v in USERS_STORAGE.items():
        user_email = k
        user_info_1 = v
        print(f"User_email: {user_email}\nUser_info:  {user_info_1}")


def update_user(USERS_STORAGE):
    USERS_STORAGE[user_update].update({key_update: value_update})
    print('User_update = ', USERS_STORAGE)


def delete_user(USERS_STORAGE):
    """delete a user"""
    del USERS_STORAGE[user_delete]
    print('User_delete = ', USERS_STORAGE)


# def help_CRUD()
#     help_crud =
while True:
    action = input('Enter CRUD action: ').lower()
    if action == 'create':
        print('Action = ', action)
        email = input('Email: ').lower()
        if email not in USERS_EMAIL:
            name = input('Name: ').lower()
            password = input('Password: ')
            phone = input('Phone: ')

            create_user(email,
                        name,
                        password,
                        phone,
                        USERS_EMAIL,
                        USERS_STORAGE)

            print('User_emails = ', USERS_EMAIL)
            print('User_storage = ', USERS_STORAGE)

        else:
            print(f"Sorry, the email {email} is closed 😕")

    elif action == 'read_all':
        print('Action = ', action)
        all_users_info(USERS_STORAGE)

    elif action == 'read_user':
        user_e = input('Enter user email: ').lower()
        if user_e in USERS_EMAIL:
            print('Action = ', action)
            print(user_info(USERS_EMAIL, USERS_STORAGE))
        else:
            print(f'Sorry, user {user_e} does not exist 😕')

    elif action == 'update':
        user_update = input('Enter user email: ').lower()
        if user_update in USERS_EMAIL:
            key_update = input("Enter new user's key (name, password, phone): ").lower()
            value_update = input("Enter new user's value: ").lower()

            print('Action = ', action)
            update_user(USERS_STORAGE)
        else:
            print(f'Sorry, user {user_update} does not exist 😕')

    elif action == 'delete':
        user_delete = input('Enter user email you want to delete: ').lower()
        if user_delete in USERS_EMAIL:
            print('Action = ', action)
            delete_user(USERS_STORAGE)
        else:
            print(f'Sorry, user {user_delete} does not exist 😕')
