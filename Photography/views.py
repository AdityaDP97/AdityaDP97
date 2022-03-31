from django.http import HttpResponse
from django.shortcuts import render
from form.models import form

def home(request):
	# data={
	# 'title':'Welcome to the Nature'
	# }
	return render(request,"index.html",)


def catagory(request):
	# data={
	# 'title':'Catagories'
	# }
	return render(request,"catagory.html",)


def birds(request):
	# data={
	# 'title':'Birds'
	# }
	return render(request,"birds.html")


def scenes(request):
	# data={
	# 'title':'Scenes'
	# }
	return render(request,"scenes.html")


def morning(request):
	# data={
	# 'title':'Morning'
	# }
	return render(request,"morning.html")


def flowers(request):
	# data={
	# 'title':'Flowers'
	# }
	return render(request,"flowers.html")


def construction(request):
	# data={
	# 'title':'Constructions'
	# }
	return render(request,"construction.html")


def contact(request):
	# data={
	# 'title':'Contact Us'
	# }
	n=''
	# ContactData=''
	if request.method=='POST':
		name=request.POST.get('name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		msg=request.POST.get('msg')
		er=form(name=name, last_name=last_name, email=email, subject=subject, msg=msg)
		er.save()
		n='DATA INSERTED'
		# ContactData= contact.objects.all()

	return render(request,'contact.html',{'n':n})
	# return render(request,"contact.html",data)


# def SaveDetails(request):
# 	n=""
# 	ContactData=''
# 	if request.method=='POST':
# 		name=request.POST.get('name')
# 		last_name=request.POST.get('last_name')
# 		email=request.POST.get('email')
# 		subject=request.POST.get('subject')
# 		msg=request.POST.get('msg')
# 		en=contactAdmin(name=name, last_name=last_name, email=email, subject=subject, msg=msg,)
# 		en.save()
# 		n='DATA INSERTED'
# 		ContactData= contact.objects.all()

# 	return render(request,'contact.html',{'ContactData':ContactData})
# 	