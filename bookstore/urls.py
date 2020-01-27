"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/<int:author_id>',views.AuthorsDetail.as_view()),
    path('update/<int:author_id>',views.AuthorUpdate.as_view()),
    path('delete/<int:author_id>',views.AuthorDelete.as_view()),
    path('delete/<int:book_id>',views.BookDelete.as_view()),
    path('books/create',views.BookCreate.as_view()),
    path('authors/create',views.AuthorCreate.as_view()),
    path('authors/',views.AuthorsList.as_view()),
    path('books/',views.BooksList.as_view()),
    path('register/',views.RegisterView.as_view())
]
