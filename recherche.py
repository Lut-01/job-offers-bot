from auth import obtenir_token
from suivi import detecter_nouvelles_offres
import requests

def rechercher_offres(mot_cle, departement=None):
    token = obtenir_token()
    
    url = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    params = {
        "motsCles": mot_cle
    }
    
    if departement:
        params["departement"] = departement
    
    reponse = requests.get(url, headers=headers, params=params)
    
    if reponse.status_code in (200, 206):
        resultats = reponse.json()
        return resultats.get("resultats", [])
    else:
        print(f"Erreur pour '{mot_cle}' (dept {departement}) : {reponse.status_code}")
        print(reponse.text)
        return []

def rechercher_plusieurs_criteres(liste_mots_cles, liste_departements, alternance_uniquement=True):
    toutes_les_offres = {}
    
    for mot_cle in liste_mots_cles:
        for departement in liste_departements:
            offres = rechercher_offres(mot_cle, departement)
            
            if alternance_uniquement:
                offres = [o for o in offres if o.get("alternance") is True]
            
            for offre in offres:
                toutes_les_offres[offre["id"]] = offre
    
    return list(toutes_les_offres.values())

if __name__ == "__main__":
    mots_cles = ["développeur", "support informatique", "data", "développement web"]
    departements = ["75", "78"]
    
    offres = rechercher_plusieurs_criteres(mots_cles, departements)
    print(f"Total unique : {len(offres)} offre(s) en alternance trouvées")
    
    nouvelles = detecter_nouvelles_offres(offres)
    print(f"\n{len(nouvelles)} nouvelle(s) offre(s) depuis le dernier passage :")
    for offre in nouvelles:
        print(f"- {offre['intitule']} ({offre.get('entreprise', {}).get('nom', 'Entreprise non précisée')})")