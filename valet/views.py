import uuid
from django.shortcuts import render, redirect
from .forms import VehicleForm
from .models import Vehicle


def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by("-created_at")
    return render(request, "valet/vehicle_list.html", {"vehicles": vehicles})


def vehicle_create(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            Vehicle.objects.create(
                username="operador1",
                brand_model=form.cleaned_data["brand_model"],
                key_code=form.cleaned_data["key_code"],
                ticket_number=f"T-{uuid.uuid4().hex[:6].upper()}",
                responsible=form.cleaned_data["responsible"],
                license_plate=form.cleaned_data["license_plate"],
                status="En Custodia",
                parking_spot=form.cleaned_data["parking_spot"],
            )
            return redirect("valet:vehicle_list")
    else:
        form = VehicleForm()
    return render(request, "valet/vehicle_form.html", {"form": form})