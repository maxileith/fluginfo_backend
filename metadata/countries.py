from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class CountryFlag(APIView):

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
                ],
            ),
        ],
        auth=None,
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
        url = f'https://raw.githubusercontent.com/hampusborgos/country-flags/main/svg/{country_code}.svg'

        r = requests.get(url, allow_redirects=False)
        if r.status_code == 200:
            return HttpResponse(
                content=r.content,
                content_type="image/svg+xml",
                status=HTTP_200_OK,
            )
        elif r.status_code == 404:
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
        else:
            return HttpResponse(
                content=r.content,
                status=r.status_code,
            )
