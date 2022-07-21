
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api_weight.serializers import PlanSerializer
from ..DAO.PlanDAO import *
from django.utils.datastructures import MultiValueDictKeyError
@api_view(['POST'])
def handleCreatePlan(request,format=None): 
    data = request.data
    UserID=data['UserID']
    CurrentWeight =data['CurrentWeight']
    TargetWeight = data['TargetWeight']
    TargetDate = data['TargetDate']
    res = CreatePlan(UserID,CurrentWeight,TargetWeight,TargetDate)
    return JsonResponse(res, safe=False)
    # serializer = PlanSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # else:
    #     return Response(serializer.errors, status=400)