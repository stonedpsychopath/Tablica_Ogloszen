from django.shortcuts import render, get_object_or_404
from .models import Announcement, AbstractUser


def question_list(request):
   announcements = Announcement.objects.all()
   return render(request, 'tablica_ogloszen/question_list.html', {'announcements': announcements})

def question_detail(request, question_id):
   question = get_object_or_404(Announcement, pk=question_id)
   return render(request, 'tablica_ogloszen/question_detail.html', {'announcement': question})

def announcement_list(request):
   abstractUser = AbstractUser.objects.all()
   return render(request, 'tablica_ogloszen/announcement_list.html', {'abstractUser': abstractUser})

