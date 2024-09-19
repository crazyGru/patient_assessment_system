from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .models import Patient, Assessment
from .serializers import PatientSerializer, AssessmentSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class AssessmentPagination(PageNumberPagination):
    page_size = 10

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    pagination_class = AssessmentPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ['assessment_date', 'assessment_type']
    search_fields = ['assessment_type', 'patient__full_name']