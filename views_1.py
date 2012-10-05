# Create your views here.

def home(request):
	import datetime	
	from django.shortcuts import render
	context = { }
	context['ts'] = datetime.datetime.now()
	return render(request, 'home.html', context)

def listing(request, sub):
	import os
	from django.shortcuts import render
	context = { }
	if sub == '':
		context['dir_name'] = '/var/log'
		context['dir_content'] = os.listdir('/var/log')
	else:
		context['dir_name'] = '/var/log' + '/' + str(sub)
		context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
	return render(request, 'listing.html', context)