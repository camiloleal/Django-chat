from django.contrib import admin
from chat_app.models import *

admin.site.register(ChatProfile)
admin.site.register(Room)
admin.site.register(Message)