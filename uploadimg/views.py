# Create your views here.
from django.views import View
from django.shortcuts import render, redirect
from . models import Image
from .utils import image_editor



class index(View):
    def get(self, request):
        return render(request, 'uploadimg/index.html', {
            })

    def post(self, request):
        image_front = request.FILES.get('image_front')
        image_back = request.FILES.get('image_back')
        color = request.POST.get('tshirt_color')
        position = request.POST.get('position')

        if image_front == None and image_back == None:
            return redirect('index')

        x = image_editor(image_front, color, position, image_back)
        return render(request, 'uploadimg/index.html', {
            'img_front': image_front , 'img_back':image_back
        })