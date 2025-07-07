import requests
from django.shortcuts import render
import json




def indexpage(request):
    api_key="7acedd47a7a52e875cfcdaea"
    currency_url=f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    currency_request=requests.get(currency_url)
    currency_response=currency_request.json()
    supported_codes = currency_response.get('supported_codes',[])
    currency = [(code[0]) for code in supported_codes]
    
    if request.method == "POST":
        

        from_currency =request.POST.get('from_currency')
        to_currency =request.POST.get('to_currency')
        amount = request.POST.get('amount')
        

 
        endpoint_url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
        

        endpoint_request=requests.get(endpoint_url)
        
        endpoint_response=endpoint_request.json()
        
        result = endpoint_response['conversion_result']
        

        context ={
            'currency':currency,
            'result':result
           
        }

        return render(request,'index.html',context)

    context ={
        "currency":currency
    }

    
    return render(request,'index.html', context)