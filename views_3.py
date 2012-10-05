# Create your views here.

def home(request):
	import datetime	
	from django.shortcuts import render
	context = { }
	context['ts'] = datetime.datetime.now()
	return render(request, 'home.html', context)

def listing(request, sub):
	import os
	import time
	from django.shortcuts import render
	context = { }
	dir_name = '/var/log' + '/' + str(sub)
	context['dir_name'] = dir_name
	context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
	context['tbl_content'] = []
	for f in context['dir_content']:
		row = []
		fullname = os.path.join(dir_name, f)
		sz = os.path.getsize(fullname)
		stat = os.stat(fullname)
		t = time.localtime(stat.st_mtime)
		ct = str(t[2])+'/'+str(t[1])+'/'+str(t[0])+' '+str(t[3])+':'+str(t[4])+':'+str(t[5])
		row.append(f)
		row.append(sz)
		row.append(ct)
		context['tbl_content'].append(row)
	return render(request, 'listing.html', context)