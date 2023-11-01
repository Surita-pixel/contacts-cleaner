import os
import json
import pandas as pd



clean_contacts = []

def main():
    with open('TUARCHIVOJCONTACTOS.json', 'r', encoding='utf-8') as contacts:
        data = json.load(contacts)

        clean_contacts = []

        for contact in data:
            if contact['Mobile Phone'][0] == '+':
                if len(contact['Mobile Phone']) != 13:
                    continue  

                contact_name = contact['First Name'].lower()
                contact_name = contact_name.title()

                if 'Familia' in contact_name:
                    continue  

                data = {
                    "name": contact_name,
                    "phone": contact['Mobile Phone'][1:]
                }
                clean_contacts.append(data)

        sorted_clean_contacts = sorted(clean_contacts, key=lambda x: x['name'])

        df = pd.DataFrame(sorted_clean_contacts)

        df.to_excel('sorted_contacts.xlsx', index=False)

        
if __name__ == '__main__':
    main()