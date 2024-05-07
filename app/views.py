from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created')


def insert_webpage(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    TO.save()
    return HttpResponse('topic is created')


def insert_access(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    d=input('enter date')
    a=input('enter autnor name')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()

    return HttpResponse('topic is created')

def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)

