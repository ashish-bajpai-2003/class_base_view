from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.

## function based view
# def myview(request):
#     return HttpResponse('<h1>Function Based View</h1>')


# class Myview(View):
#     name = 'Ashish Bajpai'
#     def get(self,request):
#         # return HttpResponse('<h1>Class Based View</h1>')
#         return HttpResponse(self.name)

# class MyviewChild(Myview):

#     name = 'Swet'
#     def get(self,request):
#         return HttpResponse(self.name)

def homefun(request):
    context = {'msg' : 'Welcome to the world of Function Based view.'}
    return render(request,'home.html',context)


class HomeClassView(View):
    def get(self,request):
        context = {'msg' : 'Welcome to the world of class Based view.'}
        return render(request,'home.html',context)


##############################################################
def contactfun(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you for Submitted form.') 
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})


class ContactClassView(View):
    def get(self,request):
        form = ContactForm()
        return render(request, 'contact.html',{'form':form})
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you for Submitted form.') 
        
##########################################################################

def newsfun(request):
    context = {'info':'Ashish is a boy, that is learning Django.'}
    return render(request, 'news.html', context)