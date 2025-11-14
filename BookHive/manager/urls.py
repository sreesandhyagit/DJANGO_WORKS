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
    path("all-authors",views.allAuthors,name="list_authors")
]