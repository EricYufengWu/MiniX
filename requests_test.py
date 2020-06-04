import binascii, json, requests, time

     
Key = 'hvWEBqdUgNtRqQAPcrVwd7fyJJwxJQGr4pIq24vUMq'
     
def SL_setup():
     urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     headers = {"Accept":"application/json","x-ni-api-key":Key}
     return urlBase, headers
     
def Put_SL(Tag, Type, Value):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     propValue = {"value":{"type":Type,"value":Value}}
     try:
          reply = requests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)         
          reply = 'failed'
     return reply

def Get_SL(Tag):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     try:
          value = requests.get(urlValue,headers=headers).text
          data = json.loads(value)
          #print(data)
          result = data.get("value").get("value")
     except Exception as e:
          print(e)
          result = 'failed'
     return result
     
def Create_SL(Tag, Type):
     urlBase, headers = SL_setup()
     urlTag = urlBase + Tag
     propName={"type":Type,"path":Tag}
     try:
          requests.put(urlTag,headers=headers,json=propName).text
     except Exception as e:
          print(e)
          
# Get_SL('Bill')
# Create_SL('Bill','STRING')
# Put_SL('Bill','STRING','done')
# Get_SL('Bill')
while True:
     print('Grabing info from Tag:{}'.format(Get_SL('Bill'))
     Put_SL('Eric','STRING','Hello SystemLink')