from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import AmadeusBadRequest, OfferSearch, AvailabilitySearch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample


class Search(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='departureIata',
                description='airport IATA code from which the traveler will depart, e.g. BOS for Boston',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Frankfurt Airport',
                        summary='Frankfurt Airport',
                        value='FRA',
                    ),
                    OpenApiExample(
                        'Heathrow Airport',
                        summary='Heathrow Airport',
                        value='LHR',
                    ),
                    OpenApiExample(
                        'Dallas/Fort Worth International Airport',
                        summary='Dallas/Fort Worth International Airport',
                        value='DFW',
                    ),
                ],
            ),
            OpenApiParameter(
                name='arrivalIata',
                description='airport IATA code to which the traveler is going, e.g. PAR for Paris',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Dallas/Fort Worth International Airport',
                        summary='Dallas/Fort Worth International Airport',
                        value='DFW',
                    ),
                    OpenApiExample(
                        'Frankfurt Airport',
                        summary='Frankfurt Airport',
                        value='FRA',
                    ),
                    OpenApiExample(
                        'Heathrow Airport',
                        summary='Heathrow Airport',
                        value='LHR',
                    ),
                ],
            ),
            OpenApiParameter(
                name='date',
                description='the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the ISO 8601 YYYY-MM-DD format, e.g. 2017-12-25',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'The 1st of November 2021',
                        summary='The 1st of November 2021',
                        value='2021-11-01',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='Which flights are there to go from A to B on a certain day?',
    )
    @method_decorator(cache_page(1800))
    def get(self, request):
        """
        This endpoint returns the availability of flights traveling
        from a certain airport to a certain airport on a specific
        date.
        """
        if 'departureIata' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        if 'arrivalIata' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        if 'date' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        try:
            s = AvailabilitySearch(
                departure_iata=request.GET.get('departureIata'),
                arrival_iata=request.GET.get('arrivalIata'),
                date=request.GET.get('date'),
            )
            availabilities = s.go()

            return JsonResponse(
                data=availabilities,
                status=HTTP_200_OK,
            )
        except AmadeusBadRequest:
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
