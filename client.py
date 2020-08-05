from aws_requests_auth.aws_auth import AWSRequestsAuth
import requests
import time

auth = AWSRequestsAuth(aws_access_key='AKIA4MZDBMMYJXJGEVVW',
    aws_secret_access_key='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',
    aws_host='a2fy7vpo70ka8f-ats.iot.us-west-2.amazonaws.com',
    aws_region='us-west-2',
    aws_service='iotdata')

#Post Request example
data = {
    "state":{
        "desired":{
            "msg":"Send from HTTP Python"
        }
    }
}

while(1):
    res = requests.post('https://a2fy7vpo70ka8f-ats.iot.us-west-2.amazonaws.com/things/test/shadow',json=data,auth=auth)
    print(res.content)
    time.sleep(1)