from django.shortcuts import render, redirect
from .models import blog_post, category , Top_job ,State ,Sec_post , Result ,Admitcard ,Syllabus ,Anskey , Social_medias , Carousel , Breaking_news 
from django.db.models import Q 
from .models import *


def home(request):
    categories = category.objects.all()
    data = blog_post.objects.all()[::-1]
    breaking = Breaking_news.objects.all()
    social = Social_medias.objects.all()
    recent_data = blog_post.objects.all()
    topjob = Top_job.objects.all()
    state = State.objects.all()
    carousel = Carousel.objects.all()
    ads = AdSense.objects.all()
 

    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
         data = blog_post.objects.filter(
            Q(title__icontains=search_query) |
            Q(content1__icontains=search_query)
            
        )
         
         

         
   
         
    if request.method == "GET":
        search_query = request.GET.get('Location')
        search_query = request.GET.get('job_type')
       
        if search_query:
         data = blog_post.objects.filter(
            
           
            Q(Location__icontains=search_query) |
            Q(Type__icontains=search_query) 
            
        )
         if not data:  # If no posts are found
            message = " No0 posts found"

    
    cate_filter = request.GET.get('categories')    
    if cate_filter is not None:
        cat_filter = blog_post.objects.filter(cat=cate_filter)
        context = {'data':data,'cat_filter':cat_filter ,'categories': categories , 'ads':ads ,'state':state ,'social':social }
        return render(request,'blog/categories.html', context)
    
    
    sta_filter = request.GET.get('state')    
    if sta_filter is not None:
        state_filter = blog_post.objects.filter(state=sta_filter)
        context = {'data':data,'state_filter':state_filter ,'state':state , 'ads':ads, 'social':social}
        return render(request,'blog/state.html', context)


    context = {'categories': categories, 'data': data,'state':state , 'recent_data': recent_data, 'ads':ads , 'topjob':topjob  , 'social':social, 'carousel':carousel, 'breaking':breaking}
    return render(request, 'blog/index.html', context)

def base(request):
    social = Social_medias.objects.all()
    categories = category.objects.all()
    data = blog_post.objects.all()
    context = {'social': social,'categories':categories,'data':data}
    return render(request, 'base.html',context)

def AllPost(request):
    data = blog_post.objects.all()
    ads = AdSense.objects.all()
    categories = category.objects.all()
    social = Social_medias.objects.all()
    recent_data = blog_post.objects.all()
    state = State.objects.all()
    carousel = Carousel.objects.all()
    ads = AdSense.objects.all()
    context = { 'data': data,'ads':ads ,'categories':categories,'social':social,'carousel':carousel,'recent_data':recent_data, 'state':state}
    return render(request, 'blog/All_post.html', context)

def category_page(request):
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = { 'ads':ads ,'social':social ,'data':data}
    return render(request, 'blog/categories.html',context)

def age_cal(request):
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = { 'ads':ads ,'social':social ,'data':data}
    return render(request, 'blog/age_cal.html',context)

def image_compress(request):
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = { 'ads':ads ,'social':social ,'data':data}
   
    return render(request, 'blog/image_compress.html', context)
    
def anskey(request):
    anskey = Anskey.objects.all()
    data = blog_post.objects.all()
    ads = AdSense.objects.all()
    social = Social_medias.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
         anskey = Anskey.objects.filter(
           
            Q(Exam_name__icontains=search_query) |
            Q(anskey__icontains=search_query)
            
            
        )
    context = { 'anskey': anskey , 'ads':ads ,'data':data ,'social':social}
    return render(request, 'blog/anskey.html',context)

def about(request):
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    return render(request, 'blog/about.html' ,{'social':social ,'data':data})

def contact(request):
    data = blog_post.objects.all()
    ads = AdSense.objects.all()
    social = Social_medias.objects.all()
    context = {'ads':ads ,'social':social ,'data':data}
    return render(request, 'blog/Contact.html', context)

def privacy_policy(request):
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    return render(request, 'blog/privacy_policy.html',{'social':social ,'data':data})

def disclaimer(request):
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    return render(request, 'blog/Disclaimer.html', {'social':social ,'data':data})

def sitemap(request):
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    return render(request, 'blog/Sitemap.html',{'social':social ,'data':data})

def tool(request):
    data = blog_post.objects.all()
    tools = Tool_add.objects.all()
    social = Social_medias.objects.all()
    ads = AdSense.objects.all()
    context = {'social':social,'tools':tools ,'ads':ads ,'social':social ,'data':data}
    return render(request, 'blog/Tools.html',context)

def syllabus(request):
    data = blog_post.objects.all()
    syllabus = Syllabus.objects.all()
    social = Social_medias.objects.all()
    ads = AdSense.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
         syllabus = Syllabus.objects.filter(
           
            Q(syllabus__icontains=search_query) |
            Q(Exam_name__icontains=search_query)
            
            
        )
    context = {'syllabus':syllabus, 'ads':ads ,'social':social ,'data':data}
    return render(request, 'blog/Syllabus.html',context)

def old_pepar(request):
    data = blog_post.objects.all()
    Old_pepar = PreviousYear.objects.all()
    social = Social_medias.objects.all()
    ads = AdSense.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
         Old_pepar = PreviousYear.objects.filter(
           
            Q(previous_year_q_detail__icontains=search_query)
            
            
        )
    context = {'Old_pepar':Old_pepar, 'ads':ads ,'social':social ,'data':data}
    return render(request, 'blog/previous.html',context)

def result(request):
    results = Result.objects.all()
    social = Social_medias.objects.all()
    data = blog_post.objects.all()
    ads = AdSense.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
         results = Result.objects.filter(
           
            Q(Exam_name__icontains=search_query) |
            Q(result__icontains=search_query)
            
            
        )
    context = {'results':results, 'ads':ads ,'social':social ,'data':data}
    return render(request, 'blog/result.html',context)

def sarkari_yojna(request):
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = {'ads':ads ,'social':social,'data':data }
    
    return render(request, 'sarkari_yojna.html' ,context)

def admit_card(request):
    admit = Admitcard.objects.all()
    social = Social_medias.objects.all()
    data = blog_post.objects.all()
    ads = AdSense.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
         admit = Admitcard.objects.filter(
            Q(admitcard__icontains=search_query) |
            Q(Exam_name__icontains=search_query)
            
            
        )
         
    context = {'admit':admit , 'ads':ads ,'data':data,'social':social}
    return render(request, 'blog/Admit-card.html', context)


def new_post(request, slug):
    meta = blog_post.objects.filter(slug=slug).all()
    categories = category.objects.all()
    social = Social_medias.objects.all()
    Sub_data = blog_post.objects.all()
    data = blog_post.objects.all()
    state = State.objects.all()
    ads = AdSense.objects.all()
    carousel = Carousel.objects.all()
    recent_data = blog_post.objects.all()[::-1]
    context = {'categories': categories, 'meta': meta , 'carousel':carousel,'social':social, 'Sub_data':Sub_data , 'recent_data': recent_data ,'data':data , 'state':state, 'ads':ads }
    return render(request, 'blog/Post-Page.html', context)

def top_post(request, pk):
    top_meta  = Top_job.objects.get(pk=pk)
    borad = Sec_post.objects.all()
    carousel = Carousel.objects.all()
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = { 'top_meta': top_meta , 'borad':borad ,  'carousel':carousel , 'carousel':carousel,'data':data, 'social':social ,'ads':ads}
    return render(request, 'blog/Top-post-page.html', context)


def S_post(request):

    borad = Sec_post.objects.all()
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
          borad = Sec_post.objects.filter(

            Q(title__icontains=search_query)
            
            
        )
    context = {  'borad':borad ,'ads':ads ,'data':data,'social':social}
    return render(request, 'blog/S_post.html', context)

def Secpost(request, slug):
    sec_meta  = Sec_post.objects.filter(slug=slug).all()
    borad = Sec_post.objects.all()
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    carousel = Carousel.objects.all()
    social = Social_medias.objects.all()
    context = { 'sec_meta':sec_meta,'borad':borad,'ads':ads ,'data':data, 'carousel':carousel,'social':social}
    return render(request, 'blog/Sec_post.html', context)

def Sarkari(request):

    sarkari = Sarkari_post.objects.all()
    social = Social_medias.objects.all()
    data = blog_post.objects.all()
    ads = AdSense.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('searchbar')
        
        if search_query:
          sarkari = Sarkari_post.objects.filter(
           
            
            Q(title__icontains=search_query)
            
            
        )
    context = {  'sarkari':sarkari ,'ads':ads ,'data':data ,'social':social }
    return render(request, 'blog/sarkari.html', context)

def Sarkaripost(request, slug):
    sarkari_meta  = Sarkari_post.objects.filter(slug=slug).all()
    borad = Sec_post.objects.all()
    carousel = Carousel.objects.all()
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    sarkari = Sarkari_post.objects.all()
    context = { 'sarkari_meta':sarkari_meta , 'borad':borad, 'carousel':carousel ,'data':data,'sarkari':sarkari ,'ads':ads ,'social':social }
    return render(request, 'blog/sarkari_post.html', context)

def vyapam(request):
    vyapam = Vyapam.objects.all()
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = {  'vyapam':vyapam , 'ads':ads  ,'social':social ,'data':data}
    return render(request, 'blog/vyapam.html',context)

def railway(request):
     railway = Railway.objects.all()
     data = blog_post.objects.all()   
     ads = AdSense.objects.all()
     social = Social_medias.objects.all()
     context = {  'railway':railway , 'ads':ads ,'social':social ,'data':data}
     return render(request, 'blog/railway.html',context)

def upsc(request):
    upsc = UPSC.objects.all()
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = {  'upsc':upsc , 'ads':ads ,'social':social,'data':data}
    return render(request, 'blog/upsc.html',context)

def Ssc(request):
    ssc = SSC.objects.all()
    ads = AdSense.objects.all()
    data = blog_post.objects.all()
    social = Social_medias.objects.all()
    context = {  'ssc':ssc,'ads':ads ,'social':social,'data':data}
    return render(request, 'blog/ssc.html',context)
    
def Robot(request):
   
    return render(request, 'blog/robots.txt')