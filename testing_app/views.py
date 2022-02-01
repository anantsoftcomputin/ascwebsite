from django.forms.forms import Form
from django.shortcuts import render,HttpResponseRedirect
from testing_app.forms import NewUserForm,ContactForm,ApplyNowForm
from django.shortcuts import render
from django.contrib import messages
from .models import  User,Contact,Job
import os
import requests
import json
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.core import mail
from django.template.loader import render_to_string,get_template
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage

  

from django.shortcuts import render
def page_not_found_view(request, exception):
    return render(request, '404.html')





def index(request):
   if request.method=="POST":
          ind=User()
         
          if(request.POST.get('branch_1_group_1')=='Mobile-App-Development'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/mobile-app-development/')
          elif(request.POST.get('branch_1_group_1')=='Web-Development'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/web-app-development/')
          elif(request.POST.get('branch_1_group_1')=='Seo-Optimization'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/search-engine-optimization/')
          elif(request.POST.get('branch_1_group_1')=='Design'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/graphics-design/')
          elif(request.POST.get('branch_1_group_1')=='Software-Product-Development'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/software-development/')
          elif(request.POST.get('branch_1_group_1')=='Machine-Learning'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/machine-learning-ai/')
          elif(request.POST.get('branch_1_group_1')=='Server-Management'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/server-management/')
          elif(request.POST.get('branch_1_group_1')=='digital-marketing'):
             request.session['branch_1_group_1'] = request.POST.get('branch_1_group_1')
             return HttpResponseRedirect('/digital-marketing/')
   else:
            return render(request,'index.html')


      
    
   
  
   
   
def update_data(request,id):
       if request.method=='POST':
            pi = User.objects.get(pk=id)
            fm=NewUserForm(request.POST,instance=pi)
            if fm.is_valid():
             fm.save()
       else:
          pi = User.objects.get(pk=id)
          fm=NewUserForm(instance=pi)
       return render(request,'updatestudent.html',{'form':fm})

 #this function delete data 
def delete_data(request, id):
      if request.method == 'POST':
          pi = User.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/')

    



    
def about(request):
    return render(request, 'about.html')

def ourteam(request):
    return render(request, 'ourteam.html')

def portfolio(request):
    return render(request, 'portfolio.html')
    
def career(request):
    return render(request, 'career.html')
    
def clienttestimonial(request):
    return render(request, 'clienttestimonial.html')

def lifeatasc(request):
    return render(request, 'lifeatasc.html')

def photogallery(request):
    return render(request, 'photogallery.html')

def faq(request):
    return render(request, 'faq.html')

def applynowform(request):
    if request.method=="POST":
      if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('user_email') and request.POST.get('user_mobile')and request.POST.get('apply_for') and request.POST.get('experiance'):
        app=Job()
   
        app.first_name=request.POST.get('first_name')
        app.last_name=request.POST.get('last_name')
        app.email_add=request.POST.get('user_email')
        app.Mobile=request.POST.get('user_mobile')
        app.Experience=request.POST.get('experiance')
        app.Apply_for=request.POST.get('apply_for')
        
        captcha_token=request.POST.get('g-recaptcha-response')
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LdoMTceAAAAAJJ15_F_P-L2gS0JSMjxZuAh5cVs" 
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)
        if cap_json['success']==False:
            messages.error(request,"Invalid captcha try again")
            return HttpResponseRedirect("/")
        
        app.save()
        UploadedFile=request.FILES['file_name']
        fs=FileSystemStorage()
        file=fs.save(UploadedFile.name,UploadedFile)
        file_url = fs.url(file)
       
        file_path= '/home/ananxsab/testing_project/media/'+file
        subject = 'job profile'
        ctx = {
        
        'first_name':app.first_name,
        'last_name':app.last_name,
        'email_add':app.email_add,
        'experience':app.Experience,
        'Telephone':app.Mobile}
        
      
        msg = render_to_string('job_detail_thankyou_template.html',ctx)
        from_email = settings.EMAIL_HOST_USER
        to_email = 'noreplyasc3@gmail.com'
        mail = EmailMessage(
        subject,
        msg,
        from_email,
        [to_email],)
        mail.content_subtype='html'
        mail.attach_file(file_path)
        email_res = mail.send()
        return render(request,'thankyou.html')
    else:
        return render(request,'applynowform.html')
        
        
             
  
   

def thankyou(request):
    form=NewUserForm()
    stud=User.objects.all()
    return render(request,'thankyou.html',{'form':form,'stu':stud})

def success(request):
    
    form=NewUserForm()
    
    if request.method=="POST":
       form=NewUserForm(request.POST)
       if form.is_valid():
           fnm= form.cleaned_data['first_name']
           lnm= form.cleaned_data['last_name']
           email= form.cleaned_data['email_add']
           phone= form.cleaned_data['Telephone']
           country= form.cleaned_data['country']

           reg=User(first_name=fnm,last_name=lnm,email_add=email,Telephone=phone,country=country)
           reg.save()
      
       form=NewUserForm(request.POST)
       stud=User.objects.all() 
       subject="Subject"
       html_message = render_to_string('thankyou.html', {'form':form,'stu':stud})
       plain_message = strip_tags(html_message)
       from_email = settings.EMAIL_HOST_USER
       to = request.POST.get('email_add')
       mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
       form=NewUserForm()
       stud=User.objects.all() 
       return render(request,'thankyou.html',{'form':form,'stu':stud})
      
    else:
     form=NewUserForm()
     stud=User.objects.all() 
     return render(request,'success.html',{'form':form,'stu':stud})


def summary(request):
  return render(request, 'summary.html',{'form':request.GET})

def mobileapp(request):
    if request.method=="POST":
          #pro=User()
          if(request.POST.get('branch_1_answers')=='nativemobileapp'):
           #pro.option=request.POST.get('branch_1_answers')
           request.session['branch_1_answers'] = request.POST.get('branch_1_answers')
          elif(request.POST.get('branch_1_answers')=='progressivewebspp'):
           #pro.option=request.POST.get('branch_1_answers')
           request.session['branch_1_answers'] = request.POST.get('branch_1_answers')
          
         # pro.save()
          return HttpResponseRedirect('/budget/')
    else:
        return render(request,'mobileapp.html')
def web(request):
    if request.method=="POST":
        
           if(request.POST.get('branch_2_answers')=='static-website'):
             request.session['branch_2_answers'] = request.POST.get('branch_2_answers')
             return HttpResponseRedirect('/static-website-development/')
           elif(request.POST.get('branch_2_answers')=="CMS-Development"):
            request.session['branch_2_answers'] = request.POST.get('branch_2_answers')
            return HttpResponseRedirect('/website-with-cms/')
           elif(request.POST.get('branch_2_answers')=="FrontEnd-Development"):
            request.session['branch_2_answers'] = request.POST.get('branch_2_answers')
            return HttpResponseRedirect('/frontend-development/')
           elif(request.POST.get('branch_2_answers')=="Ecom-Development"):
            request.session['branch_2_answers'] = request.POST.get('branch_2_answers')
            return HttpResponseRedirect('/ecommerce-development/')
          # wb.save()
          
    else:
       return render(request,'web.html')
def servermanagement(request):
    if request.method=="POST":
           #sv=User()
           if(request.POST.get('branch_4_answers')=='Web hosting'):
            request.session['branch_4_answers'] = request.POST.get('branch_4_answers')
            
           elif(request.POST.get('branch_4_answers')=='cloud hosting'):
             request.session['branch_4_answers'] = request.POST.get('branch_4_answers')
            
           elif(request.POST.get('branch_4_answers')=='dedicated servers'):
            request.session['branch_4_answers'] = request.POST.get('branch_4_answers')
             
           elif(request.POST.get('branch_4_answers')=='gsuite'):
             request.session['branch_4_answers'] = request.POST.get('branch_4_answers')
            
           #sv.save()
           return HttpResponseRedirect('/budget/')
    else:
      return render(request,'servermanagement.html')
def design(request):
    if request.method=="POST":
           #ds=User()
           if(request.POST.get('branch_5_answers')=='content creation'):
             request.session['branch_5_answers'] = request.POST.get('branch_5_answers')
             
           elif(request.POST.get('branch_5_answers')=='video editing'):
             request.session['branch_5_answers'] = request.POST.get('branch_5_answers')
             
           elif(request.POST.get('branch_5_answers')=='email marketing'):
             request.session['branch_5_answers'] = request.POST.get('branch_5_answers')
            
           elif(request.POST.get('branch_5_answers')=='digital branding'):
              request.session['branch_5_answers'] = request.POST.get('branch_5_answers')
            
          # ds.save()
           return HttpResponseRedirect('/budget/')
    else:
      return render(request,'design.html')
def software(request):
    if request.method=="POST":
           #so=User()
           if(request.POST.get('branch_6_answers')):
             request.session['branch_6_answers'] = request.POST.get('branch_6_answers')
            
             
           #so.save()
           return HttpResponseRedirect('/budget/')
    else:
      return render(request,'software.html')
def seo(request):
    if request.method=="POST":
           #ht=User()
           if(request.POST.get('seo_options')):
              request.session['seo_options'] = request.POST.get('seo_options')
          # ht.save()
           return HttpResponseRedirect('/budget/')
          
    else:
     return render(request,'seo.html')
def machinelearning(request):
    if request.method=="POST":
           #mc=User()
           if(request.POST.get('branch_7_answers')):
            request.session['branch_7_answers'] = request.POST.get('branch_7_answers')
             
           #mc.save()
           return HttpResponseRedirect('/budget/')
    else:
     return render(request,'machinelearning.html')
def digitalmarketing(request):
    if request.method=="POST":
           #ht=User()
           if(request.POST.get('digital_options')):
              request.session['digital_options'] = request.POST.get('digital_options')
          # ht.save()
           return HttpResponseRedirect('/budget/')
    else:
     return render(request,'digitalmarketing.html')

def staticwebsite(request):
    if request.method=="POST":
           #ht=User()
           if(request.POST.get('html_options')):
              request.session['html_options'] = request.POST.get('html_options')
           if(request.POST.get('home_page')):
             request.session['home_page'] = request.POST.get('home_page')
           if(request.POST.get('inner_pages')):
             request.session['inner_pages'] = request.POST.get('inner_pages')
           if(request.POST.get('html_development_notes')):
             request.session['html_development_notes'] = request.POST.get('html_development_notes')
          
           #ht.save()
           return HttpResponseRedirect('/budget/')
    else:
        return render(request,'staticwebsite.html')
def cmsoption(request):
    if request.method=="POST":
           #cm=User()
           if(request.POST.get('cms_options')):
            request.session['cms_options'] = request.POST.get('cms_options')
           if(request.POST.get('cms_development_notes')):
             request.session['cms_development_notes'] = request.POST.get('cms_development_notes')
           #cm.save()
           return HttpResponseRedirect('/budget/')
    else:
      return render(request,'cmsoption.html')
def ecommerceoption(request):
    if request.method=="POST":
           #cm=User()
           if(request.POST.get('ecom_options')):
            request.session['ecom_options'] = request.POST.get('ecom_options')
           if(request.POST.get('ecom_development_notes')):
            request.session['ecom_development_notes'] = request.POST.get('ecom_development_notes')
           #cm.save()
           return HttpResponseRedirect('/budget/')
    else:
      return render(request,'ecommerceoption.html')
def frontendoption(request):
    if request.method=="POST":
           #fr=User()
           if(request.POST.get('frontend_options')):
             request.session['frontend_options'] = request.POST.get('frontend_options')
           if(request.POST.get('frontend_development_notes')):
             request.session['frontend_development_notes'] = request.POST.get('frontend_development_notes')
           #fr.save()
           return HttpResponseRedirect('/budget/')
    else:
       return render(request,'frontendoption.html')
def budget(request):
    
    if request.method=="POST":
          #bud=User()
          if(request.POST.get('budget_slider')):
        
           #bud.budget=request.POST.get('budget_slider')
           request.session['budget_slider'] = request.POST.get('budget_slider')
           #bud.save()
          return HttpResponseRedirect('/form/')
    else:
        return render(request,'budget.html')
    
     
        
        
def pagewiseseo(request):
    return render(request,'pagewiseseo.html')
def techseo(request):
    return render(request,'techseo.html')
def googleads(request):
    return render(request,'googleads.html')
def websiteaudit(request):
    return render(request,'websiteaudit.html')
def form(request):
    if request.method=="POST":
      if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email_add') and request.POST.get('country') and request.POST.get('Telephone')  :
        
        reg2=User()
   
        reg2.first_name=request.POST.get('first_name')
        reg2.last_name=request.POST.get('last_name')
        reg2.email_add=request.POST.get('email_add')
        reg2.country=request.POST.get('country')
        reg2.Telephone=request.POST.get('Telephone')
        reg2.budget= request.session['budget_slider']
       
       #mobile app development
        if (request.session['branch_1_group_1']=='Mobile-App-Development'):
         reg2.project= request.session['branch_1_group_1']
         if (request.session['branch_1_answers']=='nativemobileapp'):
          reg2.option =  request.session['branch_1_answers']
         elif(request.session['branch_1_answers']=='progressivewebapp'):
          reg2.option =  request.session['branch_1_answers']

       # web development
        if(request.session['branch_1_group_1']=='Web-Development'):
         reg2.project= request.session['branch_1_group_1']
         if (request.session['branch_2_answers']=='Static-Website'):
          reg2.option =  request.session['branch_2_answers']
          reg2.html_options=request.session['html_options']
          reg2.homepage=request.session['home_page']
          reg2.innerpages=request.session['inner_pages']
          reg2.html_development_notes=request.session['html_development_notes']
         
         if (request.session['branch_2_answers']=='FrontEnd-Development'):
          reg2.option =  request.session['branch_2_answers']
          reg2.frontend_options=request.session['frontend_options']
          reg2.frontend_development_notes=request.session['frontend_development_notes']


         if (request.session['branch_2_answers']=='CMS-Development'):
          reg2.option =  request.session['branch_2_answers']
          reg2.cms_options=request.session['cms_options']
          reg2.cms_development_notes=request.session['cms_development_notes']
         
         if (request.session['branch_2_answers']=='Ecom-Development'):
          reg2.option =  request.session['branch_2_answers']
          reg2.ecom_options=request.session['ecom_options']
          reg2.ecom_development_notes=request.session['ecom_development_notes']


         
        # seo optimization
        if(request.session['branch_1_group_1']=='Seo-Optimization'):
         reg2.project= request.session['branch_1_group_1']
         reg2.seo_options=request.session['seo_options']
         
          
        
          
          
         #Graphics design

        if(request.session['branch_1_group_1']=='Design'):
         reg2.project= request.session['branch_1_group_1']
         if (request.session['branch_5_answers']=='content creation'):
          reg2.option =  request.session['branch_5_answers']
         elif (request.session['branch_5_answers']=='video editing'):
          reg2.option =  request.session['branch_5_answers']
         elif (request.session['branch_5_answers']=='email marketing'):
          reg2.option =  request.session['branch_5_answers']
         elif (request.session['branch_5_answers']=='digital branding'):
          reg2.option =  request.session['branch_5_answers']

        #software development
        if(request.session['branch_1_group_1']=='Software-Product-Development'):
         reg2.project= request.session['branch_1_group_1']
         if (request.session['branch_6_answers']=='software product developement'):
           reg2.option =  request.session['branch_6_answers']
        
        
        #Machine learning
        if(request.session['branch_1_group_1']=='Machine-Learning'):
         reg2.project= request.session['branch_1_group_1']
         if (request.session['branch_7_answers']=='machine learning'):
           reg2.option =  request.session['branch_7_answers']


        #server management
        if(request.session['branch_1_group_1']=='Server-Management'):
         reg2.project= request.session['branch_1_group_1']
         if (request.session['branch_4_answers']=='Web hosting'):
          reg2.option =  request.session['branch_4_answers']
         elif (request.session['branch_4_answers']=='cloud hosting'):
          reg2.option =  request.session['branch_4_answers']
         elif (request.session['branch_4_answers']=='dedicated servers'):
          reg2.option =  request.session['branch_4_answers']
         elif (request.session['branch_4_answers']=='gsuite'):
          reg2.option =  request.session['branch_4_answers']
         
         #digital marketing
        if(request.session['branch_1_group_1']=='digital-marketing'):
         reg2.project= request.session['branch_1_group_1']
         reg2.digital_options = request.session['digital_options']
        
        reg2.save()
        ctx = {'user': reg2.first_name}
       
        subject="Project Enquiry"
        html_message =  get_template('user_welcome_template.html').render(ctx)
        admin_message= render_to_string('admin_thank_template.html',{'first_name':reg2.first_name,
                'project_name':reg2.project,
                'project_type':reg2.option,
                'last_name':reg2.last_name,
                'email_add':reg2.email_add,
                'country':reg2.country,
                'Telephone':reg2.Telephone})
        plain_message = strip_tags(html_message)
        plain_message = strip_tags(admin_message)
        from_email =settings.EMAIL_HOST_USER
        to1 = 'noreplyasc3@gmail.com'
        to = request.POST.get('email_add')
        mail.send_mail(subject, plain_message,from_email,[to], html_message=html_message)
        mail.send_mail(subject,plain_message,from_email, [to1],html_message=admin_message)
        return render(request,'thankyou.html')
        
    else:
     return render(request,'form.html')





def user_welcome_template(request):
    return render(request,'user_welcome_template.html')
def admin_thank_template(request):
    return render(request,'admin_thank_template.html')

def contactus(request):

    if request.method=="POST":
     if request.POST.get('email') and request.POST.get('subject') and request.POST.get('message')   :
             cont=Contact()
             cont.email=request.POST.get('email')
             cont.subject=request.POST.get('subject')
             cont.message=request.POST.get('message')
             cont.save()
             subject=request.POST.get('subject')
             content=request.POST.get('message')
             from_email=request.POST.get('email')
             to = 'noreplyasc3@gmail.com'
             mail.send_mail(subject, content,from_email,[to])
             return render(request, 'thankyou.html')
    else:
        return render(request,'contactus.html')




   
          
       
      













