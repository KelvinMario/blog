from django.shortcuts import render,get_object_or_404,redirect
from .forms import MessageForm

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():

            message = form.save()

            return render(request,'blog/blog.html')
        else:
            return render(request,'blog/contact.html')

    return render(request,'blog/contact.html')