from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from users.models import CustomerUser


from service.jwtToken import generate_jwt_token
from users.serializers.v1.user_auth_serializer import CustomerAuthSerializer


post_swager = swagger_auto_schema(
    operation_description="Получение пользователем JWT токена",
    request_body=CustomerAuthSerializer,
    responses={
        200: openapi.Response("Успешная аутентификация"),
        400: openapi.Response(description="Email or Password not valid"),
    },
    tags=["Аутентификация", "Пользователь"],
)


class CustomerAuthView(APIView):
    permission_classes = [AllowAny]

    @post_swager
    def post(self, request):
        serializer = CustomerAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer: CustomerUser = serializer.validated_data["user"]

        token = generate_jwt_token(user_id=customer.id)

        return Response(token, status=status.HTTP_200_OK)
