from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
from fluginfo.settings import AIRHEX_KEY
from hashlib import md5
from fluginfo.settings import CACHE_TIMEOUT


class AirlineLogo(APIView):

    serializer_class = None

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='iata',
                description='iata of the airline',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'TUIFly',
                        summary='TUIFly',
                        value='X3',
                    ),
                    OpenApiExample(
                        'Lufthansa',
                        summary='Lufthansa',
                        value='LH',
                    ),
                ],
            ),
            OpenApiParameter(
                name='filetype',
                description='This specifies the fileformat.',
                required=True,
                type=str,
                default='png',
                location=OpenApiParameter.QUERY,
                enum=['png', 'svg'],
            ),
            OpenApiParameter(
                name='shape',
                description='This specifies the shape of the logo. (rectangular - 3.5:1)',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                default='square',
                enum=['rectangular', 'square', 'tail']
            ),
            OpenApiParameter(
                name='width',
                description='This specifies the width of the logo. Ignored for SVGs.',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
                default=200,
            ),
            OpenApiParameter(
                name='height',
                description='This specifies the height of the logo. Ignored for SVGs.',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
                default=200,
            ),
            OpenApiParameter(
                name='background',
                description='This specifies the background color (hexcolor). Ignored for SVGs.',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                default='',
                examples=[
                    OpenApiExample(
                        'transparent',
                        summary='transparent',
                        value='',
                    ),
                    OpenApiExample(
                        'polar night',
                        summary='polar night',
                        value='434C5E',
                        description='Based on the awesome nord color palette.',
                    ),
                    OpenApiExample(
                        'snow storm',
                        summary='snow storm',
                        value='E5E9F0',
                        description='Based on the awesome nord color palette.',
                    ),
                    OpenApiExample(
                        'frost',
                        summary='frost',
                        value='81A1C1',
                        description='Based on the awesome nord color palette.',
                    ),
                    OpenApiExample(
                        'aurora red',
                        summary='aurora red',
                        value='BF616A',
                        description='Based on the awesome nord color palette.',
                    ),
                    OpenApiExample(
                        'aurora orange',
                        summary='aurora orange',
                        value='D08770',
                        description='Based on the awesome nord color palette.',
                    ),
                    OpenApiExample(
                        'aurora yellow',
                        summary='aurora yellow',
                        value='EBCB8B',
                        description='Based on the awesome nord color palette.',
                    ),
                    OpenApiExample(
                        'aurora green',
                        summary='aurora green',
                        value='A3BE8C',
                        description='Based on the awesome nord color palette.',
                    ),
                    OpenApiExample(
                        'aurora purple',
                        summary='aurora purple',
                        value='B48EAD',
                        description='Based on the awesome nord color palette.',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='What ist the logo of a certain airline?',
    )
    @method_decorator(cache_page(CACHE_TIMEOUT))
    def get(self, request):
        """
        This endpoint gives the logo of the airline associated with
        the given IATA-Code as a PNG file. 
        """
        if 'iata' not in request.GET.dict().keys() or \
            'shape' not in request.GET.dict().keys() or \
            'filetype' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        if request.GET.get('filetype') not in ['png', 'svg']:
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        if request.GET.get('shape') == 'rectangular':
            shape = 'r'
        elif request.GET.get('shape') == 'square':
            shape = 's'
        elif request.GET.get('shape') == 'tail':
            shape = 't'
        else:
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        if 'background' in request.GET.dict().keys():
            background = request.GET.get('background')
        else:
            background = ''

        iata_code = request.GET.get('iata').upper()

        # usage of the API according to the documentation
        # https://airhex.com/api/logos/
        
        # png
        if request.GET.get('filetype') == 'png':
            height = request.GET.get('height') if 'height' in request.GET.dict().keys() else 200
            width = request.GET.get('width') if 'width' in request.GET.dict().keys() else 200
            logo_id = f'{iata_code}_{width}_{height}_{shape}_{AIRHEX_KEY}'
            logo_md5 = md5(logo_id.encode('utf-8')).hexdigest()
            url = f'https://content.airhex.com/content/logos/airlines_{iata_code}_{width}_{height}_{shape}.png?proportions=keep&md5apikey={logo_md5}&background={background}'
        
        # svg
        else:
            logo_id = f'{iata_code}_{shape}_{AIRHEX_KEY}'
            logo_md5 = md5(logo_id.encode('utf-8')).hexdigest()
            url = f'https://content.airhex.com/content/logos/airlines_{iata_code}_{shape}.svg?md5apikey={logo_md5}'

        r = requests.get(url, allow_redirects=False)
        if r.status_code == 200:
            return HttpResponse(
                content=r.content,
                content_type=r.headers['content-type'],
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
