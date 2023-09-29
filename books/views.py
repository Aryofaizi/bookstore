from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


from .models import Book, Comment
from .forms import BookForm, CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"

    def get_queryset(self):
        return Book.objects.filter(status="pub")


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = "books/book_detail.html"
@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            return redirect("book_detail", pk)
    else:
        form = CommentForm()
    return render(request, template_name="books/book_detail.html", context={
        "book": book,
        "comments": comments,
        "form": form
    })


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    template_name = "books/book_create.html"
    fields = ["title", "description", "author", "status", "price", "cover"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_create.html"
    # fields = ["title", "description", "author", "status", "price"]

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class CommentDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = "books/book_delete.html"

    def get_success_url(self):
        return reverse_lazy("book_detail", kwargs={"pk": self.get_object().book.id})

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


