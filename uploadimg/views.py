# Create your views here.
from django.views import View
from django.shortcuts import render, redirect
from . models import Image



class index(View):
    def get(self, request):
        return render(request, 'uploadimg/index.html', {
            })

    def post(self, request):
        image_front = request.FILES.get('image_front')
        image_back = request.FILES.get('image_back')
        color = request.POST.get('tshirt_color')
        position = request.POST.get('position')

        if not image_front:
            return redirect('index')

        image = Image(image=image_front)
        image.save(color=color, position=position)
        return render(request, 'uploadimg/index.html', {
            'img_obj': image.image
        })

    