import requests,json

token = "9312ced9250b10bf0adcf33eaf26ac4b183af3a337f6dbc639eaad4640aefe1a6f1561d1"
contacttag_url = "https://nuphysical.activehosted.com/api/3/contactTags"
headers = {
    'Api-Token': token,
    'accept': 'application/json',
    'content-type': 'application/json'
}

def update_contact(id, email, first_name, last_name, phone_number, age, dob):
    update_url = "https://nuphysical.activehosted.com/api/3/contacts/" + id
    payload = {
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
    }
    response = requests.put(update_url, headers=headers, json=payload)

    contacttag_payload = {
        "contactTag": {
            "contact": id,
            "tag": 63
        }
    }
    response = requests.post(contacttag_url, headers=headers, json=contacttag_payload)
