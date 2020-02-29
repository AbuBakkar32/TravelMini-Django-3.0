import pytz
from django.shortcuts import render, redirect
# Create your views here.
from travello.models import City


def index(request):
    city = City.objects.all()
    return render(request, 'index.html', {'city': city})













    """
    dest1 = Destination()
    dest1.name = 'Chittagong'
    dest1.desc = 'The City people work hard'
    dest1.img = 'destination_1.jpg'
    dest1.price = '$620'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Dhaka'
    dest2.desc = 'First Biriyani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = '$720'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Sylhet'
    dest3.desc = 'This is Most Beautiful city'
    dest3.img = 'destination_3.jpg'
    dest3.price = '$520'
    dest3.offer = True

    dest3 = Destination()
    dest3.name = 'Sylhet'
    dest3.desc = 'This is Most Beautiful city'
    dest3.img = 'destination_3.jpg'
    dest3.price = '$520'
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Rangpur'
    dest4.desc = 'Most Fabulous City in Bangladesh'
    dest4.img = 'destination_4.jpg'
    dest4.price = '$350'
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'Rajshahi'
    dest5.desc = 'Most Clean City in Bangladesh'
    dest5.img = 'destination_5.jpg'
    dest5.price = '$450'
    dest5.offer = False

    dest6 = Destination()
    dest6.name = 'Khulna'
    dest6.desc = 'Most Historical City in Bangladesh'
    dest6.img = 'destination_6.jpg'
    dest6.price = '$425'
    dest6.offer = False

    dests = [dest2, dest1, dest3, dest4, dest5, dest6]
    """
