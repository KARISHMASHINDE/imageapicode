from rest_framework.parsers import FileUploadParser,FormParser
from .models import apiuser,imageprofile
from .serializers import userSerializer,profileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class userList(APIView):
   
    def get(self, request, format=None):
        obj = apiuser.objects.all()
        serializer = userSerializer(obj, many=True)
        return Response(serializer.data)

class userpost(APIView):

    def post(self, request, format=None):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # parser_class = (FileUploadParser,FormParser)
    # def post(self, request, *args, **kwargs):
    #     serializer = userSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
    
class userDetail(APIView):
   
    def get_object(self, pk):
        try:
            return apiuser.objects.get(pk=pk)
        except apiuser.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = userSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = userSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class profileList(APIView):
       
    def get(self, request, format=None):
        obj = imageprofile.objects.all()
        serializer = profileSerializer(obj, many=True)
        return Response(serializer.data)

class profilepost(APIView):

    def post(self, request, format=None):
        serializer =profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
    
class profileDetail(APIView):
   
    def get_object(self, pk):
        try:
            return imageprofile.objects.get(pk=pk)
        except apiuser.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = profileSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = profileSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


