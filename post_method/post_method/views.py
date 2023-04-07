from django.shortcuts import render, HttpResponse

def home(request):
    if request.method == "GET":
        name = ['AA','BB','NN']
    context = {
        'name': name
    }
    return render(request,'home.html',context)

def contact(request):
    if request.method == "POST":
        email = request.POST['email']
        comment = request.POST['comment']
        print('email: ' +email+ ' comment: ' +comment)
    return render(request,'contact.html')