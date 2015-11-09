# Create your views here.
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib import auth
from libymanage.models import Book, Author
from django.template import Context
from django.shortcuts import render_to_response
#from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login#, logout
# Create your views here.
def main(request):
    return render_to_response("main.html")
     
#def sign(request):
#     return render_to_response("signup.html")
#我的天
def more(request):
    return render_to_response("more.html") 
def signup(request):
    right=""
    if request.POST:       
        username = request.POST["username"]  
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            try:
                user = User.objects.create_user(username=username,password=password)  
                user.save()
                user = auth.authenticate(username=username, password=password)
                auth.login(request,user)
                return HttpResponseRedirect("/login/")
            except:
                right="user is already exist."
                return  render_to_response("signup.html",{"right":right})
        else:
            right="Entered passwords differ."
            return  render_to_response("sign.html",{"right":right})
    else:
        return render_to_response("sign.html")
        
def loginsure(request):
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/mainpage/")
            else:
                return render_to_response('Error.html')
        else:
            return render_to_response('Error.html')
    else:
        return render_to_response('mylogin.html')
    

def mainpage(request):
 #   right = ""
  #  flag = 0
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    if request.POST:
        post = request.POST
        authorname = post["name"]
        temp = post["sname"]
        s = Author.objects.filter(name=authorname)
        s1 = Author.objects.filter(name=temp)
        if s:
           person = Author.objects.get(name = authorname)
           book = person.book_set.all()
         #  authorname = Context({"authorname":Author.objects.get(name = authorname)})
           return render_to_response('newshow.html', {"books":book, "authorname": authorname})
        elif s1:
           # request.session['authorname'] = temp
            temp = "/add/" + str(temp)
            return  HttpResponseRedirect(temp)
        else:
           # right = "the author is not exist"
            return  HttpResponseRedirect('/addau/')
           
    else:
        return render_to_response("mainpage.html")           

 
#addbook then search   
def search(request, authorname):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    try:
        person = Author.objects.get(name = authorname)
        book = person.book_set.all()
    except:
        return  HttpResponseRedirect('/addau/')
   # c = Context({"people_list": People.objects.filter(user=request.user.username),"user":user})
    return render_to_response('newshow.html',{"books":book, "authorname":authorname})

def addauthor(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    if request.POST:
        post = request.POST
        temp = post["name"]
        if not Author.objects.filter(name = temp):
            new_au = Author(
                    authorid = Author.objects.all().count()+1,
                    name = post["name"],
                    age = post["age"],
                    country = post["country"])
            new_au.save()
            return render_to_response('addauthor.html')
        else:
            right = "author is already exist"
            return render_to_response('addauthor.html',{"right":right})
    else:
        return render_to_response('addauthor.html')
        
    
def add(request, authorname):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
   # user=request.user.username
    if request.POST:
       post = request.POST
       authorid = Author.objects.get(name = authorname)
       new_book = Book(
          ISBN = post["isbn"],
          title = post["title"],
          authorid = authorid,
          publisher = post["publisher"],
          publishdate = post["publishdata"],
          price = post["price"])
  #  new_book.authorid.add(Author.objects.filter(authorid = post["authorid"]))
       new_book.save()
  #  new_book.authorid.add(Author.objects.filter(authorid = post["authorid"]))
    return render_to_response('myaddbook.html', {"authorname":authorname})
        #else:
           #return render_to_response('addbook.html')
        
   # else:
       #  return render_to_response('addbook.html')
  #  else:
      #  return render_to_response("addbook.html",Context({"user":user}))
     
def shownews(request, isbn):
     if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
     c = Context({"book": Book.objects.filter(ISBN=isbn)})
  #  book = person.book_set.all()
   # c = Context({"people_list": People.objects.filter(user=request.user.username),"user":user})
     return render_to_response('shownews.html',c) 
     
def delete(request, idbook):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    book = Book.objects.get(ISBN = idbook)
    auth = Author.objects.get(name = book.authorid.name)
    newbook = auth.book_set.all()
    book.delete()   
    return render_to_response('newshow.html',{"books": newbook})
   
def update(request, isbn):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    news = "000"
    if isbn != '':
        book = Book.objects.get(ISBN = isbn)
        flag = 0
     #   auth = Author.objects.get(name = book.authorid.name)
        if request.POST:
           post = request.POST
           if post["name"] != '':
               flag = 1
               try:
                   auth1 = Author.objects.get(name =  post["name"])
                   book.authorid = auth1 
               except:
                 #  right = "author is not exist"
                   return   HttpResponseRedirect('/addau/')
                   
           if post["publisher"] != '':
                flag = 1
                book.publisher =  post["publisher"]
               
           if post["publishdata"] != '':
               flag = 1
               book.publishdata = post["publishdata"] 
               
           if post["price"] != '':
               flag = 1
               book.price = post["price"] 
               
           if flag == 1:
              book.save() 
               
           else:
               news = "no input data, please check"
               return   render_to_response('myupdate.html', {"news":news})
        return render_to_response('myupdate.html', {"booknews": book})
    return  render_to_response('myupdate.html', {"news":news})
           
           
           
           
               
            
          
    
    # Create your views here.
