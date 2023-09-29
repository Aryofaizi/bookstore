from django.urls import path
from .views import (
    BookListView,
    # BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    book_detail_view,
    CommentDeleteView
)

urlpatterns = [
    path("list/", BookListView.as_view(), name="book_list"),
    # path("list/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("list/<int:pk>/", book_detail_view, name="book_detail"),
    path("create/", BookCreateView.as_view(), name="book_create"),
    path("update/<int:pk>/", BookUpdateView.as_view(), name="book_update"),
    path("delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
    path("delete/comment/<int:pk>/", CommentDeleteView.as_view(), name="comment_delete")
]
