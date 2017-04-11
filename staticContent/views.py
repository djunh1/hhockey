from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy

from easy_timezones.utils import get_ip_address_from_request
from axes.utils import reset


from staticContent.forms import ContactForm, AxesCaptchaForm



def home(request):
    return render(request, 'site/home.html')


def about(request):
    return render(request, 'site/about.html')

def plans(request):
    return render(request, 'site/plans.html')

def contact(request):
    sent = False
    if request.method == 'POST':
        form_class = ContactForm(data=request.POST)
        if form_class.is_valid():
            cd = form_class.cleaned_data
            template = get_template('contact/contact_template.txt')
            subject = '{} at ({}) has sent an email from Hopewell Hockey'.format(cd['contact_name'],
                        cd['contact_email'])
            message = 'HOPEWELL HOCKEY - message from our Application as follows: \n\n {}' \
                      '\n\n\nREPLY TO EMAIL: {}'.format(cd['content'], cd['contact_email'])
            send_mail(subject,
                      message,
                      'info@hopewellhockey.com',
                      ['douglas.jacobson@hopewellhockey.com', 'brian.deangelis@hopewellhockey.com'],
                      fail_silently=False)
            sent = True
    else:
        sent = False
        form_class = ContactForm
    return render(request, 'site/contact.html',
                {'form': form_class, "sent": sent}
    )


def faq(request):
    return render(request, 'site/freqQuest.html')


def locked(request):
    if request.POST:
        form = AxesCaptchaForm(request.POST)
        if form.is_valid():
            ip = get_ip_address_from_request(request)
            reset(ip=ip)
            return HttpResponseRedirect(reverse_lazy('customer:login'))
    else:
        form = AxesCaptchaForm()

    return render_to_response('site/locked.html', dict(form=form), context_instance=RequestContext(request))


def toc(request):
    return render(request, 'site/toc.html')


def privacy(request):
    return render(request, 'site/privacyPolicy.html')


def sticks(request):
    return render(request, 'site/sticks.html')


def warranty(request):
    return render(request, 'site/warranty.html')

