from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class HomePageView (TemplateView):
	template_name = "home.html"

	def get_context_data(self):
		data = {"message_title" : "Hello!",
				"message_content" : "EXO"
		}
		return data
	
class AboutPageView (TemplateView):
	template_name = "about.html"
