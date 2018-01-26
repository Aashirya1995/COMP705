from django.shortcuts import render

def home(request):
	'''
	renders the homepage
	'''
	greeting = "Welcome to WeStudy, its the BEST"
	# create a variable with the days of the week as list in it
	days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ]
	# Then we add it to the template context
	context = {'our_greeting': greeting, 'weekday_list' : days_of_week } #empty dic
	return render(request, 'home.html', context)
