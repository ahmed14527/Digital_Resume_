from rest_framework import generics
from .models import Skill, UserProfile, ContactProfile, Testimonial, Media, Portfolio, Blog, Certificate
from .serializers import SkillSerializer, UserProfileSerializer, ContactProfileSerializer, TestimonialSerializer, MediaSerializer, PortfolioSerializer, BlogSerializer, CertificateSerializer

class SkillListCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class UserProfileListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ContactProfileListCreate(generics.ListCreateAPIView):
    queryset = ContactProfile.objects.all()
    serializer_class = ContactProfileSerializer

class TestimonialListCreate(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class MediaListCreate(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class PortfolioListCreate(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CertificateListCreate(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer