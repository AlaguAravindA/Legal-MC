import requests 
def translate(gentext,ln):

    url = "https://api.apilayer.com/language_translation/translate?target="+ln

    payload = gentext.encode("utf-8")
    headers= {
  "apikey": "Your-api-key"
}
    response = requests.request("POST", url, headers=headers, data = payload)

    response = requests.post(url, data=payload, headers=headers)

    data1=response.json()

  
   
    translated_text = data1['translations'][0]['translation']
    return(translated_text)














