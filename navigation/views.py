
from django.shortcuts import render
from django.views.generic import View

#
class HomeView(View):
    """
    """
     
    #
    def get(self, request):
        """
        """
        # 
        template_name   = "navigation/home.html"
        # 
        context         = {} 
        #
        return render(request, template_name, context)

#
class FAQView(View):
    """
    """
     
    #
    def get(self, request):
        """
        """
        # 
        template_name   = "navigation/faq.html"
        # 
        context         = {} 
        #
        return render(request, template_name, context)

