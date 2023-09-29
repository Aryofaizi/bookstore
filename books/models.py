from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    STATUS_CHOICES = (
        ("pub", "published"),
        ("drf", "draft"),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    cover = models.ImageField(upload_to="covers/", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])

    def get_update_url(self):
        return reverse("book_update", args=[self.id])

    @property
    def truncate_description(self):
        return self.description[:40] + "..." if len(self.description) > 40 else self.description


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return self.text
