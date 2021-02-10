
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")
    #return render(request, 'polls/home.html')

'''

from django.shortcuts import render  

#importing loading from django template  
from django.template import loader  
    
# Create your views here.  
from django.http import HttpResponse  
def index(request):  
    template = loader.get_template('home.html') # getting our template  
    return HttpResponse(template.render())       # rendering the template in HttpResponse  

'''