from django.shortcuts import render


def index(request):

    return render(request,"index.html")

def price(request):

    return render(request,"price.html")

def service(request):

    return render(request,"service.html")

def appointment(request):

    return render(request,"appointment.html")

def opening(request):

    return render(request,"opening.html")


def team(request):

    return render(request,"team.html")

def about(request):

    return render(request,"about.html")

def contact(request):

    return render(request,"contact.html")