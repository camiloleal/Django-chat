from django.contrib import admin
from chat_app.models import *

admin.site.register(ChatUser)
admin.site.register(Message)