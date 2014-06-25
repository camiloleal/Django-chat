class Student(object):
    def __init__(self):
        self.username=""
        self.password=""
        self.email=""

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def set_username(self,username):
        self.username = username

    def set_password(self,password):
        self.password = password

    def set_email(self,email):
        self.email = email
