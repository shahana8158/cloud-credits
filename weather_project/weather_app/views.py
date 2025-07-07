
from django.shortcuts import render
import requests
import datetime
from django.contrib import messages
# Create your views here.

def home(request):
   if 'city' in request.POST:
      city = request.POST['city']
   else:
      city = 'indore'
      


   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=222dfebd3a42b903eed59a9218447c84"
   PARAMS ={'units':'metric'}
   API_KEY ='AIzaSyBO3vL3dPBHxetaF_Opq9CfkLFOYu_hMPQ'
   SEARCH_ENGINE_ID ='83e15e90533a1428b'

   query = city + " 1920x1080"
   page = 1
   start = (page - 1) * 10 + 1
   searchType = 'image'
   city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

   data = requests.get(city_url).json()
   count = 1
   search_items = data.get("items")
   image_url = search_items[1]['link']

   try:

        data = requests.get(url,params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity =data['main']['humidity']
        day = datetime.date.today()

        return render(request,'home.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city ,'humidity':humidity, 'exception_occurred':False ,'image_url':image_url})
   
   except KeyError:
       exception_occurred=True
       messages.error(request,'entered data is not available to API')
       day=datetime.date.today()

       return render(request,'home.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 ,'humidity':50, 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )