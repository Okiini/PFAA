from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class Level(models.Model):
    name = models.CharField("Название", max_length=100, default='')
    maxExperience = models.IntegerField("Максимальный опыт")
    digitalEquivalent = models.IntegerField("Цифровой эквивалент уровня", blank=True, null=True)
    value = models.IntegerField("Значение(%)", default=0)
    img = models.ImageField("Иконка", upload_to='lvl', blank=True, null=True)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'
    
class Сategory(models.Model):
    name = models.CharField("Название", max_length=100, default='')
    icon = models.ImageField("Иконка", upload_to='lvl', blank=True, null=True)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'
    
class Event(models.Model):
    name = models.CharField("Название", max_length=100, default='')
    adress = models.CharField("Адрес", max_length=200, default='')
    category = models.ForeignKey("Сategory", on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'
    
class Achievement(models.Model):
    name = models.CharField("Название", max_length=100, default='')
    icon = models.ImageField("Иконка", upload_to='covers', blank=True)
    category = models.ForeignKey("Сategory", on_delete=models.CASCADE, null=True)
    addExperience = models.IntegerField("Выдаваемый опыт", blank=True, null=True)
    addScore = models.IntegerField("Выдаваемыe баллы", blank=True, null=True)
    limit = models.IntegerField("Цель", default=1)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, null=True)
    requiredQuantity = models.IntegerField("Необходимое количество людей", default=1)
    text = models.TextField("Текст условия", max_length=300, blank=True)


    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField("Имя", max_length=100, default='')
    theard_name = models.CharField("Фамилия", max_length=100, default='', null=True)
    email = models.EmailField(null=True, blank=True)
    level = models.ForeignKey("Level", on_delete=models.CASCADE, null=True)
    experience = models.IntegerField("Количество опыта")
    score = models.IntegerField("Количество баллов", blank=True, default=0)


    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'
    
class InputData(models.Model):
    date = models.DateTimeField("Время оплаты", default=timezone.now)
    numberOfPeople = models.IntegerField("Количество людей")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, null=True)
    cheque = models.FloatField("Чек(сколько оплачено)")
    user = models.ForeignKey("UserData", on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.date}'

class AchievementProgress(models.Model):
    user = models.ForeignKey("UserData", on_delete=models.CASCADE, null=True)
    achievement = models.ForeignKey("Achievement", on_delete=models.CASCADE, null=True)
    progress = models.IntegerField("Прогресс", default=0)
    DoneOrNot = models.BooleanField('Выполнено', default=False)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.user} {self.achievement}'