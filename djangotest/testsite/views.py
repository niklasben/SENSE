from django.shortcuts import render_to_response, render
from django.forms import ModelForm


# Create your views here.
def index(request):
    """Hello World."""
    return render_to_response('index.html')


def contact(request):
    """Contact Form."""
    form_class = ModelForm

    return render(request, 'contact.html', {
        'form': form_class,
    })
