from django.contrib import admin
from .models import Post, Contact, Author, Tag, Blog, Idea, ContactMessage

admin.site.register(Idea)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(ContactMessage)