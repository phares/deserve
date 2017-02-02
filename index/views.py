from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def contactus(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        form = ContactUsForm(request.POST)

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        send_to = 'abungaphares@gmail.com'

        subject = 'New Contact US Form SignUp'


        mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Phone" + " " + phone + "Message" + " " + message

        sendmail(send_to, subject, mail)

        messages.success(request, 'Thank you for contacting us. '
                                  'Your message has been received, o'
                                  'ne of our representatives will be '
                                  'in touch with you shortly')

         #  redirect to a new URL:

        return HttpResponseRedirect('/contact/')

    # if a GET (or any other method) we'll create a blank form
    else:

        return HttpResponseRedirect('/contact/')
        form = ContactUsForm()

    return HttpResponseRedirect('/contact/')
    #return render(request, '/contacts/', {'form': form})


def sendmail( to, subject, message ):

    send_mail(subject, message, 'abungaphares@gmail.com',
              [to], fail_silently=True)

    return