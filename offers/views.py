from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from amadeus_connector import Search
from amadeus_connector import NoMatchingHashError

@api_view(['GET'])
def search(request):

    s = Search(
        originLocationCode='BRE',
        destinationLocationCode='STR',
        departureDate='2021-11-01',
        returnDate='2021-11-02',
        adults=2,
        children=1,
        max=3,
        travelClass='BUSINESS',
    )
    offers = s.go()

    return JsonResponse(
        data=offers,
        status=status.HTTP_200_OK if len(offers) else status.HTTP_404_NOT_FOUND
    )
