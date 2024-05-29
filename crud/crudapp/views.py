from django.shortcuts import render,HttpResponse,redirect

from . forms import *

# from .forms import itemform, userform
# from .models import itemsmodel, usermodel


# Create your views here.

def index(request):
    return render(request,'index.html')


def loaditem(request):
    form = itemform
    return render(request,'itemform.html',{'data':form})


def additem(request):
    if request.method == 'POST':
        a = itemform(request.POST,request.FILES)
        if a.is_valid():
            name = a.cleaned_data['name']
            img = a.cleaned_data['img']
            pr = a.cleaned_data['price']
            des = a.cleaned_data['description']

            b = itemsmodel(name=name,img=img,price=pr,description=des)
            b.save()
            #return redirect(shoeitem)
            return HttpResponse('success')
        else:
            return HttpResponse('failed')


def showitem(request):
    a = itemsmodel.objects.all()
    id1 = []
    img = []
    name = []
    des = []
    price = []

    for i in a:
        d = i.id
        id1.append(d)
        path = i.img
        img.append(str(path).split('/')[-1])

        nm = i.name
        name.append(nm)

        desc = i.description
        des.append(desc)

        pr = i.price
        price.append(pr)

    mylist = zip(img, name, des, price, id1)
    return render(request,'showitem.html', {'list': mylist})

#__________________________________________________________________________________

def loaduser(request):
    form = userform
    return render(request,'adduser.html',{'data':form})


def adduserform(request):
    a = usermodel.objects.all()
    id2 = []
    name = []
    email = []
    contact = []
    
    for i in a:

        d = i.id
        id2.append(d)
       
        nm = i.name
        name.append(nm)

        eml = i.email
        email.append(eml)

        cont = i.contact
        contact.append(cont)

    ilist = zip( name, email, contact, id2)
    return render(request,'adduserform.html', {'list': ilist})


        
def adduser(request):
    if request.method == 'POST':
        u = userform(request.POST)
        if u.is_valid():
            name = u.cleaned_data['name']
            email = u.cleaned_data['email']
            contact = u.cleaned_data['contact']

            k = usermodel(name=name,email=email,contact=contact)
            k.save()
            #return redirect(userformitem)
            return HttpResponse('success')
        else:
            return HttpResponse('failed')

#____________________________________________________________________________________________________

def edititem(request,id):
    itm = itemsmodel.objects.get(id=id)
    return render(request,'edititem.html',{'itm':itm})



def updateitem(request,id):
    itm = itemsmodel.objects.get(id=id)
    f = itemform(request.POST,request.FILES, instance=itm) #change cheyyande row veraan
    if f.is_valid():
        f.save()
        return redirect(showitem)
    else:
        return HttpResponse('not valid')
    

    
def deleteitem(request,id):
    itm = itemsmodel.objects.get(id=id) #id illa aale maathram verum
    itm.delete()
    return redirect(showitem)

    

def edituser(request,id):
    user = usermodel.objects.get(id=id)
    return render (request,'edituser.html',{'user':user})
    
def deleteuser(request,id):
        user = usermodel.objects.get(id=id)
        user.delete()
        return render(adduserform)

def updateuser(request,id):
        user = usermodel.objects.get(id=id)
        g = userform(request.POST)
        if g.is_valid():
            g.save()
            return redirect(adduserform)
        else:
            return HttpResponse('not valid')
            
        












# from django.shortcuts import render, redirect, HttpResponse
# from .forms import itemform, userform
# from .models import itemsmodel, usermodel

# def edit_user(request, name):
#     user = usermodel.objects.get(name=name)
#     form = userform(instance=user)
#     if request.method == 'POST':
#         form = userform(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('show_users')  # Redirect to the user list page
    # return render(request, 'edit_user.html', {'form': form})

# def delete_user(request, name):
#     user = usermodel.objects.get(name=name)
#     user.delete()
#     return redirect('show_users')  # Redirect to the user list page







