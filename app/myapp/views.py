from django.shortcuts import render

# Create your views here.

def first(request):
    number=""
    if 'btn' in request.POST:
        number=int(request.POST['string'])
        if number%2==0:
            number="even"
        else:
            number="odd"       

        
    return render(request,"myapp/index.html",{'ans':number})