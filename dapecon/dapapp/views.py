from django.shortcuts import render, redirect
from .models import Post, Blog, Idea
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import ContactMessage


def thank_you(request):
    return render(request, 'thankyou.html')

def contact_view(request):
    message_sent = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            message_sent = True
            return render(request, 'thankyou.html')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form, 'message_sent': message_sent})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'post_detail.html', context)



def post_detail1(request, slug1):
    blog = get_object_or_404(Blog, slug1=slug1)
    context = {'post': blog}  # Change 'blog' to 'post' to match the template variable name
    return render(request, 'post_detail1.html', context)



def blogs(request):
    blogs = Blog.objects.all().order_by('-date1')
    sorted_posts = Post.objects.all().order_by('-date')
    context1 = {
        'blogs': blogs, 
         'posts': sorted_posts,
    }
    return render(request, 'anakinosis.html', context1)





def arxiki(request):
    latest_anakinosis_post = Blog.objects.latest('date1')
    latest_posts_post = Post.objects.latest('date')
    latest_ideas_post = Idea.objects.latest('date2')
    context = {
        'latest_anakinosis_post': latest_anakinosis_post,
        'latest_posts_post': latest_posts_post,
        'latest_ideas_post': latest_ideas_post,
    }
    return render(request, 'arxiki.html', context)

    

def istoria(request):
    ideas = Idea.objects.all().order_by('-date2')
    context3 = {
        'ideas': ideas,
    }
    return render(request, 'istoria.html', context3)






   

    
def post_detail2(request, slug2):
    idea = get_object_or_404(Idea, slug2=slug2)
    context = {'idea': idea}  # Change 'blog' to 'post' to match the template variable name
    return render(request, 'post_detail2.html', context)
