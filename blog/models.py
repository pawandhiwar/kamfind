from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.contrib.auth.models import User



class category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title  = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return self.title


    
class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    def __str__(self):
        return self.name


class blog_post(models.Model):
    cat = models.ForeignKey(category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    Tumnails = models.ImageField(upload_to='static/all_images/',blank=True , null=True)
    content1 = HTMLField(blank=True)
    number_of_post = models.CharField(max_length=500, null=True, blank=True)
    salary = models.CharField(max_length=500, null=True, blank=True)
    application_end_date = models.DateField(null=True, blank=True)
    Location = models.CharField(max_length=500, null=True, blank=True)
    date_post = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True)
    recruitment_name = models.CharField(max_length=100, null=True, blank=True)
    department_name = models.CharField(max_length=500, null=True, blank=True)
    post_name = models.CharField(max_length=500, null=True, blank=True)
    Ability = models.CharField(max_length=500, null=True, blank=True)
    age = models.CharField(max_length=500, null=True, blank=True)
    application_process = models.CharField(max_length=500, null=True, blank=True)
    main_website = models.CharField(max_length=500, null=True, blank=True)
    title_important_date = models.CharField(max_length=500, null=True, blank=True)
    date_information = models.CharField(max_length=500, null=True, blank=True)
    application_start_date = models.DateField(null=True, blank=True)
    Admit_Cart_Issuance_Date = models.DateField(null=True, blank=True)
    Exam_Data = models.DateField(null=True, blank=True)
    Interview_date = models.DateField(null=True, blank=True)
    title_fee = models.CharField(max_length=500, null=True, blank=True)
    fee_information = models.TextField(null=True, blank=True)
    General = models.IntegerField(null=True, blank=True)
    Obc = models.IntegerField(null=True, blank=True)
    St_Sc = models.IntegerField(null=True, blank=True)
    title_eligibility = models.CharField(max_length=500, null=True, blank=True)
    qualification_information = models.TextField(max_length=2000, null=True, blank=True)
    required_eligibility = models.CharField(max_length=500, null=True, blank=True)
    age = models.CharField(max_length=500, null=True, blank=True)
    citizenship = models.CharField(max_length=500, null=True, blank=True)
    experience = models.CharField(max_length=500, null=True, blank=True)
    native = models.CharField(max_length=500, null=True, blank=True)
    departmental_ad = models.CharField(max_length=500, null=True, blank=True)
    online_form = models.CharField(max_length=500, null=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return self.title
    

class borad_wish_post(models.Model):
    Exam_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    def __str__(self):
        return self.name

class Sec_post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    Tumnails = models.ImageField(upload_to='static/all_images/', blank=True)
    date_post = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content1 = HTMLField(blank=True)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return self.title
    

class Sarkari_post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    Tumnails = models.ImageField(upload_to='static/all_images/' ,blank=True)
    date_post = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content1 = HTMLField(blank=True)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return self.title
    
class Top_job(models.Model):
    cat = models.ForeignKey(category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    date_post = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    Tumnails = models.ImageField(upload_to='static/all_images/' ,blank=True)
    content1 = HTMLField(blank=True)
    detailed_information_section_i = models.TextField(max_length=2000, null=True, blank=True)
    post_name = models.CharField(max_length=500, null=True, blank=True)
    number_of_post = models.CharField(max_length=500, null=True, blank=True)
    salary = models.CharField(max_length=500, null=True, blank=True)
    application_end_date = models.DateField(null=True, blank=True)
    Location = models.CharField(max_length=500, null=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return self.title
    
class Result(models.Model):
    Exam_name = models.CharField(max_length=100, null=True, blank=True)
    result = models.TextField(null=True, blank=True)
    result_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.result
    
class Breaking_news(models.Model):
    Breaking = models.TextField(null=True, blank=True)
    Breaking_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.Breaking

class Poster(models.Model):
    poster = models.TextField(null=True, blank=True)
    poster_url = models.CharField(max_length=999, null=True, blank=True)
    def __str__(self):
        return self  
    
class SSC(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    ssc = models.TextField(null=True, blank=True)
    ssc_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.ssc
    
class Vyapam(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    vyapam = models.TextField(null=True, blank=True)
    vyapam_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.vyapam
    
class Railway(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    railway = models.TextField(null=True, blank=True)
    railway_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.railway
    
class UPSC(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    upsc = models.TextField(null=True, blank=True)
    upsc_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.upsc
    
class Admitcard(models.Model):
    admitcard = models.TextField(null=True, blank=True)
    Exam_name = models.CharField(max_length=100, null=True, blank=True)
    admitcard_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.admitcard
    
class Anskey(models.Model):
    anskey = models.TextField(null=True, blank=True)
    Exam_name = models.CharField(max_length=100, null=True, blank=True)
    anskey_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.anskey
    
class Syllabus(models.Model):
    syllabus = models.TextField(null=True, blank=True)
    Exam_name = models.CharField(max_length=100, null=True, blank=True)
    syllabus_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.syllabus
    

class Tool_add(models.Model):
    tool_name = models.CharField(max_length=100, null=True, blank=True)
    about_tool = models.TextField(null=True, blank=True)
    tool_url = models.URLField(max_length=999, help_text='Enter a valid URL')
    def __str__(self):
        return self.tool_name
    
class PreviousYear(models.Model):
    previous_year_q_detail = models.TextField(null=True, blank=True)
    
     
    # Define year1 and file1 pair
    year1 = models.CharField(max_length=100 , blank=True)
    file1 = models.FileField(upload_to='Old_Q/')
    
    # Define year2 and file2 pair
    year2 = models.CharField(max_length=100 , blank=True)
    file2 = models.FileField(upload_to='Old_Q/')
    
    # Define year3 and file3 pair
    year3 = models.CharField(max_length=100 , blank=True)
    file3 = models.FileField(upload_to='uploads/')
    
    # Define year4 and file4 pair
    year4 = models.CharField(max_length=100 , blank=True)
    file4 = models.FileField(upload_to='Old_Q/')
    
    # Define year5 and file5 pair
    year5 = models.CharField(max_length=100 , blank=True)
    file5 = models.FileField(upload_to='Old_Q/')
    
   
 
    
class Social_medias(models.Model):
    Whatsapp =models.URLField(max_length=999, help_text='Enter a valid URL')
    Telegram =models.URLField(max_length=999, help_text='Enter a valid URL')
    Instagram =models.URLField(max_length=999, help_text='Enter a valid URL')
    Facebook =models.URLField(max_length=999, help_text='Enter a valid URL')
    Youtube = models.URLField(max_length=999, help_text='Enter a valid URL')
   
class Carousel(models.Model):    
      poster = models.ImageField(upload_to='static/all_images/')
      carousel_url = models.URLField(max_length=999, help_text='Enter a valid URL')



class AdSense(models.Model):
    Vartical_ads = models.CharField(max_length=1000,blank=True)
    Vartical_code = models.TextField(blank=True)
    Horizantal_ads = models.CharField(max_length=1000,blank=True)
    Horizantal_code = models.TextField(blank=True)
  
    # Add more fields as needed
    
