import traceback
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from fluginfo.settings import DEBUG, amadeus_connector
from amadeus_connector import AmadeusBadRequest, AmadeusServerError, AmadeusNothingFound


class Search(APIView):

    serializer_class = None

    @extend_schema(
        deprecated=True,
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
                        'The 1st of March 2022',
                        summary='The 1st of March 2022',
                        value='2022-03-01',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='How many seats are available on flights going from A to B on a certain day?',
    )
    def get(self, request):
        """
        This endpoint returns the number of seats that are available
        on flights going from A to B on a certain day. The number of
        seats is categorized by class.
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
            availabilities = amadeus_connector.status_search.get(
                departure_iata=request.GET.get('departureIata'),
                arrival_iata=request.GET.get('arrivalIata'),
                date=request.GET.get('date'),
            )

            return JsonResponse(
                data={
                    'data': availabilities
                },
                status=HTTP_200_OK,
            )
        except AmadeusBadRequest:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        except AmadeusNothingFound:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
        except AmadeusServerError:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_503_SERVICE_UNAVAILABLE,
            )
