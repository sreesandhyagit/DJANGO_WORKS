from django.shortcuts import render,redirect,get_object_or_404
from manager.models import Author,Book,BookLike
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy,reverse


# Create your views here.
@login_required(login_url="signin")
def managerDashboard(request):
    user="Sandhya"
    return render(request,"manager-dashboard.html",{"user":user})
    # return render(request,"manager-dashboard.html",{"user":"sree"})

@login_required(login_url="signin")
def addAuthor(request):
    if request.method=="POST":
        name=request.POST['author_name']
        place=request.POST['place']
        dob=request.POST['dob']
        about=request.POST['about']
        # print(name,place,dob,about)
        profile_pic=request.FILES.get('picture',None)
        # writter=Author(name=name,place=place,dob=dob,about=about,image=profile_pic).save()
        # link=slugify(name)
        writter=Author(name=name,place=place,dob=dob,about=about,image=profile_pic)      
        writter.save()
        messages.success(request,"New author added")
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
    books=writter.books.all()
    return render(request,"author-details.html",{"author":writter,"books":books})

@login_required(login_url="signin")
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
        messages.success(request,"Updated author details")
        return redirect('author-details',link)
    return render(request,"edit-author.html",{"writer":author})

@login_required(login_url="signin")
def deleteAuthor(request,link):
    writer=Author.objects.get(slug=link)
    writer.delete()
    messages.success(request,"Author Deleted")
    return redirect("list_authors")

@login_required(login_url="signin")
def addBooks(request):
    if request.method=="POST":
        my_form=BookForm(request.POST,request.FILES)
        if my_form.is_valid():
            my_form.save()
            messages.success(request,"New book added")
            return redirect("add_books")
        else:
            print(my_form.errors)
            return redirect("add_books")
    else:
        my_form=BookForm()
    return render(request,"add-books.html",{"form":my_form})

class AllBooksView(ListView):
    template_name="all-books.html"
    queryset=Book.objects.all()
    context_object_name="books"

class BookDetails(SuccessMessageMixin,DetailView):
    template_name='book-details.html'
    model=Book
    context_object_name="book"
    slug_field="slug"
    slug_url_kwarg="book_link"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        context["is_liked"]=self.object.likes.filter(user=self.request.user).exists()
        return context

class UpdateBook(SuccessMessageMixin, UpdateView):
    template_name="update-book.html"
    form_class=BookForm
    model=Book
    slug_field="slug"
    slug_url_kwarg="book_slug"
    success_url="/manager/all-books"
    success_message="Book Details Updated"

    def get_success_url(self):
        return reverse("book-details",kwargs={"book_link":self.object.slug})

class DeleteBook(DeleteView):
    model=Book
    slug_field="slug"
    # slug_url_kwarg=""
    success_url=reverse_lazy("list_books")

def bookLike(request,slug):
    book=get_object_or_404(Book,slug=slug)
    like,created = BookLike.objects.get_or_create(book=book,user=request.user)
    if not created:
        like.delete()
        messages.info(request,"You unliked this book")
    else:
        messages.success(request,"You liked this book")
    return redirect(book.get_absolute_url())

