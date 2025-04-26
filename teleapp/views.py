from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment, Contact

# Create your views here.

def home(request):
    """ Displays the landing page"""
    return render(request, "pages/index.html")


def about(request):
    """ Displays the about page"""
    return render(request, "pages/about.html")

def contacts(request):
    """Displays contacts page"""
    if request.method == 'POST':
        # Create a variable to pick the input fields
        contacts = Contact (
            # List the input fields
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        # Save the variable
        contacts.save()
        # Redirect
        return redirect('teleapp:home')
    else:
        return render(request, "pages/contact.html")

def services(request):
    """Displays the services page"""
    return render(request, "pages/services.html")


# Function to push the appointment to DB
def appointment(request):
    """Function to push the appointment to DB"""
    # Check if its a POST method
    if request.method == 'POST':
        # Create a variable to pick the input fields
        appointments = Appointment (
            # List the input fields
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        # Save the variable
        appointments.save()
        # Redirect
        return redirect('teleapp:home')
    else:
        return render(request, 'pages/appointment.html')

# Retrieve all appointments
def fetch_appointments(request):
    """Retrieves all appointments"""
    # Create a variable to store the appointments
    appointments = Appointment.objects.all()
    context = {'appointments':appointments}
    return render(request, "pages/show_appointments.html", context)

# Delete 
def delete_appointment(request, id):
    """Deletes appointment"""
    appointment = Appointment.objects.get(id=id)

    appointment.delete()

    return redirect("teleapp:show_appointments")

def update_appointment(request, appointment_id):
    """ Update the appointments """
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.name = request.POST.get('name')
        appointment.email = request.POST.get('email')
        appointment.phone = request.POST.get('phone')
        appointment.date = request.POST.get('date')
        appointment.doctor = request.POST.get('doctor')
        appointment.department = request.POST.get('department')
        appointment.message = request.POST.get('message')

        appointment.save()
        return redirect("teleapp:show_appointments")
        
    context = {'appointment':appointment}
    
    return render(request, "pages/update_appointments.html", context)
