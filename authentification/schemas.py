# schemas.py
from drf_yasg import openapi
from .models import STATUS_CHOICES  # STATUS_CHOICES ni import qiling

def user_schema():
    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            'middle_name': openapi.Schema(type=openapi.TYPE_STRING),
            'telegram': openapi.Schema(type=openapi.TYPE_STRING),
            'birth_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
            'started_work': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
            'supervisor': openapi.Schema(type=openapi.TYPE_STRING),
            'raiting': openapi.Schema(type=openapi.TYPE_NUMBER),
            'block': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            'job': openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=[choice[0] for choice in STATUS_CHOICES],
                description="User's job position"
            ),
        }
    )

register_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user': user_schema(),
        'refresh': openapi.Schema(type=openapi.TYPE_STRING),
        'access': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

login_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING),
        'access': openapi.Schema(type=openapi.TYPE_STRING),
    }
)