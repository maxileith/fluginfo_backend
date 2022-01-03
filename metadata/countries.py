from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from django.http.response import HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from fluginfo.settings import BASE_DIR
from os import path


class CountryFlag(APIView):

    serializer_class = None

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='countryCode',
                description='code of the country',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Germany',
                        summary='Germany',
                        value='DE',
                    ),
                    OpenApiExample(
                        'France',
                        summary='France',
                        value='FR',
                    ),
                    OpenApiExample(
                        'United States of America',
                        summary='United States of America',
                        value='US',
                    ),
                    OpenApiExample(
                        'World',
                        summary='World',
                        value='WORLD',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='What ist the flag of the country?',
    )
    @method_decorator(cache_page(86400))
    def get(self, request):
        """
        This endpoint gives the flag associated with the given
        Country-Code as an SVG file. 
        """
        if 'countryCode' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        country_code = request.GET.get('countryCode').lower()

        if country_code == "world":
            with open(path.join(BASE_DIR, "metadata", "globe.svg")) as f:
                return HttpResponse(
                    content=f.readlines(),
                    status=HTTP_200_OK,
                    content_type="image/svg+xml",
                )

            return HttpResponse(
                content='',
                status=HTTP_500_INTERNAL_SERVER_ERROR,
            )

        url = f'https://raw.githubusercontent.com/hampusborgos/country-flags/main/svg/{country_code}.svg'

        try:
            r = requests.get(url, allow_redirects=False)
        except ConnectionError:
            return HttpResponse(
                content='',
                status=HTTP_503_SERVICE_UNAVAILABLE,
            )
        if r.status_code == HTTP_200_OK:
            return HttpResponse(
                content=r.content,
                content_type="image/svg+xml",
                status=HTTP_200_OK,
            )
        elif r.status_code == HTTP_404_NOT_FOUND:
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
        else:
            return HttpResponse(
                content=r.content,
                status=r.status_code,
            )
