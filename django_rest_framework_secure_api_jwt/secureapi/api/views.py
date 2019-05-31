from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class AuthenticatedView(APIView):

    permission_classes = ( IsAuthenticated, )

    def get(self, request):

        user_id = request.user.id
        username = request.user.username
        is_staff = request.user.is_staff
        is_admin = request.user.is_superuser

        content = {'user_id':user_id, 'username':username, 'is_staff':is_staff, 'is_admin':is_admin}
        return Response(content)

class AdminView(APIView):

    permission_classes = ( IsAdminUser, )

    def get(self, request):

        user_id = request.user.id
        username = request.user.username
        is_staff = request.user.is_staff
        is_admin = request.user.is_superuser

        content = {'user_id':user_id, 'username':username, 'is_staff':is_staff, 'is_admin':is_admin}
        return Response(content)