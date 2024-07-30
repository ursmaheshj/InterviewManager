from django.contrib import admin
from interview.models import Interview

# Register your models here.
# @admin.register(Interview)
# class InterviewAdmin(admin.ModelAdmin):
#     fields = ['company','hr','phone','time','comment']
admin.site.register(Interview)