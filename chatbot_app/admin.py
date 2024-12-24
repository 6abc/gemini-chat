from django.contrib import admin
from .models import Message
# Register your models here.
admin.site.site_header = 'Chatbot Admin'
admin.site.site_title = 'Chatbot Admin Area'
admin.site.index_title = 'Welcome to the Chatbot Admin Area'
admin.site.register(Message)