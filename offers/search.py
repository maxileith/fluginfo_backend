import traceback
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from amadeus_connector import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from fluginfo.settings import DEBUG, amadeus_connector
from schemas import offer_search_response_schema


class Search(APIView):

    serializer_class = None

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
                        'The 1st of March 2022',
                        summary='The 1st of March 2022',
                        value='2022-03-01',
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
                        'The 3rd of March 2022',
                        summary='The 3rd of November 2022',
                        value='2022-03-03',
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
                        description='Family of 2 adults, 2 children and 1 infant.',
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
                        summary='2 children',
                        description='Family of 2 adults, 2 children and 1 infant.',
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
                        description='Family of 2 adults, 2 children and 1 infant.',
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
                name='max',
                description='maximum number of flight offers to return. If specified, the value should be greater than or equal to 1',
                required=False,
                type=int,
                default=3,
                location=OpenApiParameter.QUERY,
            ),
        ],
        auth=None,
        summary='How do I get from A to B?',
        responses={
            HTTP_200_OK: offer_search_response_schema,
            HTTP_404_NOT_FOUND: OpenApiResponse(description="There are no flights matching the search criteria."),
            HTTP_400_BAD_REQUEST: None,
            HTTP_503_SERVICE_UNAVAILABLE: OpenApiResponse(
                description="The internally used service provider has server problems."),
        },
    )
    def get(self, request):
        """
        This endpoint returns flight connections that match the search criteria
        specified in the GET request. Only superficial information is returned.
        To retrieve details, the id can be used at the corresponding endpoint.
        (see "/offers/seatmaps")
        """
        try:
            offers = amadeus_connector.offer_search.get(
                **{**request.GET.dict(), 'currencyCode': 'EUR'})

            if len(offers) != 0:
                return JsonResponse(
                    data={
                        'data': offers,
                    },
                    status=HTTP_200_OK,
                )
            else:
                return HttpResponse(
                    content='',
                    status=HTTP_404_NOT_FOUND,
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
