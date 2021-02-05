from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests
# Create your views here.




class ArticleAPIView(APIView):

    def get(self,request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ArticleDetails(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        article=self.get_object(id)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self,request,id):
        article=self.get_object(id)
        serializer=ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article=self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def article_list(request):

    if request.method=='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method=='POST':

        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method=='GET':
        serializer=ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method=='PUT':
       
        serializer=ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# def home(request):
#     response = requests.get('http://127.0.0.1:8000/article')
#     geodata = response.json()
#     print(geodata)
#     return render(request, 'api_basic/home.html', {
#         'ip':'India',
#         'country': 'PATNA',
#     })

# def homePost(request):
#     url='http://127.0.0.1:8000/article/'
#     obj={
#         "title": "post request article",
#         "author": "sahil kalamkar",
#         "email": "sh7@gmail.com"
#     }

#     x=requests.post(url,data=obj)

#     print(x)
#     return HttpResponse('A post request was successfully made')
