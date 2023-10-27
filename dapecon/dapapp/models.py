from django.db import models
from django.core.validators import MinLengthValidator


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title1 = models.CharField(max_length=150)
    excerpt1 = models.CharField(max_length=200)
    image_name1 = models.CharField(max_length=100)
    date1 = models.DateTimeField(auto_now_add=True)
    slug1 = models.SlugField(unique=True, db_index=True)
    content1 = models.TextField(validators=[MinLengthValidator(10)])
    author1 = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="blogs"
    )

    def __str__(self):
        return self.title1



class Idea(models.Model):
    title2 = models.CharField(max_length=150)
    excerpt2 = models.CharField(max_length=200)
    image_name2 = models.CharField(max_length=100)
    date2 = models.DateTimeField(auto_now_add=True)
    slug2 = models.SlugField(unique=True, db_index=True)
    content2 = models.TextField(validators=[MinLengthValidator(10)])
    author2 = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="ideas"
    )

    def __str__(self):
        return self.title2