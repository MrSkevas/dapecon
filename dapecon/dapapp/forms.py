from django import forms
from .models import Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)  # Adjust the max_length according to your needs
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'type': 'tel', 'placeholder': 'Πληκτρολόγησε τον αριθμό τηλεφώνου σου'})
