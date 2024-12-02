
# Digital_Resume_DRF
<p>An Digital_Resume_DRF platform developed in django-3 which allow users to build Digital_Resume :) </p>



(Note: The website can take upto 30 seconds (hosted on Render free tier services), as the project has no clients, its just for learning, please refer the source
code to run locally).

### Short Note

This guide will Step-by-Step help you to create your own online Digital_Resume_DRF website in django Framework. 

Note: this guide is not for absolute beginners so im assuming that you have the basic knowledge of MVT in django to get started. To know more on it i recommend you <a href="https://docs.djangoproject.com/en/3.0/">django documentation</a>.

# Table of contents
- [About_this_App](#About_this_App)
- [Get_Started](#Get_Started)
- [course_app](#main_App)
  * [models](#models)
  * [migrations](#migrations)
  * [admin](#admin)
  * [server](#server)
  * [views](#views)
  * [urls](#urls)
  
<hr>

## About_this_App
The Digital Resume DRF (Digital Resume Data Representation Format) is a standardized format used for representing resume information in a digital form. It aims to provide a structured way to store and exchange resume data, making it easier for systems to parse and analyze resumes.

## Get_Started

I'm assuming that you are already done with setting up virtual enviornment in your system. Ok, now lets move to a location where we can store this project by using terminal or command prompt in windows. In my case im at this location,

yash@yash-SVE15113ENB:~/Documents/django_project/$ 

* Now Setup the virtual environment

$`pipenv shell`

$`pipenv install django==3.0`

## main-app

Lets begin our project by starting our project and installing a books app, type below commands in terminal.

(django_project)$`django-admin startproject resume_app .` (do not avoid this period)

(django_project)$`python manage.py startapp main`

Now, open your favourite IDE and locate this project directory. (Im using VS Code so it should be something like this) note that at this point django doesnt know about this app, therefore we need to mention this app name inside our settings.py file.

* settings.py 

open your ecom_project folder, in here you will find settings.py file (open it). Go to Installed app section and mention your app name there (as shown below).


	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',

	    # my apps,				# changes
	    'main',
	    ]


### models

When done with the settings.py file, open the course folder (our app), in here you we find models.py file (open it)
Now put the following code in it,


	from django.db import models
    from django.contrib.auth.models import User
    from django.template.defaultfilters import slugify
    from ckeditor.fields import RichTextField


    class Skill(models.Model):
        class Meta:
            verbose_name_plural = 'Skills'
            verbose_name = 'Skill'
        
        name = models.CharField(max_length=20, blank=True, null=True)
        score = models.IntegerField(default=80, blank=True, null=True)
        image = models.FileField(blank=True, null=True, upload_to="skills")
        is_key_skill = models.BooleanField(default=False)
        
        def __str__(self):
            return self.name

    class UserProfile(models.Model):

        class Meta:
            verbose_name_plural = 'User Profiles'
            verbose_name = 'User Profile'
        
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
        title = models.CharField(max_length=200, blank=True, null=True)
        bio = models.TextField(blank=True, null=True)
        skills = models.ManyToManyField(Skill, blank=True)
        cv = models.FileField(blank=True, null=True, upload_to="cv")

        def __str__(self):
            return f'{self.user.first_name} {self.user.last_name}'


    class ContactProfile(models.Model):
        
        class Meta:
            verbose_name_plural = 'Contact Profiles'
            verbose_name = 'Contact Profile'
            ordering = ["timestamp"]
        timestamp = models.DateTimeField(auto_now_add=True)
        name = models.CharField(verbose_name="Name",max_length=100)
        email = models.EmailField(verbose_name="Email")
        message = models.TextField(verbose_name="Message")

        def __str__(self):
            return f'{self.name}'



    class Testimonial(models.Model):

        class Meta:
            verbose_name_plural = 'Testimonials'
            verbose_name = 'Testimonial'
            ordering = ["name"]

        thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
        name = models.CharField(max_length=200, blank=True, null=True)
        role = models.CharField(max_length=200, blank=True, null=True)
        quote = models.CharField(max_length=500, blank=True, null=True)
        is_active = models.BooleanField(default=True)

        def __str__(self):
            return self.name


    class Media(models.Model):

        class Meta:
            verbose_name_plural = 'Media Files'
            verbose_name = 'Media'
            ordering = ["name"]
        
        image = models.ImageField(blank=True, null=True, upload_to="media")
        url = models.URLField(blank=True, null=True)
        name = models.CharField(max_length=200, blank=True, null=True)
        is_image = models.BooleanField(default=True)

        def save(self, *args, **kwargs):
            if self.url:
                self.is_image = False
            super(Media, self).save(*args, **kwargs)
        def __str__(self):
            return self.name

    class Portfolio(models.Model):

        class Meta:
            verbose_name_plural = 'Portfolio Profiles'
            verbose_name = 'Portfolio'
            ordering = ["name"]
        date = models.DateTimeField(blank=True, null=True)
        name = models.CharField(max_length=200, blank=True, null=True)
        description = models.CharField(max_length=500, blank=True, null=True)
        body = RichTextField(blank=True, null=True)
        image = models.ImageField(blank=True, null=True, upload_to="portfolio")
        slug = models.SlugField(null=True, blank=True)
        is_active = models.BooleanField(default=True)

        def save(self, *args, **kwargs):
            if not self.id:
                self.slug = slugify(self.name)
            super(Portfolio, self).save(*args, **kwargs)

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return f"/portfolio/{self.slug}"


    class Blog(models.Model):

        class Meta:
            verbose_name_plural = 'Blog Profiles'
            verbose_name = 'Blog'
            ordering = ["timestamp"]

        timestamp = models.DateTimeField(auto_now_add=True)
        author = models.CharField(max_length=200, blank=True, null=True)
        name = models.CharField(max_length=200, blank=True, null=True)
        description = models.CharField(max_length=500, blank=True, null=True)
        body = RichTextField(blank=True, null=True)
        slug = models.SlugField(null=True, blank=True)
        image = models.ImageField(blank=True, null=True, upload_to="blog")
        is_active = models.BooleanField(default=True)

        def save(self, *args, **kwargs):
            if not self.id:
                self.slug = slugify(self.name)
            super(Blog, self).save(*args, **kwargs)

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return f"/blog/{self.slug}"


    class Certificate(models.Model):

        class Meta:
            verbose_name_plural = 'Certificates'
            verbose_name = 'Certificate'

        date = models.DateTimeField(blank=True, null=True)
        name = models.CharField(max_length=50, blank=True, null=True)
        title = models.CharField(max_length=200, blank=True, null=True)
        description = models.CharField(max_length=500, blank=True, null=True)
        is_active = models.BooleanField(default=True)

        def __str__(self):
            return self.name



* what we done here ?

in this models, we have defined the following models:

1. **Skill**:
   - Represents a skill with fields for name, score, image, and a boolean indicating if it's a key skill.

2. **UserProfile**:
   - Represents a user profile linked to a User model with fields for avatar, title, bio, skills (linked to Skill model), and a CV file.
   
3. **ContactProfile**:
   - Represents a contact profile with fields for name, email, message, and a timestamp.
   
4. **Testimonial**:
   - Represents a testimonial with fields for thumbnail image, name, role, quote, and an indicator if it's active.

5. **Media**:
   - Represents media files with fields for image, URL, name, and a boolean to indicate if it's an image.
   
6. **Portfolio**:
   - Represents a portfolio entry with fields for date, name, description, body (RichTextField), image, slug, and an indicator if it's active.

7. **Blog**:
   - Represents a blog post with fields for author, name, description, body (RichTextField), image, slug, and an indicator if it's active.

8. **Certificate**:
   - Represents a certificate with fields for date, name, title, description, and an indicator if it's active.

These models define the structure of your database tables in Django. They establish relationships and store data according to the specified fields. Make sure to run migrations (`python manage.py makemigrations` and `python manage.py migrate`) after defining or modifying models to apply these changes to your database.


## migrations 

now its time to create some tables in our database, most of which is already handled by django, we just need to run following commands:

(django_project)$`python manage.py makemigrations`

(django_project)$`python manage.py migrate`

simply, the migrations command tells us what changes are going to be made in our database (right now two models will be created one is course and other one is category ,video ,usercouse), the migrate command is just like conformation stage of makemigrations command (means if you agree with the changes mentioned by migrations command then in order to perform those changes we run migrate command) 

Note: its a quick illustration of these commands the depth knowledge is available in <a href="https://docs.djangoproject.com/en/3.0/topics/migrations/">django documentation</a>


### admin

now we need to register our models in admin file in order in to use them. Put the following code in admin.py file

	from django.contrib import admin
    from . models import (
        UserProfile,
        ContactProfile,
        Testimonial,
        Media,
        Portfolio,
        Blog,
        Certificate,
        Skill
        )


    @admin.register(UserProfile)
    class UserProfileAdmin(admin.ModelAdmin):
        list_display = ('id', 'user')

    @admin.register(ContactProfile)
    class ContactAdmin(admin.ModelAdmin):
        list_display = ('id', 'timestamp', 'name',)

    @admin.register(Testimonial)
    class TestimonialAdmin(admin.ModelAdmin):
        list_display = ('id','name','is_active')

    @admin.register(Media)
    class MediaAdmin(admin.ModelAdmin):
        list_display = ('id', 'name')

    @admin.register(Portfolio)
    class PortfolioAdmin(admin.ModelAdmin):
        list_display = ('id','name','is_active')
        readonly_fields = ('slug',)

    @admin.register(Blog)
    class BlogAdmin(admin.ModelAdmin):
        list_display = ('id','name','is_active')
        readonly_fields = ('slug',)

    @admin.register(Certificate)
    class CertificateAdmin(admin.ModelAdmin):
        list_display = ('id','name')

    @admin.register(Skill)
    class SkillAdmin(admin.ModelAdmin):
        list_display = ('id','name','score')



Here's a breakdown of what you're doing with each model in the Django admin:

1. **UserProfileAdmin**:
   - Registers the `UserProfile` model with the admin site and specifies that the admin interface should display the `id` and `user` fields for each entry.

2. **ContactAdmin**:
   - Registers the `ContactProfile` model with the admin site and specifies that the admin interface should display the `id`, `timestamp`, and `name` fields for each entry.

3. **TestimonialAdmin**:
   - Registers the `Testimonial` model with the admin site and specifies that the admin interface should display the `id`, `name`, and `is_active` fields for each entry.

4. **MediaAdmin**:
   - Registers the `Media` model with the admin site and specifies that the admin interface should display the `id` and `name` fields for each entry.

5. **PortfolioAdmin**:
   - Registers the `Portfolio` model with the admin site and specifies that the admin interface should display the `id`, `name`, and `is_active` fields for each entry. Additionally, the `slug` field is set as read-only.

6. **BlogAdmin**:
   - Registers the `Blog` model with the admin site and specifies that the admin interface should display the `id`, `name`, and `is_active` fields for each entry. The `slug` field is set as read-only.

7. **CertificateAdmin**:
   - Registers the `Certificate` model with the admin site and specifies that the admin interface should display the `id` and `name` fields for each entry.

8. **SkillAdmin**:
   - Registers the `Skill` model with the admin site and specifies that the admin interface should display the `id`, `name`, and `score` fields for each entry.

By using the `@admin.register(ModelName)` decorator with each model class and customizing the `list_display` attribute, you are defining how the data will be displayed in the Django admin interface for each model. This customization can help administrators efficiently manage and view the data stored in these models.

### server

Now, lets check that our model is being registered properly or not. First lets ensure that our server is running properly. Put the following commmand in terminal:

(django_project)$`python manage.py runserver`

* now open this link in your browser http://127.0.0.1:8000/

You will see a rocket there and a message saying, 'The install worked successfully! Congratulations!'

if yes, we didn't make any mistakes. Good !

* Now go to admin page by using this link http://127.0.0.1:8000/admin/


### views

 we need to work on views. In this case im gonna use 'Class Based Views' which makes our code as much DRY (Don't Repeat Yourself) as possible and faster to implement. Put the follwing code in your views.py file.


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
    




* what we done here ? 
In the provided views, we are creating Django REST framework API views for each of your models. These views are responsible for handling HTTP requests related to listing and creating instances of the respective models. By using Django REST framework's `ListCreateAPIView`, you are able to easily create endpoints that support both listing existing instances and creating new instances of the models.

Here's a breakdown of what you're doing in each view:

1. **SkillListCreate**:
   - Handles GET (list) and POST (create) requests for the `Skill` model.

2. **UserProfileListCreate**:
   - Handles GET (list) and POST (create) requests for the `UserProfile` model.

3. **ContactProfileListCreate**:
   - Handles GET (list) and POST (create) requests for the `ContactProfile` model.

4. **TestimonialListCreate**:
   - Handles GET (list) and POST (create) requests for the `Testimonial` model.

5. **MediaListCreate**:
   - Handles GET (list) and POST (create) requests for the `Media` model.

6. **PortfolioListCreate**:
   - Handles GET (list) and POST (create) requests for the `Portfolio` model.

7. **BlogListCreate**:
   - Handles GET (list) and POST (create) requests for the `Blog` model.

8. **CertificateListCreate**:
   - Handles GET (list) and POST (create) requests for the `Certificate` model.

For each view, you are specifying the queryset to retrieve all instances of the respective model and the serializer class to serialize the model instances into JSON format for API responses.

These views allow you to interact with your Django models through RESTful APIs, providing endpoints to list existing instances and create new instances for each model. This setup is useful for building APIs that can be consumed by frontend frameworks, mobile applications, or other services.



### urls

Now to make our class based views work we need url routing. By default we have a single urls.py file in our fciplatform directory and not in course app. So lets create a urls.py file in our app (why so ? so that django can easily find which url is working for which app, therfore instead of putting all urls in a single file its better to create seperate urls.py file for each app). Inside your course app create a new urls.py file. (you can do it by using your IDE or by following below code)

for linux users

$touch course/urls.py


Before putting some code in this file go to fciplatform folder and open urls.py file. Update this file in the follwing manner

	from django.contrib import admin
	from django.urls import path, include # changes

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include('main.urls')),  # changes
	]

In short, here im telling django that im using a seperate urls.py file for my main app. Now go back to our app level url.py file (or open the urls.py file of our course app). Put the following code there

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




* what we done here ? 


 we are defining the URL patterns for the Django app with the name `'main'`. These URL patterns map specific URLs to the corresponding views that you have created for handling requests related to your models using Django REST framework.

Here's a breakdown of what you are doing in this URL configuration:

1. **Import Statements**:
   - You are importing the necessary view classes (`SkillListCreate`, `UserProfileListCreate`, `ContactProfileListCreate`, `TestimonialListCreate`, `MediaListCreate`, `PortfolioListCreate`, `BlogListCreate`, `CertificateListCreate`) from your views file.

2. **URL Patterns**:
   - You are defining URL patterns using `path()` for different endpoints related to your models:
     - `/api/skills/`: Maps to `SkillListCreate` view for handling skill-related requests.
     - `/api/userprofiles/`: Maps to `UserProfileListCreate` view for managing user profile instances.
     - `/api/contactprofiles/`: Maps to `ContactProfileListCreate` view for contact profile operations.
     - `/api/testimonials/`: Maps to `TestimonialListCreate` view for testimonial interactions.
     - `/api/media/`: Maps to `MediaListCreate` view for media-related actions.
     - `/api/portfolios/`: Maps to `PortfolioListCreate` view for portfolio operations.
     - `/api/blogs/`: Maps to `BlogListCreate` view for handling blog-related requests.
     - `/api/certificates/`: Maps to `CertificateListCreate` view for certificate management.

3. **Naming URLs**:
   - Each URL pattern is assigned a unique name using the `name` parameter. This name can be used to reference the URL in Django templates or code, providing a way to create dynamic links.

By setting up these URL patterns, you are establishing the structure of your API endpoints, which will allow clients to interact with your Django app's functionality related to skills, user profiles, contact profiles, testimonials, media, portfolios, blogs, and certificates through API requests.



Every time we create a new application, we follow the same steps and add the application within the project settings and upload it to our server.

