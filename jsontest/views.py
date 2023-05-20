import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def parse_json(request):
    # Sample JSON data
    data = json.loads(request.body)

    # Parse JSON data
    # parsed_data = json.loads(json_data)


    # Return JsonResponse
    return JsonResponse(data)