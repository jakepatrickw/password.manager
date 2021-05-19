import logging
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
                                    DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import UsernamePasswordService
from .serializer import PassWordSerializer, UpdatePassWordSerializer
import html
from .forms import PassWordForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def profile(request):
    passwords = UsernamePasswordService.objects.all()
    return render(request, 'home.html', {'passwords':passwords})


def pass_lister(request, pk):
    password = UsernamePasswordService.objects.get(pk=pk)
    form = PassWordForm(instance=password)
    return render(request, 'pass_lister.html', {'passwordform':form, 'password':password})


class ListPassword(ListAPIView):
    queryset = UsernamePasswordService.objects.all()
    serializer_class = PassWordSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]


class CreatePassword(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PassWordSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeletePassword(DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = PassWordSerializer
    queryset = UsernamePasswordService.objects.all()
    lookup_field = 'id'

class UpdatePassword(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UpdatePassWordSerializer
    queryset = UsernamePasswordService.objects.all()
    lookup_field = 'id'
