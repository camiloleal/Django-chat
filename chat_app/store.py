from django.contrib import auth
from django.contrib.auth.models import User

class Store(object):

    def save_data(self,vector):
        for student in vector:
            user = User.objects.create_user(str (student.get_username()),str( student.get_email()), str (student.get_password()))
            user.save()


