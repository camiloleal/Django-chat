from django.contrib import admin
from chat_app.models import *

admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(Message)