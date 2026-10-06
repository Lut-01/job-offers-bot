import os
import requests
from dotenv import load_dotenv

# Charge les variables depuis le fichier .env
load_dotenv()

client_id = os.getenv("FRANCE_TRAVAIL_CLIENT_ID")
client_secret = os.getenv("FRANCE_TRAVAIL_CLIENT_SECRET")

def obtenir_token():
    url = "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=/partenaire"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "api_offresdemploiv2 o2dsoffre"
    }
    
    reponse = requests.post(url, headers=headers, data=data)
    
    if reponse.status_code == 200:
        token = reponse.json()["access_token"]
        print("Token récupéré avec succès !")
        return token
    else:
        print(f"Erreur : {reponse.status_code}")
        print(reponse.text)
        return None

if __name__ == "__main__":
    token = obtenir_token()
    if token:
        print(token[:50] + "...")  # on affiche juste le début pour vérifier