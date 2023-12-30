
import requests ,json
def get_services_data(services_ids):
     ### replace with logic for admin api call
     # only use 5 for testing because there are no other services currently
     print("entered services")
     print(services_ids)
     Admin_services_url=f'https://admin-service-healu.onrender.com/api/v1/clinicService/'
     services_names=[]
     services_amounts=[]
     for id in services_ids:
          response=requests.get(f'{Admin_services_url}{id}')
          print("services", response)
          if response.status_code== 200:
            service_data=json.loads(response.text)
            service_name=service_data['data']['clinicService']["name"]
            service_amount=service_data['data']['clinicService']["price"]
            print(service_name,service_amount,response.status_code)
            services_names.append(service_name)
            services_amounts.append(service_amount)
            services_response={
                 "status code": response.status_code,
                 "services_names":services_names,
                 "services_amounts":services_amounts
            }
          else : ### handle 404 and other cases
                services_response={
                 "status code": response.status_code,
                 "error": response.text
                     }
        
     return services_response
print( get_services_data([1]))