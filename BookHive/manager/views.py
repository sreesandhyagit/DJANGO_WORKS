from django.shortcuts import render

# Create your views here.
def managerDashboard(request):
    return render(request,"manager-dashboard.html")

def addAuthor(request):
    return render(request,"add-author.html")

def allAuthors(request):
    return render(request,"all-authors.html")