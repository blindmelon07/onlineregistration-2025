from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Member
from datetime import datetime

def home(request):
    result = None
    not_found = False

    if request.method == "POST":
        # ✅ Handle Search button
        if "fetch_btn" in request.POST:
            client_id = request.POST.get('get_id')
            try:
                result = Member.objects.get(id=client_id)
            except Member.DoesNotExist:
                not_found = True

        # ✅ Handle Register button
        elif "register_btn" in request.POST:
            client_id = request.POST.get('id')

            try:
                member = Member.objects.get(id=client_id)
                if not member.is_registered:
                    member.is_registered = True
                    member.save()
                    messages.success(request, "You have successfully registered!")
                    return redirect('success')
                else:
                    messages.warning(request, "You are already registered.")
            except Member.DoesNotExist:
                not_found = True

    return render(request, 'pages/home.html', {'result': result, 'not_found': not_found})

def success(request):
    return render(request, 'pages/success.html')