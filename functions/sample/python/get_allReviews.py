# THIS CODE IS TO BE USED INSIDE OF IBM CLOUD
import sys 
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    
    authenticator = IAMAuthenticator('I_AM_API_KEY')
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
        doc.pop('_id')
        doc.pop('_rev')
        formatResult.append(doc)
            
    return {'headers': {'Content-Type':'application/json'}, 
            'body': formatResult, 
            }
            