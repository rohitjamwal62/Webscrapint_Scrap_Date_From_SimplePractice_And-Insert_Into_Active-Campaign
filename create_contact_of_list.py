import requests,json

token = "9312ced9250b10bf0adcf33eaf26ac4b183af3a337f6dbc639eaad4640aefe1a6f1561d1"
contact_url = "https://nuphysical.activehosted.com/api/3/contacts"
contacttag_url = "https://nuphysical.activehosted.com/api/3/contactTags"
contactlist_url = "https://nuphysical.activehosted.com/api/3/contactLists"

headers = {
    'Api-Token': token,
    'accept': 'application/json',
    'content-type': 'application/json'
}

# function to create a contact and subscribe a contact to a list
def create_contact_of_list(email, first_name, last_name, phone_number, age, dob):
    try:
        contact_payload = json.dumps({
            "contact": {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone_number,
                "fieldValues": [
                    {"field": "30", "value": age},
                    {"field": "29", "value": dob}
                ]
            }
        })
        response = requests.post(contact_url, headers=headers, data=contact_payload)
        contact_dict = json.loads(response.text)
        contact_id = contact_dict["contact"]["id"]
        
        contacttag_payload = json.dumps({
            "contactTag": {"contact": contact_id, "tag": 63}
        })
        response_tag = requests.post(contacttag_url, headers=headers, data=contacttag_payload)
        
        contactlist_payload = json.dumps({
            "contactList": {"list": 26, "contact": contact_id, "status": 1}
        })
        response_list = requests.post(contactlist_url, headers=headers, data=contactlist_payload)
        
        return response_list.json()
    
    except Exception as e:
        # Handle or log the exception appropriately
        print("An error occurred:", str(e))
