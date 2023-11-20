"""Code to be used in IBM Cloudant. 
   Invoke with parameter: 
   {
"review": 
    {
        "id": 1114,
        "name": "Upkar Lidder",
        "dealership": 15,
        "review": "Great service!",
        "purchase": false,
        "another": "field",
        "purchase_date": "02/16/2021",
        "car_make": "Audi",
        "car_model": "Car",
        "car_year": 2021
    }
}
Without parameter, you will get message: error: review
"""

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator("KDDy7JeifWad3-qZ_a44oSCdSQJJjsoV3g6DOqhoVsqu")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://c0973199-be03-41ac-936f-8ee189aea9c2-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
            
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data': response,
        'message':'You have successfully posted your review!',}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }