from django.shortcuts import render

# Create your views here.
def landing(request): 
  return render (request, 'base/landing.html')

from django.shortcuts import render
import openai, os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY")

def bot(request): 
    bot_response = None 
    if api_key is not None and request.method=="POST":
        openai.api_key = api_key
        nightlife = request.POST.get('nightlife')
        attractions = request.POST.get('attractions')
        pets = request.POST.get('pets')
        city = request.POST.get('city')
        prompt = (f"Please be my tour guide! I am traveling in {city}. I am interested in going to {{attractions}}. {{pets}} traveling with pets and or children. {{nightlife}} intersted in shopping and nightlife.")
        response = openai.Completion.create(
            model = 'text-davinci-003', 
            prompt = prompt, 
            max_tokens = 256, 
            temperature = 0.5
        )
        print(response)
        bot_response = response["choices"][0]["text"]
    return render(request, 'base/guide.html', {
        "response": bot_response
    })
  
def landing(request): 
  return render (request, "base/landing.html")

def causes(request):
  return render (request, "base/causes.html")

def calculator(request):
  return render (request, "base/calculator.html")



