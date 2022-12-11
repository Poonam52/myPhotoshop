import re
from django.utils.crypto import get_random_string
from django.http import JsonResponse
from rest_framework import generics, status, viewsets
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from myPhotoshop.settings import BASE_DIR
from webapp.forms import ImageForm
from webapp.models import imageProcess
from PIL import Image

from webapp.serializers import ImageProcessSerializer


class ProcessImageCreateAPIView(generics.CreateAPIView):
    queryset = imageProcess.objects.all()
    serializer_class = ImageProcessSerializer
    permission_classes = []
    authentication_classes = []

class ProcessImage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = ImageForm
        return render(request, 'index.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ImageForm()
        return render(request, 'index.html', {'form': form})

def remove(string):
    pattern = re.compile(r'\s+:')
    return re.sub(pattern, '', string)


class ImageProcessViewSet(viewsets.ModelViewSet):
    queryset = imageProcess.objects.all()
    serializer_class = ImageProcessSerializer

@api_view(['GET'])
def GetManipulated_Image(requests):
    filepath = str(BASE_DIR) + requests.GET.get('imgurl')
    print(filepath)
    imacr = Image.open(filepath)
    if (requests.GET.get('optname') == 'flip'):
        imacr = imacr.transpose(Image.FLIP_LEFT_RIGHT)
    elif (requests.GET.get('optname') == 'rotate'):
        imacr = imacr.rotate(270, expand=True)
    elif (requests.GET.get('optname') == 'grayscale'):
        imacr = imacr.convert('L')
    elif (requests.GET.get('optname') == 'crop'):
        box = (200, 300, 700, 600)
        imacr = imacr.crop(box)
    elif (requests.GET.get('optname') == 'thumbnail'):
        imacr.thumbnail((90,90))
    elif (requests.GET.get('optname') == 'rotateleft'):
        imacr = imacr.rotate(90, expand=True)
    elif (requests.GET.get('optname') == 'rotateright'):
        imacr = imacr.rotate(270, expand=True)
    else:
        imacr = imacr

    unique_id = get_random_string(length=7)
    imgname = 'rtrimg_' + str(unique_id) + '.jpg'
    fpath = '/media/images/' + imgname
    imgpath = str(BASE_DIR) + fpath
    imacr.save(imgpath, 'JPEG')
    imacr.close()
    return JsonResponse({'imgpath': str(fpath)}, status=status.HTTP_200_OK)





