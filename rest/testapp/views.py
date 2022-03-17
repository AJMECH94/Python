from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import Empserializer
from .models import Emp
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from rest_framework import mixins

class EmpCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset = Emp.objects.all()
    serializer_class = Empserializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmpRetriveUpdateDestroyModelMixin(mixins.DestroyModelMixin,mixins.UpdateModelMixin,RetrieveAPIView):
    queryset = Emp.objects.all()
    serializer_class = Empserializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

"""class ListApi(ListAPIView):
    queryset = Emp.objects.all()
    seializer_class = Empserializer

class EmplistApi(ListAPIView):
    queryset = Emp.objects.all()
    serializer_class = Empserializer

class EmpListCreateApiView(ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = Empserializer

class EmpRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = Empserializer"""

