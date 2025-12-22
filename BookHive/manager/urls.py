from django.urls import path
from manager import views


# urlpatterns=[
#     path("dashboard",views.managerDashboard),
#     path("add-author",views.addAuthor),
#     path("all-authors",views.allAuthors)
# ]
urlpatterns=[
    path("",views.managerDashboard,name="dashboard"),
    path("add-author",views.addAuthor,name="create_author"),
    path("all-authors",views.allAuthors,name="list_authors"),
    path("author-details/<slug:link>",views.authorDetails,name="author-details"),
    path("edit-author/<slug:link>",views.editAuthor,name="edit-author"),
    path("remove-author/<slug:link>",views.deleteAuthor,name="delete-author"),

    path("add-books",views.addBooks,name="add_books"),
    path("all-books",views.AllBooksView.as_view(),name="list_books"),
    path("book-details/<slug:book_link>",views.BookDetails.as_view(),name="book-details"),
    path("update-book/<slug:book_slug>",views.UpdateBook.as_view(),name="update-book"),
    path("delete-book/<slug:slug>",views.DeleteBook.as_view(),name="delete-book"),
    path("books/<slug:slug>/like/",views.bookLike,name="book_like")

]