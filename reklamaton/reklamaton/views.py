from django.http import HttpResponse

#from my_project.example.models import Profile
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django import forms

class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response({'result':False})
    def post(self,request):
        print(request.POST)
        for key, value in request.POST.items():
            print('Key: %s' % (key) )
        message = 'ggggggg'#request.POST['message']
        return Response({'result':True, 'message':message})

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")