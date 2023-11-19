# with requests module
    pip install requests

### post
    url= ""
    headers = {
        'Token': "",
        'Content-Type' : 'application/json'
    }

        
    payload = {
        "location_id":location_id,
        "inventory_item_id":data[2]['inventory_item_id'],
        "available":data[2]['quantity']
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload)).json()

### get
    response = requests.post(url).json()


# with out requests module (urllib3)
for aws lambda functions

    import urllib3
    import json
    def lambda_handler(event, context):
        
        file_key = event['Records'][0]['s3']['object']['key']
        file_name_without_ext = (lambda file_name: file_name.split('.')[0]) (file_key.split('/')[-1])
        fist_three_letter = file_name_without_ext[:3]

        http = urllib3.PoolManager()
        data = {
            "key": file_key
        }
        body = json.dumps(data)
        headers = {'Content-Type': 'application/json'}

        #----------------- sending mail -----------------------
        email_send_url = ""
        email_response = http.request(
            'POST', 
            email_send_url,
            headers=headers,
            body=body
        )
        print(email_response.data.decode('utf-8'))
        print("------- email has been sent -------")
        #==================== sending mail ====================



