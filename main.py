from recherche import rechercher_plusieurs_criteres
from suivi import detecter_nouvelles_offres
from notifications import notifier_nouvelles_offres

def main():
    mots_cles = ["développeur", "support informatique", "data", "développement web"]
    departements = ["75", "78"]
    
    print("Recherche des offres en cours...")
    offres = rechercher_plusieurs_criteres(mots_cles, departements)
    print(f"{len(offres)} offre(s) en alternance trouvées au total")
    
    nouvelles = detecter_nouvelles_offres(offres)
    print(f"{len(nouvelles)} nouvelle(s) offre(s) détectée(s)")
    
    if nouvelles:
        notifier_nouvelles_offres(nouvelles)
        print("Notifications envoyées !")
    else:
        print("Rien de nouveau, aucune notification envoyée.")

if __name__ == "__main__":
    main()