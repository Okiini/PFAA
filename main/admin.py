from django.contrib import admin
from .models import *

class LevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'maxExperience', 'value']
    list_editable = ['maxExperience', 'value']
    list_display_links = ['name']
    class Meta:
        model = Level

admin.site.register(Level, LevelAdmin) 

class СategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    class Meta:
        model = Сategory

admin.site.register(Сategory, СategoryAdmin) 

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress', 'category']
    list_editable = ['adress']
    list_display_links = ['name']
    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)

class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'category', 'addExperience', 'addScore']
    list_editable = ['addExperience', 'addScore']
    list_display_links = ['name']
    class Meta:
        model = Achievement

admin.site.register(Achievement, AchievementAdmin)

class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'experience', 'score']
    list_editable = ['experience', 'score']
    list_display_links = ['name']
    class Meta:
        model = UserData

admin.site.register(UserData, UserDataAdmin)

class InputDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'numberOfPeople', 'event', 'cheque', 'user']
    list_editable = ['numberOfPeople', 'cheque']
    list_display_links = ['date']
    class Meta:
        model = InputData

admin.site.register(InputData, InputDataAdmin) 

class AchievementProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'progress', 'DoneOrNot']
    list_editable = ['progress', 'DoneOrNot']
    class Meta:
        model = AchievementProgress

admin.site.register(AchievementProgress, AchievementProgressAdmin) 