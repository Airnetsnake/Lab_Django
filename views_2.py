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
	dir_name = '/var/log' + '/' + str(sub)
	context['dir_name'] = dir_name
	context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
	context['dir'] = []
	context['f'] = []
	for f in context['dir_content']:
		fullname = os.path.join(dir_name, f)
		if os.path.isdir(fullname):
			context['dir'].append(f)
		else:
			context['f'].append(f)
	return render(request, 'listing.html', context)