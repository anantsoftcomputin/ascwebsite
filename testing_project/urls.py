"""testing_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testing_app import views
from testing_app.views import index,HttpResponseRedirect
from django.conf import settings
from testing_app.views import form,HttpResponseRedirect
from django.conf.urls.static import static
#from testing_app.views import send_email
from django.conf.urls import handler404
admin.site.site_header = "ASC Admin"
admin.site.site_title = "ASC Admin Portal"
admin.site.index_title = "Welcome to ASC Portal"




urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('our-team/', views.ourteam, name='our-team'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('career/', views.career, name='career'),
    path('apply-now-form/', views.applynowform, name='apply-now-form'),
    path('client-testimonial/', views.clienttestimonial, name='client-testimonial'),
    path('life-at-asc/', views.lifeatasc, name='life-at-asc'),
    path('photo-gallery/', views.photogallery, name='photo-gallery'),
    path('faq/', views.faq, name='faq'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('success/',views.success,name='success'),
    path('mobile-app-development/',views.mobileapp,name='mobileappdevelopment'),
    path('web-app-development/',views.web,name='web'),
    path('static-website-development/',views.staticwebsite,name='staticwebsite'),
    path('website-with-cms/',views.cmsoption,name='cmsoption'),
    path('frontend-development/',views.frontendoption,name='frontendoption'),
    path('ecommerce-development/',views.ecommerceoption,name='ecommerce'),
    path('budget/',views.budget,name='budget'),
    path('form/',views.form,name='form'),
    path('server-management/',views.servermanagement,name='server-management'),
    path('software-development/',views.software,name='software-development'),
    path('search-engine-optimization/',views.seo,name='search-engine-optimization'),
    path('machine-learning-ai/',views.machinelearning,name='machine-learning-ai'),
    path('digital-marketing/',views.digitalmarketing,name='digital-marketing'),
    path('graphics-design/',views.design,name='graphics-design'),
   
    path('admin/', admin.site.urls),
    path('user/', admin.site.urls),
    path('contact/',admin.site.urls),
    path('job/',admin.site.urls),
    path('thank/', views.thankyou,name='thankyou'),
    path('summary/', views.summary,name='summary'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('<int:id>/',views.update_data,name='updatedata'),
    #path('send/',sendanemail,name="email"),
    path('user_welcome_template/',views.user_welcome_template,name='user_welcome_template'),
    path('admin_thank_template/',views.admin_thank_template,name='admin_thank_template'),
   
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



handler404 = "testing_app.views.page_not_found_view"
	




