class Users:
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    def log_in(self, username, password):
        print('please enter your usename and password')
        entered_username = input('Username: ')
        entered_password = input('Password: ')
        if self.username == entered_username and self.password == entered_password:
            print('You have logged in')
        else:
            print('You have entered an incorrect username or password, please try again')
