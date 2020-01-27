from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Authors, Books
from .serializers import *
# Create your views here.

class AuthorsList(ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsListSerializer


class BooksList(ListAPIView):
    queryset = Books.objects.filter(available=True)
    serializer_class = BooksListSerializer

class AuthorsDetail(RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsListSerializer
    lookup_field = 'id'
    lookup_url_kwarg= 'author_id'

class AuthorUpdate(RetrieveUpdateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg= 'author_id'
class AuthorDelete(DestroyAPIView):
    queryset = Authors.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg= 'author_id'


class AuthorCreate(CreateAPIView):
    serializer_class = AuthorsListSerializer

class BookCreate(CreateAPIView):
    serializer_class = BookCreateSerializer

class BookDelete(DestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg= 'book_id'

class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer