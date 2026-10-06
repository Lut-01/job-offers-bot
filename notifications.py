import os
import requests
from dotenv import load_dotenv

load_dotenv()

webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

def envoyer_notification_discord(message):
    data = {
        "content": message
    }
    
    reponse = requests.post(webhook_url, json=data)
    
    if reponse.status_code == 204:
        print("Notification envoyée avec succès !")
    else:
        print(f"Erreur lors de l'envoi : {reponse.status_code}")
        print(reponse.text)

def notifier_nouvelles_offres(offres):
    if not offres:
        return
    
    for offre in offres:
        titre = offre["intitule"]
        entreprise = offre.get("entreprise", {}).get("nom", "Entreprise non précisée")
        lieu = offre.get("lieuTravail", {}).get("libelle", "Lieu non précisé")
        url_offre = offre.get("origineOffre", {}).get("urlOrigine", "")
        
        message = f"**Nouvelle offre : {titre}**\n🏢 {entreprise}\n📍 {lieu}\n🔗 {url_offre}"
        envoyer_notification_discord(message)

if __name__ == "__main__":
    envoyer_notification_discord("🎉 Le bot fonctionne ! Ceci est un message de test.")