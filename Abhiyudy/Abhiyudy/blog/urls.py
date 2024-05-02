
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .import views


urlpatterns = [
   path('',views.home,name="home"),
   path('old_pepar/', views.old_pepar, name='old_pepar'),
   path('Spost/', views.S_post, name='S_post'),
   path('Ssc/', views.Ssc, name='Ssc'),
   path('railway/', views.railway, name='railway'),
   path('upsc/', views.upsc, name='upsc'),
   path('vyapam/', views.vyapam, name='vyapam'),
   path('Sarkari/', views.Sarkari, name='Sarkari'),
   path('base/', views.base, name='base'),
   path('c',views.category_page,name="category_page"),
   path('about/', views.about, name='about'),
   path('anskey/', views.anskey, name='anskey'),
   path('tools/', views.tool, name='tools'),
   path('age_cal/', views.age_cal, name='age_cal'),
   path('image_compress/', views.image_compress, name='image_compress'),
   path('contact/', views.contact, name='contact'),
   path('privacy/', views.privacy_policy, name='privacy'),
   path('disclaimer/', views.disclaimer, name='disclaimer'),
   path('sitemap/', views.sitemap, name='sitemap'),
   path('categories/', views.category_page, name='categories'),
   path('result/', views.result, name='result'),
   path('sarkari-yojna/', views.sarkari_yojna, name='sarkari_yojna'),
   path('all-post/', views.AllPost, name='all_post'),
   path('syllabus/', views.syllabus, name='syllabus'),
   path('a', views.admit_card, name='admit_card'),
   path('<int:pk>/', views.top_post, name='top_post'),
   path('sarkari/<slug:slug>/', views.Sarkaripost, name='sarkari_detail'),
   path('secpost/<slug:slug>/', views.Secpost, name='secpost_detail'),
   path('<str:slug>/', views.new_post, name='new_post'),
  
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


