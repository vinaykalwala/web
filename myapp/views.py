# views.py
# views.py

from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from .models import  Jobs

def service(request):
    images = Image.objects.all()
    return render(request, 'service.html', {'images': images})


def home(request):
    return render(request, 'home.html')

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'Aboutus.html')

def apply(request):
    return render(request, 'Apply.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def career_page(request):
    # Retrieve all job objects from the database
    all_jobs = Jobs.objects.all()
    # Pass the data to the template
    return render(request, 'career_page.html', {'jobs': all_jobs})






def submit_application(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        mobile = request.POST['mobile']
        role = request.POST['role']
        resume = request.FILES['resume']

        # Save form data to the database
        application = JobApplication(name=name, email=email, address=address, mobile=mobile, role=role, resume=resume)
        application.save()

        subject = 'Job Application Submitted'
        message = f'Thank you for applying for the position at Vindus, {name}! Your application has been received successfully.'
        from_email = 'your@example.com'  # Replace with your email
        to_email = [email]  # Send email to the applicant
        send_mail(subject, message, from_email, to_email)

        return redirect('home')  # Redirect to a success page or another URL
    else:
        return render(request, 'Apply.html')
    

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')

        contact_form = Enquiry(name=name, mobile=mobile, email=email, address=address, message=message)
        contact_form.save()

        return redirect('contactus.html')  # Redirect to a success page after saving the form data
    else:
        return render(request, 'contactus.html')  # Replace 'your_template.html' with the actual template name