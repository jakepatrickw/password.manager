import logging
from django.shortcuts import render
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


class PassLister(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pass_lister.html'

    def get(self, request):
        queryset = UsernamePasswordService.objects.all()
        return Response({'passwords':queryset})

# def PassLister(request):
#     form = PassWordForm
#     return render(request, 'pass_lister.html', {'form':form})



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
