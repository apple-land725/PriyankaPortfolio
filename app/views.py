from django.shortcuts import render, redirect
from .models import Inquiry

from .import models


# Create your views here.

def IndexPageView(request):
    return render(request,"app/index.html")

def ContactView(request):
    return render(request, 'app/contact.html')


def InsertData(request):
     if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        query=request.POST['query']
        link=request.POST['link']

        newuser = Inquiry.objects.create( Entername = fname, Company = lname, Email = email, Contact = contact, Message = query, Link = link)
    # newuser.save() 
        return render(request, 'app/thank.html')
    # else:
            # If it's not a POST request, create an empty form
        # return render(request, 'app/contact.html')
       
 
    # return redirect('indexpage')
def ThankView(request):
    return render(request, 'app/thank.html')
   








# def ContactView(request):
#     if request.method == 'POST':
#         form = forms.ContactForm(request.POST)  # Create an instance of the ContactForm
#         if form.is_valid():
#             # Process the form data (e.g., save to database)
#             # Redirect to another page after processing
#             return redirect('app:index')  # Replace 'app:index' with the appropriate URL name
#     # else:
#     #     form = forms.ContactForm()  # Create an empty form instance

#     return render(request, 'app/contact.html', {'form': form})
    











# def ContactView(request):
     

#     if request.method == 'POST':
#         agreed = request.POST.get('agreed')
#         if agreed:
#             # Logic for processing the form data goes here
#             messages.success(request, 'Thank you for agreeing to the terms and conditions!')
#             return redirect('index')  # Redirect to the index page after successful submission
#         else:
#             messages.error(request, 'You must agree to the terms and conditions to submit the form.')

#     return render(request, 'app/contact.html')

# Create your views here.
