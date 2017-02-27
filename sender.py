from spam import create_message, send_message, get_users

# paste here an address of file with your email base
database_1 = 'PATH_OF_YOUR_EMAILS_ADDRESS_LIST_FILE'

# create a list of users from base
users = get_users(database_1)

# sending messages to every user
for user in users:
    msg = create_message(user)
    send_message(msg, True)