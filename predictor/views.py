from django.shortcuts import render


def home(request):

    prediction = None

    if request.method == "POST":

        location = request.POST.get("location")
        bedrooms = int(request.POST.get("bedrooms"))
        bathrooms = int(request.POST.get("bathrooms"))
        size = int(request.POST.get("size"))
        floor = int(request.POST.get("floor"))
        parking = request.POST.get("parking")
        furnished = request.POST.get("furnished")
        balcony = request.POST.get("balcony")
        building_age = int(request.POST.get("building_age"))

        # Temporary test prediction
        prediction = 25000

    return render(
        request,
        "predictor/home.html",
        {
            "prediction": prediction
        }
    )