from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginpage(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			return redirect('/allrequest')
		else:
			return render(request, "loginpage.html")
	elif request.method == "POST":
		if request.user.is_authenticated:
			return redirect('/allrequest')
		elif "emailid" in request.POST and "password" in request.POST and request.POST['emailid'] in [_.emailid for _ in WebUsers.objects.all()]:
			user = authenticate(username=request.POST['emailid'], password=request.POST['password'])
			if user is not None:
				login(request, user)
				return redirect('/allrequest')
			else:
				return HttpResponse("Invalid Credentials")
		else:
			return HttpResponse("Invalid Credentials")
	else:
		return redirect('/login')

def requestpage(request):
	if request.method == "GET":
		return render(request)
	elif request.method == "POST" and all(list(map(lambda x:x in request.POST and request.POST[x] != '', ['reqtype', 'reqdesc', 'city', 'state', 'pincode', 'altmobile', 'ccode']))):
		req = RequestList(reqtype=request.POST['reqtype'], reqdesc=request.POST['reqdesc'], city=request.POST['city'], state=request.POST['state'], pincode=request.POST['pincode'], countrycode=request.POST['ccode'], mobileno=request.POST['altmobile'])
		try:
			req.full_clean()
			req.save()
			return HttpResponse("Request Submitted")
		except ValidationError as e:
			return HttpResponse("<br>".join(e.messages))
	else:
		return redirect('/new')

def allrequestpage(request):
	if request.method == "GET":
		return render(request, "allrequests.html", context={'reqs': RequestList.objects.all()})
	else:
		return redirect('/all')

def updatepage(request):
	if request.method == "GET":
		return render()
	elif request.method == "POST":
		return render()
	else:
		return redirect('/update')

def viewrequestpage(request):
	if request.method == "GET":
		return render()
	else:
		return redirect('/view')