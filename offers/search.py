from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import AmadeusBadRequest, OfferSearch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample


class Search(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='originLocationCode',
                description='city/airport IATA code from which the traveler will depart, e.g. BOS for Boston',
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
                name='destinationLocationCode',
                description='city/airport IATA code to which the traveler is going, e.g. PAR for Paris',
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
                name='departureDate',
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
            OpenApiParameter(
                name='returnDate',
                description='the date on which the traveler will depart from the destination to return to the origin. If this parameter is not specified, only one-way itineraries are found. If this parameter is specified, only round-trip itineraries are found. Dates are specified in the ISO 8601 YYYY-MM-DD format, e.g. 2018-02-28',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'The 3rd of November 2021',
                        summary='The 3rd of November 2021',
                        value='2021-11-03',
                    ),
                ],
            ),
            OpenApiParameter(
                name='adults',
                description='the number of adult travelers (age 12 or older on date of departure).',
                required=True,
                type=int,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Family',
                        summary='2 adults',
                        description='Family of 2 adults, 2 childs and 1 infant.',
                        value=2,
                    ),
                ],
            ),
            OpenApiParameter(
                name='children',
                description='the number of child travelers (older than age 2 and younger than age 12 on date of departure) who will each have their own separate seat. If specified, this number should be greater than or equal to 0',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Family',
                        summary='2 childs',
                        description='Family of 2 adults, 2 childs and 1 infant.',
                        value=2,
                    ),
                ],
            ),
            OpenApiParameter(
                name='infants',
                description='the number of infant travelers (whose age is less or equal to 2 on date of departure). Infants travel on the lap of an adult traveler, and thus the number of infants must not exceed the number of adults. If specified, this number should be greater than or equal to 0',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Family',
                        summary='1 infant',
                        description='Family of 2 adults, 2 childs and 1 infant.',
                        value=1,
                    ),
                ],
            ),
            OpenApiParameter(
                name='travelClass',
                description='most of the flight time should be spent in a cabin of this quality or higher. The accepted travel class is economy, premium economy, business or first class. If no travel class is specified, the search considers any travel class.',
                required=False,
                type=str,
                enum=['ECONOMY', 'PREMIUM_ECONOMY', 'BUSINESS', 'FIRST'],
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='includedAirlineCodes',
                description='This option ensures that the system will only consider these airlines. This can not be cumulated with parameter excludedAirlineCodes. Airlines are specified as IATA airline codes and are comma-separated, e.g. 6X,7X,8X',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'no whitelisting',
                        summary='no whitelisting',
                        value='',
                    ),
                    OpenApiExample(
                        'TUIFly & Lufthansa',
                        summary='TUIFly & Lufthansa',
                        value='X3,LH',
                    ),
                    OpenApiExample(
                        'Turkish Airlines',
                        summary='Turkish Airlines',
                        value='TK',
                    ),
                ],
            ),
            OpenApiParameter(
                name='excludedAirlineCodes',
                description='This option ensures that the system will ignore these airlines. This can not be cumulated with parameter includedAirlineCodes. Airlines are specified as IATA airline codes and are comma-separated, e.g. 6X,7X,8X',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'no blacklisting',
                        summary='no blacklisting',
                        value='',
                    ),
                    OpenApiExample(
                        'TUIFly & Lufthansa',
                        summary='TUIFly & Lufthansa',
                        value='X3,LH',
                    ),
                    OpenApiExample(
                        'Turkish Airlines',
                        summary='Turkish Airlines',
                        value='TK',
                    ),
                ],
            ),
            OpenApiParameter(
                name='nonStop',
                description='if set to true, the search will find only flights going from the origin to the destination with no stop in between',
                required=False,
                type=bool,
                default=False,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='currencyCode',
                description='the preferred currency for the flight offers. Currency is specified in the ISO 4217 format, e.g. EUR for Euro',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Euro',
                        summary='Euro',
                        value='EUR',
                    ),
                    OpenApiExample(
                        'US-Dollar',
                        summary='US-Dollar',
                        value='USD',
                    ),
                ],
            ),
            OpenApiParameter(
                name='maxPrice',
                description='maximum price per traveler. By default, no limit is applied. If specified, the value should be a positive number with no decimals',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='max',
                description='maximum number of flight offers to return. If specified, the value should be greater than or equal to 1',
                required=False,
                type=int,
                default=3,
                location=OpenApiParameter.QUERY,
            ),
        ],
        auth=None,
        summary='What are the flight offers?',
    )
    @method_decorator(cache_page(1800))
    def get(self, request):
        """
        This endpoint returns flight connections that match the search criteria
        specified in the GET request. Only superficial information is returned.
        To retrieve details, the id can be used at the corresponding endpoint.
        (see "/offers/seatmaps")
        """
        try:
            s = OfferSearch(**request.GET.dict())
            offers = s.go()

            if len(offers):
                return JsonResponse(
                    data=offers,
                    status=HTTP_200_OK,
                )
            else:
                return HttpResponse(
                    content='',
                    status=HTTP_404_NOT_FOUND,
                )
        except AmadeusBadRequest:
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )   
