import json
import os

FICHIER_SUIVI = "offres_connues.json"

def charger_offres_connues():
    if os.path.exists(FICHIER_SUIVI):
        with open(FICHIER_SUIVI, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def sauvegarder_offres_connues(ids_offres):
    with open(FICHIER_SUIVI, "w", encoding="utf-8") as f:
        json.dump(list(ids_offres), f)

def detecter_nouvelles_offres(offres_actuelles):
    ids_connus = charger_offres_connues()
    
    nouvelles_offres = [o for o in offres_actuelles if o["id"] not in ids_connus]
    
    tous_les_ids = ids_connus | {o["id"] for o in offres_actuelles}
    sauvegarder_offres_connues(tous_les_ids)
    
    return nouvelles_offres