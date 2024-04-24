from crud import serializer
from crud.models import DetailsModel
from .serializer import DetailsSerializer
from crud.models import CreateTaxModel
from .serializer import CreateTaxModelSerializer
from .serializer import UserSignupSerializer
from .serializer import UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token


#signup
class UserSignup(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                try:
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key})
                except Exception as e:
                        return Response({'error': str(e)})
                        return Response(serializer.errors)

class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})  # Return token in response
        return Response({'error': 'Invalid Credentials'})
    
    

# create and get 
class DetailsTable(APIView):
    def get(self,request):
        detailsObj=DetailsModel.objects.all()
        dlSerializeObj=DetailsSerializer(detailsObj,many=True)
        return Response(dlSerializeObj.data)
     
    def post(self,request):
        serializeobj=DetailsSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)
    
#  update   
class DetailsUpdate(APIView):
    def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj=DetailsSerializer(detailObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)
    
    def get(self, request, pk):
        detail_obj = get_object_or_404(DetailsModel, pk=pk)
        serializer_obj = DetailsSerializer(detail_obj)
        return Response(serializer_obj.data)
    
# delete
class DetailsDelete(APIView):
    def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        detailObj.delete()
        return Response(200)
    
       
class TaxmasterAdd(APIView):
    def get(self,request):
        detailsObj=CreateTaxModel.objects.all()
        dlSerializeObj=CreateTaxModelSerializer(detailsObj,many=True)
        return Response(dlSerializeObj.data)
    

    def post(self,request):
        serializeobj=CreateTaxModelSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)