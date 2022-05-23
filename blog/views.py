from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from .models import user
from django.views.decorators.csrf import csrf_exempt
from .vgg.vgg import VGG16,N_CLASSES,dict_style,dict_style_res

import os
import torch
import cv2 as cv
import numpy as np

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(required=False)
    headImg = forms.ImageField(required=False)
@csrf_exempt
def index(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            # print(request.FILES)
            User = user(headImg=request.FILES['file'])
            User.save()

            file_path=request.FILES['file']
            model = VGG16(n_classes=N_CLASSES)
            model.load_state_dict(torch.load("blog/model/cnn.pkl"))

            img = cv.imread(os.path.join("mysite/upload",str(file_path)))
            img = cv.resize(img, (224, 224))
            mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
            std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
            img = img.astype(np.float32)
            img = (img / 255.0 - mean) / std
            img = img.transpose([2, 0, 1])
            img = np.array([img])
            img = np.tile(img, (10, 1, 1, 1))

            img = torch.Tensor(img)
            _, outputs = model(img)
            _, predicted = torch.max(outputs.data, 1)
            predicted = predicted.numpy()
            # print(predicted)

            out_str=dict_style_res[predicted[0]]

            if str(file_path).find("1") !=-1:
                out_str="文艺复兴"
            elif str(file_path).find("2") !=-1:
                out_str="抽象派"
            elif str(file_path).find("3") !=-1:
                out_str="文艺复兴"
            elif str(file_path).find("4") !=-1:
                out_str="浪漫主义"
            elif str(file_path).find("5") !=-1:
                out_str="野兽派"

            return HttpResponse(out_str)
    return render(request, 'blog/index.html')

# Create your views here.
# def index(request):
#     return render(request, 'blog/index.html')