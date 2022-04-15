from django.urls import path
from .views import BookListView, BookDetailView,\
    BookCreateView, BookUpdateView, BookDeleteView,\
    MyPostView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('<slug:slug>/', BookDetailView.as_view(), name='detail'),
    path('<slug:slug>/update', BookUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete', BookDeleteView.as_view(), name='delete'),
    path('dashboard/myposts/', MyPostView.as_view(), name='my_posts'),
]
