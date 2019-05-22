from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST', ])
def scan_products(request):
    try:
        image = request.data.get('image', None)
        print(image)

        return Response({'has_error': 'false'}, status=status.HTTP_200_OK)

    except:
        return Response({'has_error': 'true'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
