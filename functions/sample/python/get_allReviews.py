# THIS CODE IS TO BE USED INSIDE OF IBM CLOUD TO DISPLAY ALL REVIEWS FOR SELECTED DEALERSHIP
# Invoke with parameter {"dealerId": "2"}, otherwise, you will get error: deadlerId not found


import sys 
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    
    authenticator = IAMAuthenticator('KDDy7JeifWad3-qZ_a44oSCdSQJJjsoV3g6DOqhoVsqu')
    cloudant = CloudantV1(authenticator=authenticator)
    cloudant.set_service_url("https://c0973199-be03-41ac-936f-8ee189aea9c2-bluemix.cloudantnosqldb.appdomain.cloud")
    
    """Get all reviews"""
    try:
        response = cloudant.post_all_docs(
            db = 'reviews',
            include_docs = True,
            limit = 50,
            ).get_result()['rows']
            
    except:  
        return { 
            'statusCode': 404, 
            'message': 'Something went wrong'
            }
    
    """Format result"""
    formatResult = []
    
    for row in response:
        doc = row['doc']
        if doc['id'] == int(dict['dealerId']):
            doc.pop('_id')
            doc.pop('_rev')
            formatResult.append(doc)
    
    if len(formatResult) == 0:
        return("No dealer with at id")
    
    return {'headers': {'Content-Type':'application/json'}, 
            'body': formatResult, 
            }
            