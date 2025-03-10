from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from .models import *
from .forms import *
from django.db.models import F
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
from django.views.decorators.csrf import csrf_exempt

class Main(View):
    @csrf_exempt
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            userProfile = UserData.objects.filter(user=current_user) 
            levels = Level.objects.all()
            achievementList = AchievementProgress.objects.none()
            achievementProgress = AchievementProgress.objects.filter(user=userProfile[0])
            for el in achievementProgress:
                if (el.progress > 0) & (el.progress < el.achievement.limit):
                    tmp = AchievementProgress.objects.filter(user = el.user, achievement = el.achievement)
                    achievementList |= tmp
            print(achievementList)
            if userProfile[0].experience in range(0, 499):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=0)[0])
            elif userProfile[0].experience in range(500, 999):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=1)[0])
            elif userProfile[0].experience in range(1000, 1499):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=2)[0])
            elif userProfile[0].experience in range(1500, 2500):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=3)[0])

            percentLVL = int(userProfile[0].experience) / int(userProfile[0].level.maxExperience) * 100

            data = {
                'percentLVL': percentLVL,
                'userProfile': userProfile,
                'levels': levels,
                'achievementList': achievementList,
            }
            return render(request, "main/main.html", data)
        else:
            return render(request, "main/main.html")
    @csrf_exempt
    def post(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            userProfile = UserData.objects.filter(user=current_user) 
            levels = Level.objects.all()
            achievementList = AchievementProgress.objects.none()
            achievementProgress = AchievementProgress.objects.filter(user=userProfile[0])
            for el in achievementProgress:
                if (el.progress > 0) & (el.progress < el.achievement.limit):
                    tmp = AchievementProgress.objects.filter(user = el.user, achievement = el.achievement)
                    achievementList |= tmp
            print(achievementList)
            if userProfile[0].experience in range(0, 499):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=0)[0])
            elif userProfile[0].experience in range(500, 999):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=1)[0])
            elif userProfile[0].experience in range(1000, 1499):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=2)[0])
            elif userProfile[0].experience in range(1500, 2500):
                userProfile.update(level=Level.objects.filter(digitalEquivalent=3)[0])

            percentLVL = int(userProfile[0].experience) / int(userProfile[0].level.maxExperience) * 100

            data = {
                'percentLVL': percentLVL,
                'userProfile': userProfile,
                'levels': levels,
                'achievementList': achievementList,
            }
            return render(request, "main/main.html", data)
        else:
            return render(request, "main/main.html")
    
class TestAPIForm(View):
    def get(self, request):
        current_user = request.user
        userProfile = UserData.objects.filter(user=current_user) 
        allAchievementProgress = AchievementProgress.objects.filter(user=userProfile[0])
        if request.method =='POST':
            form = inputDataForm(request.POST)
            if form.is_valid():
                form.save()
                tmp = AchievementProgress.objects.none()
                target = Event.objects.filter(name=form.cleaned_data['event'])[0].category
                for el in allAchievementProgress:
                    if el.achievement.category == target:
                        if el.progress < el.achievement.limit:
                            tmp |= AchievementProgress.objects.filter(achievement = el.achievement, user = userProfile[0])
                            tmp.update(progress=el.progress + 1)
                            if el.progress + 1 == el.achievement.limit:
                                tmp.update(DoneOrNot=True)
                                if userProfile[0].experience < 2500:
                                    userProfile.update(experience=int(userProfile[0].experience)+tmp[0].achievement.addExperience)
                                userProfile.update(score=int(userProfile[0].score + tmp[0].achievement.addScore))
                if userProfile[0].experience < 2500:
                    userProfile.update(experience=int(userProfile[0].experience)+5)
                userProfile.update(score=int(userProfile[0].score)+form.cleaned_data['cheque']*userProfile[0].level.value/100)
                return redirect('main')
        
        form = inputDataForm()
        data = {
            'form': form,
        }
        return render(request, "testAPI/form.html", data)
    def post(self, request):
        current_user = request.user
        userProfile = UserData.objects.filter(user=current_user) 
        allAchievementProgress = AchievementProgress.objects.filter(user=userProfile[0])
        if request.method =='POST':
            form = inputDataForm(request.POST)
            if form.is_valid():
                form.save()
                tmp = AchievementProgress.objects.none()
                target = Event.objects.filter(name=form.cleaned_data['event'])[0].category
                for el in allAchievementProgress:
                    if el.achievement.category == target:
                        if el.progress < el.achievement.limit:
                            tmp |= AchievementProgress.objects.filter(achievement = el.achievement, user = userProfile[0])
                            tmp.update(progress=el.progress + 1)
                            if el.progress + 1 == el.achievement.limit:
                                tmp.update(DoneOrNot=True)
                                if userProfile[0].experience < 2500:
                                    userProfile.update(experience=int(userProfile[0].experience)+tmp[0].achievement.addExperience)
                                userProfile.update(score=int(userProfile[0].score + tmp[0].achievement.addScore))
                if userProfile[0].experience < 2500:
                    userProfile.update(experience=int(userProfile[0].experience)+5)
                userProfile.update(score=int(userProfile[0].score)+form.cleaned_data['cheque']*userProfile[0].level.value/100)
                return redirect('main')
        
        form = inputDataForm()
        data = {
            'form': form,
        }
        return render(request, "testAPI/form.html", data)
    
class Achievements(View):
    def get(self, request):
        category = Сategory.objects.all()
        current_user = UserData.objects.filter(user=request.user)
        userData = current_user
        achievementProgress = AchievementProgress.objects.filter(user=current_user[0])
        data = {
            'category': category,
            'userData': userData,
            'achievementProgress': achievementProgress,
        }
        return render(request, "main/achievements.html", data)
    def post(self, request):
        return render(request, "main/achievements.html")
    
class AddAchievements(View):
    def get(self, request):
        if request.method =='POST':
            form = achievementForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('addAchievements')
        
        form = achievementForm()
        list = Achievement.objects.all()
        data = {
            'form': form,
            'list': list,
        }
        return render(request, "admin/addAchievement.html", data)
    def post(self, request):
        current_user = request.user
        userProfile = UserData.objects.filter(user=current_user) 
        if request.method =='POST':
            form = achievementForm(request.POST)
            if form.is_valid():
                form.save()
                for el in UserData.objects.all():
                    a = AchievementProgress.objects.create(user=el, achievement=Achievement.objects.filter(name=form.cleaned_data['name'])[0], progress=0, DoneOrNot=False)
                    a.save()
                return redirect('addAchievements')
        
        form = achievementForm()
        data = {
            'form': form,
        }
        return render(request, "admin/addAchievement.html", data)
    
class MyActivities(View):
    def get(self, request):
        current_user = request.user
        userProfile = UserData.objects.filter(user=current_user) 
        listInputData = InputData.objects.filter(user=userProfile[0])
        data = {
            'userProfile': userProfile,
            'listInputData': listInputData,
        }
        return render(request, "main/myActivities.html", data)
    def post(self, request):
        current_user = request.user
        userProfile = UserData.objects.filter(user=current_user) 
        listInputData = InputData.objects.filter(user=userProfile[0])
        data = {
            'userProfile': userProfile,
            'listInputData': listInputData,
        }
        return render(request, "main/myActivities.html", data)