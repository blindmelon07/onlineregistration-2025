from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

def home(request):
    return HttpResponse("Welcome to the API! 🎉 Try /api/fetch or /api/register")
# ✅ Fetch member by ID
# ✅ Fetch Member (GET)
@api_view(['GET'])
def fetch_member(request):
    if request.method == "POST":  # Make sure POST is accepted
        member_id = request.POST.get('id')
        try:
            member = Member.objects.get(id=member_id)
            return JsonResponse({
                "id": member.id,
                "name": member.name,
                "is_registered": member.is_registered
            })
        except Member.DoesNotExist:
            return JsonResponse({"error": "Member not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


# ✅ Register Member (POST)

@api_view(['POST'])
def fetch_member(request):
    if request.method == "POST":
        member_id = request.POST.get("id")
        try:
            member = Member.objects.get(id=member_id)
            return JsonResponse({
                "id": member.id,
                "name": member.name,
                "is_registered": member.is_registered,
            })
        except Member.DoesNotExist:
            return JsonResponse({"error": "Member not found"})
    else:
        return JsonResponse({"error": "Invalid request method"})
    
@csrf_exempt
def register_member(request):
    if request.method == "POST":
        try:
            # Parse incoming data
            data = json.loads(request.body)
            member_id = data.get("id")

            # Try to fetch the member
            member = Member.objects.get(id=member_id)

            # Update is_registered to True
            member.is_registered = True
            member.save()

            return JsonResponse({
                "message": "Member registered successfully!",
                "id": member.id,
                "is_registered": member.is_registered
            })

        except Member.DoesNotExist:
            return JsonResponse({"error": "Member not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)