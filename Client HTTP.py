from pip._vendor import requests

# -----------------------------------------------------------------------------------------------#
# Ce programme permet de réaliser des requêtes HTTP de type GET, POST, PUT et DELETE
# Il permet de récupérer des données, d'envoyer des données, de modifier des données et de supprimer des données
# Il utilise la librairie requests pour réaliser ces requêtes
# Il n'est pas complet et ne gère pas toutes les erreurs possibles (ex: URL invalide, mauvais type de données reçus, etc.)
# Il est à titre d'exemple et pourrait être complété pour être utilisé dans un cas réel
# -----------------------------------------------------------------------------------------------#


# Fonctions pour les requêtes HTTP : GET, POST, PUT, DELETE

# Comme vu dans la 1ère partie de notre BE, Requests possède des gestions d'erreurs intégrées qui permettent de lever des exceptions
# en cas d'erreur HTTP. Cela permet de gérer les erreurs de manière plus propre et de ne pas laisser le programme planter en cas d'erreur.
# Cela permet également de ne pas avoir à gérer les erreurs à la main et de ne pas avoir à écrire des conditions pour chaque cas d'erreur possible.

#Fonction GET : Permet de récupérer des données depuis un serveur web
def GET(url, params, headers):
    try:
        response = requests.get(url, data=params, headers=headers)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP et fait passer le programme en mode erreur
        return response
    # Si le programme renvoie une erreur, on l'affiche et on retourne None
    except requests.exceptions.RequestException as e:
        print(f"GET request failed: {e}")
        print(response.status_code)
        return None

#Fonction POST : Permet d'envoyer des données à un serveur web
def POST(url, data, headers):
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status() # Lève une exception pour les erreurs HTTP et fait passer le programme en mode erreur
        return response
    # Si le programme renvoie une erreur, on l'affiche et on retourne None
    except requests.exceptions.RequestException as e:
        print(f"POST request failed: {e}")
        print(response.status_code)
        return None

#Fonction PUT : Permet de modifier des données déjà existantes
def PUT(url, data, headers):
    try:
        response = requests.put(url, data=data, headers=headers)
        response.raise_for_status() #Lève une exception pour les erreurs HTTP et fait passer le programme en mode erreur
        return response
    # Si le programme renvoie une erreur, on l'affiche et on retourne None
    except requests.exceptions.RequestException as e:
        print(f"PUT request failed: {e}")
        print(response.status_code)
        return None

#Fonction DELETE : Permet de supprimer des données
def DELETE(url, headers):
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status() #Lève une exception pour les erreurs HTTP et fait passer le programme en mode erreur
        print(response.text)
        return response
    #Si le programme renvoie une erreur, on l'affiche et on retourne None
    except requests.exceptions.RequestException as e:
        print(f"DELETE request failed: {e}")
        print(response.status_code)
        return None

#--------------------------------------------------------------------------------------------------#

#Fonctions pour vérifier les entrées de l'utilisateur : fonction, URL

#Fonction vérification fonction
def verif_fonction():
    fonction = ""
    while fonction not in ["GET", "POST", "PUT", "DELETE"]:  # On vérifie si la fonction est valide
        # On demande à l'utilisateur de choisir une fonction
        fonction = input("Quelle fonction souhaitez-vous utiliser ? (GET, POST, PUT, DELETE): ")
    return fonction

#Fonction vérification URL
def verif_url():
    url = input("Entrer l'URL que vous souhaitez atteindre: ")
    while url[0:4] != "http":  # On vérifie si l'URL est valide
        url = input("URL invalide, veuillez entrer une URL valide: ")
    return url


# -----------------------------------------------------------------------------------------------#
#Partie de traitement des réponses et de la continuité du programme :

#Fonction pour traiter la réponse
def traitement_reponse(reponse):
    if reponse is not None:
        print("Voici le contenu de la réponse: ")
        print(reponse.text)
        print(reponse.status_code)
        print(reponse.json())
    return reponse

#Fonction pour demander à l'utilisateur s'il souhaite continuer
def continuer(ensemble_reponse):
    continuer = input("Voulez-vous continuer? (oui,non): ")
    while continuer not in ["oui", "non"]:
        continuer = input("Voulez-vous continuer? (oui, non): ")
    if continuer == "oui":
        main(ensemble_reponse)
    else:
        print("Merci d'avoir utilisé notre programme")

#--------------------------------------------------------------------------------------------------#

#Fontion principale
def main(ensemble_reponse):
    #On demande à l'utilisateur de saisir l'URL qu'il souhaite atteindre
    url=verif_url()
    #On vérifie la fonction que l'utilisateur souhaite utiliser
    fonction=verif_fonction()

    match fonction :  
        #Si le choix de l'utilisateur est GET on appelle la fonction requests.get et on affiche le texte obtenu
        #On retournera la liste des réponses en fin de programme
        case "GET":
            reponse=GET(url, params=None, headers=None)
            #Si la réponse n'est pas nulle, on affiche le texte reçu et le code de statut
            ensemble_reponse.append(traitement_reponse(reponse))

        #Si le choix de l'utilisateur est POST on lui demande de saisir les données à envoyer et on appelle la fonction requests.post
        #Dans un cas réel, nous pourrions utiliser un dictionnaire pré-rempli
        case "POST":
            donnees = {}
            donnees= (input("Entrer les données que vous souhaitez envoyer (sous forme de dictionnaire):"))
            reponse=POST(url,donnees,None)
            #Si la réponse n'est pas nulle, on affiche le text reçu et le code de statut
            ensemble_reponse.append(traitement_reponse(reponse))


        #Si le choix de l'utilisateur est PUT on lui demande de saisir les données à envoyer et on appelle la fonction requests.put
        #Fonction similaire à POST mais pour la modification de données déjà existantes
        case "PUT":
            donnees = {}
            donnees= (input("Entrer les données que vous souhaitez envoyer (sous forme de dictionnaire):"))
            reponse=PUT(url,donnees,None)
            #Si la réponse n'est pas nulle, on affiche le text reçu et le code de statut
            ensemble_reponse.append(traitement_reponse(reponse))


        #Choix de l'utilisateur est DELETE on appelle la fonction requests.delete
        #Si réponse == 200 = suppression effectuée avec succès, 202 = suppression acceptée mais n'a pas encore été effectuée
        # 204 =suppression effectuée mais aucune donnée n'a été renvoyée
        case "DELETE":
            reponse=DELETE(url,None)
            #Si la réponse n'est pas nulle, on affiche le text reçu et le code de statut
            ensemble_reponse.append(traitement_reponse(reponse))


        
    # On demande à l'utilisateur s'il souhaite continuer
    continuer(ensemble_reponse)
    return ensemble_reponse

#--------------------------------------------------------------------------------------------------#

#On initialise la liste des réponses
tab_reponse=[]
#On appelle la fonction principale
ensemble_reponse=main(tab_reponse)
#On affiche la liste des réponses obtenues
print(ensemble_reponse)
