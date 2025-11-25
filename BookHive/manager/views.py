from django.shortcuts import render,redirect
from manager.models import Author
from django.utils.text import slugify

# Create your views here.
def managerDashboard(request):
    user="Sandhya"
    return render(request,"manager-dashboard.html",{"user":user})
    # return render(request,"manager-dashboard.html",{"user":"sree"})

def addAuthor(request):
    if request.method=="POST":
        name=request.POST['author_name']
        place=request.POST['place']
        dob=request.POST['dob']
        about=request.POST['about']
        # print(name,place,dob,about)
        profile_pic=request.FILES['picture']
        # writter=Author(name=name,place=place,dob=dob,about=about,image=profile_pic).save()
        link=slugify(name)
        writter=Author(name=name,place=place,dob=dob,about=about,image=profile_pic,slug=link)      
        writter.save()
        return redirect('list_authors')
    return render(request,"add-author.html")

def allAuthors(request):
    # malayalam_authors = [
    # {
    #     "name": "Thakazhi Sivasankara Pillai",
    #     "place": "Thakazhi, Alappuzha",
    #     "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Thakazhi_1.jpg"
    # },
    # {
    #     "name": "Vaikom Muhammad Basheer",
    #     "place": "Thalayolaparambu, Kottayam",
    #     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Vaikom_Muhammad_Basheer_2009_stamp_of_India.jpg/500px-Vaikom_Muhammad_Basheer_2009_stamp_of_India.jpg"
    # },
    # {
    #     "name": "M. T. Vasudevan Nair",
    #     "place": "Kudallur, Palakkad",
    #     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/MT_VASUDEVAN_NAIR.jpg/500px-MT_VASUDEVAN_NAIR.jpg"
    # },]
    malayalam_authors=Author.objects.all()
    print(malayalam_authors)
    context= {"authors":malayalam_authors,"user":"sree"}
    return render(request,"all-authors.html",context)
# return render(request,"all-authors.html",{"authors":malayalam_authors})

# def authorDetails(request,author_id):
#     writter=Author.objects.get(id=author_id)
#     # print(writter)
#     return render(request,"author-details.html",{"author":writter})
def authorDetails(request,link):
    writter=Author.objects.get(slug=link)
    # print(writter)
    return render(request,"author-details.html",{"author":writter})

def editAuthor(request,link):
    author=Author.objects.get(slug=link)
    if request.method=="POST":
        name=request.POST['author_name']
        place=request.POST['place']
        dob=request.POST['dob']
        about=request.POST['about']
        profile_pic=request.FILES.get('picture')
        author.name=name
        author.place=place
        author.dob=dob
        author.about=about
        if profile_pic:
            author.image=profile_pic
        author.save()
        return redirect('author-details',link)
    return render(request,"edit-author.html",{"writer":author})

def deleteAuthor(request,link):
    writer=Author.objects.get(slug=link)
    writer.delete()
    return redirect("list_authors")
