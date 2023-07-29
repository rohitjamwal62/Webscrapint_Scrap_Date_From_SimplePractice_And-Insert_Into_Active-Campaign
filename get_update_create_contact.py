import requests,json
from create_contact_of_list import create_contact_of_list
from selenium_simplepractice import scrape
from update_contact import update_contact

token = "9312ced9250b10bf0adcf33eaf26ac4b183af3a337f6dbc639eaad4640aefe1a6f1561d1"
get_contact_url = "https://nuphysical.activehosted.com/api/3/contacts?listid=26"
headers = {
    'Api-Token': token,
    'accept': 'application/json',
    'content-type': 'application/json'
}

# Endpoint to retrieve all contacts for a list
# Function to get all contacts of a list, then create or update contacts accordingly to existing contact details
def get_create_update_contact(user_contact_list):
    contact_list = json.loads(requests.request("GET", get_contact_url, headers=headers).text).get('contacts')
    contact_email_list = [contact_email['email'] for contact_email in contact_list]
    contact_id_list = [contact_id['id'] for contact_id in contact_list]
    exist_contact = {}
    
    # Create a dictionary of email and id pairs for existing contacts
    for key in contact_email_list:
        for value in contact_id_list:
            exist_contact[key] = value
            contact_id_list.remove(value)
            break
    
    # Compare existing contacts with user contact list and create or update contacts accordingly
    for user_contact in user_contact_list:
        if user_contact.get('email') not in exist_contact.keys():
            print("Creating Records__________")
            create_contact_of_list(
                user_contact.get('email'),
                user_contact.get('firstName'),
                user_contact.get('lastName'),
                user_contact.get('phone'),
                user_contact.get('age'),
                user_contact.get('dob')
            )
        else:
            id_of_email = user_contact.get('email')
            print("Updating Records___________")
            update_contact(
                exist_contact[id_of_email],
                user_contact['email'],
                user_contact['firstName'],
                user_contact['lastName'],
                user_contact['phone'],
                user_contact['age'],
                user_contact['dob']
            )

# Example usage
user_contact_list = scrape()
get_create_update_contact(user_contact_list)
