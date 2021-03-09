'''

input = put in user + pass

check if account exists

if matches, log in
if not prompt ask to make acc
'''


class Users:
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name


def new_user():
    name = input('what is your name? ')
    username = input('Ok, please tell me your new username: ')
    password = input('Please set a password: ')
    account_created = name, username, password
    return account_created


valid_accounts = [

]


User_decision = input('Would you like you log in or create an account? ')


if User_decision == 'create account':
    new_user()
else:
    exit()

valid_accounts.append(account_created)

print(valid_accounts)
