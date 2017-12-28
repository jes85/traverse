from django.shortcuts import render
from django.http import HttpResponse
from activitysearch.models import Activity, Location, Trip


def index(request):
    min_popularity = request.GET.get('min_rating', 0)
    max_cost = request.GET.get('max_cost', 1000)
    max_distance = request.GET.get('max_distance', 1000)
    order_by = request.GET.get('order_by', 'rating')

    trips = filter_trips(min_popularity, max_cost, max_distance, order_by)[:6]
    context = {'trips': trips}
    return render(request, 'activitysearch/homepage.html', context)

def detail(request):
    context = {}
    return render(request, 'activitysearch/detail.html', context)

def filter_trips(min_popularity, max_cost, max_distance, order_by):
    return Trip.objects.filter(rating__gte=min_popularity, cost__lte=max_cost, distance__lte=max_distance).order_by(order_by)

# #todo implement function (maybe in a Manager)
# def distance(loc1, loc2):
#     return 0
#
# def closest_trip(request):
#     # current_location =
#     # trips = Trip.objects.all()
#     # closest_trip = Trip.objects.get(pk=1)
#     # for trip in trips:
#     #     trip_distance = distance(current_location, trip.location)
#     #     if trip_distance < closest_trip_distance:
#     #         closest_trip = trip
#     #         closest_trip_distance = distance
#
#     #todo pass closest trip to httpresponse
#     return HttpResponse("Closest trip: ")
#
# def cheapest_trips(request):
#     trips = Trip.objects.order_by('cost')[:5]
#     cheapest_trip = Trip.objects.get(pk=1)
#     for trip in trips:
#         if trip.cost < cheapest_trip.cost:
#             cheapest_trip = trip
#     #todo pass cheapest trip to httpresponse
#     return HttpResponse("Cheapest trip: ")
#
# def most_popular_trip(request):
#     trips = Trip.objects.all()
#     most_popular_trip = Trip.objects.get(pk=1)
#     for trip in trips:
#         if trip.rating > most_popular_trip:
#             most_popular_trip = trip
#     #todo pass most popular trip to httpresponse
#     return HttpResponse("Most popular trip: ")
#
# #todo create simple heuristic based on location, cost, popularity
# def recommended_trip(request):
#     return HttpResponse("recommended trip: ")
