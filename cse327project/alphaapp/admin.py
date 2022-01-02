from django.contrib import admin

from alphaapp.models import Contact,Question, Answer

# Register your models here.
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(Answer)