app_name = 'main'
from django.urls import path
from .views import SkillListCreate, UserProfileListCreate,ContactProfileListCreate, TestimonialListCreate, MediaListCreate, PortfolioListCreate, BlogListCreate, CertificateListCreate
urlpatterns = [
    path('api/skills/', SkillListCreate.as_view(), name='skill_list_create'),
    path('api/userprofiles/', UserProfileListCreate.as_view(), name='userprofile_list_create'),
    path('api/contactprofiles/', ContactProfileListCreate.as_view(), name='contactprofile_list_create'),
    path('api/testimonials/', TestimonialListCreate.as_view(), name='testimonial_list_create'),
    path('api/media/', MediaListCreate.as_view(), name='media_list_create'),
    path('api/portfolios/', PortfolioListCreate.as_view(), name='portfolio_list_create'),
    path('api/blogs/', BlogListCreate.as_view(), name='blog_list_create'),
    path('api/certificates/', CertificateListCreate.as_view(), name='certificate_list_create'),
]