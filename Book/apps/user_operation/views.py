from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from user.models import UserInfo,Administrator
from .models import UserOperation,UserReturnBook
from book_list.models import BookCategory,BookList


# Create your views here.
from datetime import time
import json
from datetime import datetime

def indexon(request):
    borrowed = []
    returnbook = []
    List = []
    if request.method == 'GET':
        if 'email' in request.session:
            try:
                user = UserInfo.objects.get(email=request.session['email'])
                booklist = BookCategory.objects.all()
                for i in booklist:
                    List.append(i.category)
                name = user.name
                email = user.email
                money = user.money
                phone_num = user.phone_num
                birthday = user.birthday
                hobby = user.hobby
                say = user.say
                # if phone_num==None:
                #     phone_num="xxx"
                # if birthday==None:
                #     birthday = "xxx"
                # if hobby==None :
                #     hobby = "xxx"
                # if say==None:
                #     say = "xxx"
                # # print(phone_num,birthday,hobby,say)
                userinfo = {
                    'name':name,
                    "email":email,
                    "money":money,
                    "phone_num":phone_num,
                    "birthday":birthday,
                    "hobby":hobby,
                    "say":say
                }
                id = user.id
                borrow_book = UserOperation.objects.filter(name_id=id)
                for book in borrow_book:
                    if book.is_back:
                        id = book.id
                        bname = book.book_name.name
                        bimage = "/" + book.book_name.image.url
                        bdata = book.day.strftime('%Y-%m-%d %H:%M:%S')
                        try:
                            bookback = UserReturnBook.objects.get(borrow_id=id)
                            btime = bookback.backtime.strftime('%Y-%m-%d %H:%M:%S')
                            returnall = {
                                "bname": bname,
                                "bimage": bimage,
                                "bdata": bdata,
                                "btime": btime
                            }
                            returnbook.append(returnall)
                            print(returnbook)
                        except:
                            pass

                    else:
                        bookname = book.book_name.name
                        bookimage = "/"+book.book_name.image.url
                        author = book.book_name.author
                        press = book.book_name.press
                        data = book.day.strftime('%Y-%m-%d %H:%M:%S')
                        all = {
                            "bookname":bookname,
                            "bookimage":bookimage,
                            "author":author,
                            "data":data,
                            "press":press
                        }
                        borrowed.append(all)
                return render(request, 'index.html', {'name': name,"borrowed":json.dumps(borrowed),"returnbook":returnbook,'userinfo':userinfo,"List":List})
            except:
                pass
        else:
            return redirect('/')
    else:
        try:
            uinfo = UserInfo.objects.get(email=request.session['email'])
            if request.POST.get("phone") =="":
                pass
            else:
                uinfo.phone_num = request.POST.get("phone")
            if request.POST.get("birthday") =="":
                pass
            else:
                uinfo.birthday = request.POST.get("birthday")
            if request.POST.get("hobby") =="":
                pass
            else:
                uinfo.hobby = request.POST.get("hobby")
            if request.POST.get("message") =="":
                pass
            else:
                uinfo.say = request.POST.get("message")
            uinfo.save()
            return redirect('/index')
        except:
            return redirect('/')

def adminon(request):
    if request.method =="GET":
        if "username" in request.session and 'pwd' in request.session:
            return render(request,"adminindex.html")
        else:
            return redirect('/adminlogin')
    else:
        return render(request,'adminindex.html')


def portfolio(request):
    list = []
    bookcategory = BookCategory.objects.all()
    for i in bookcategory:
        list.append(i.category)
    if request.method == "GET":
        if "username" in request.session and 'pwd' in request.session:
            return render(request,"portfolio.html",{'list':list})
        else:
            return redirect('/adminlogin')
    else:
        if request.POST.get("category") == "":
            return render(request, 'portfolio.html', {"mes": "请选择类别"})
        else:
            name = request.POST.get("bookname")
            author = request.POST.get("author")
            press = request.POST.get("press")
            cate = request.POST.get("category")
            num = request.POST.get("num")
            price = request.POST.get("price")
            img = request.FILES.get("image").name
            imgfile = request.FILES.get('image')
            print(img)
            print(imgfile)
            print(type(imgfile))
            print(type(img))
            try:
                category = BookCategory.objects.get(category=cate)
                print(type(category))
                postfix = img.split(".")[1]
                if postfix == "jpg" or postfix == "png" or postfix == "jpeg" or postfix == "bmp" or postfix == "gif" or postfix == "tiff":
                    imgname = '%s/%s' % ('static/images/goods', img)
                    print(imgname)
                    with open(imgname, 'wb') as f:
                        f.write(imgfile.read())
                    Book = BookList()
                    Book.name = name
                    Book.author = author
                    Book.press = press
                    Book.category_id = category.id
                    Book.num = num
                    Book.price = price
                    Book.image = imgname
                    print(postfix)
                    Book.save()
                    return HttpResponseRedirect('/portfolio')
                else:
                    return render(request, "portfolio.html", {'mes': "图片格式不正确", 'list': list})
            except Exception as e:
                print(e)
                return render(request, 'portfolio.html', {"mes": "数据库中未包含选择的类型", 'list': list})


def team(request):
    if request.method == "GET":
        if "username" in request.session and 'pwd' in request.session:
            return render(request,"team.html",{'list':list})
        else:
            return redirect('/adminlogin')
    else:
        byone = request.POST.get("byone")
        if byone == "借书":
            uname = request.POST.get("username")
            bookname = request.POST.get("bookname")
            try:
                booklist = BookList.objects.get(name=bookname)
                try:
                    user = UserInfo.objects.get(name=uname)
                    if len(UserInfo.objects.filter(name=uname)) <= 0:
                        return render(request, 'team.html', {"error": "用户名不存在"})
                    booklist.num = int(booklist.num) - 1
                    borrow = UserOperation(book_name_id=booklist.id, name_id=user.id)
                    borrow.save()
                    booklist.save()
                    return HttpResponseRedirect('/team')
                except:
                    return render(request, 'team.html', {"error": "该用户名不存在"})
            except Exception as e:
                print(e)
                return render(request, 'team.html', {"error": "书库中没有此书"})
        elif byone == "还书":
            uname = request.POST.get("username")
            bookname = request.POST.get("bookname")
            try:
                booklist = BookList.objects.get(name=bookname)
                user = UserInfo.objects.get(name=uname)
                if len(UserInfo.objects.filter(name=uname)) <= 0:
                    return render(request, 'team.html', {"error": "用户名不存在"})
                try:
                    borrowbook = UserOperation.objects.get(book_name_id=booklist.id, name_id=user.id)
                    booklist.num = int(booklist.num) + 1
                    borrowbook.is_back = True
                    giveback = UserReturnBook(borrow_id=borrowbook.id)
                    giveback.save()
                    borrowbook.save()
                    booklist.save()
                    return HttpResponseRedirect('/team')
                except:
                    return render(request, 'team.html', {"error": "该用户没有借过本书"})
            except Exception as e:
                print(e)
                return render(request, 'team.html', {"error": "书库中没有此书"})

def invest(request):
    if request.method == "GET":
        if "username" in request.session and 'pwd' in request.session:
            return render(request,"invest.html")
        else:
            return redirect('/adminlogin')
    else:
        if "money" in request.POST:
            name = request.POST.get("name")
            print(name)
            money = request.POST.get("money")
            try:
                user = UserInfo.objects.get(name=name)
                print(user)
                print(user.money)
                print(float(money))
                print(type(user.money))
                user.money = float(user.money) + float(money)
                user.save()
                return render(request,'invest.html',{"message":"充值成功",})
            except:
                return render(request,'invest.html',{"name":name,"message":"用户名不存在"})
