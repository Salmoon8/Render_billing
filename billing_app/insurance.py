
import requests , json
def get_insurance_percentage(patient_id):
     registeration_url=f'https://registration-zf9n.onrender.com/patient/'
     response=requests.get(f'{registeration_url}{patient_id}')
     print(response)
     if response.status_code ==200:
         response=json.loads(response.text)
         print(response["data"]['insurancePersentage'])
         insurance=response["data"]['insurancePersentage']
         print(insurance)
         insurace_response={
             "status code": response.status_code,
             "insurance": insurance   
         }
     else: 
        insurace_response={
             "status code": response.status_code,
             "error": response.text   
         }
          
     return insurace_response
print(get_insurance_percentage(2))