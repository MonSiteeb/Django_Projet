from django.contrib import admin

# Register your models here.
from .models import Documents,Newsletter,MailMessage
admin.site.register(Documents)
admin.site.register(MailMessage)
admin.site.register(Newsletter)
