import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from typing import Optional

def index(request, route: str):
    # return HttpResponse("<h1>path parameter dynamique</h1>")
    return render(request, "harouna.html")

def users(request):
    # retourner le contenu du fichier
    chemin = "file.txt"
    separateur = "   @@@   "
    
    selecteur: Optional[str] = request.GET.get('selecteur')
    print("selecteur " , selecteur, type(selecteur))

    # Vérifier si le fichier existe et lire son contenu
    if os.path.exists(chemin):
        with open(chemin, 'r') as fp:

            # S'il n'y a pas de sélecteur
            if selecteur == None:
                # On récupère tout le contenu du fichier
                contenu_fichier = fp.read()
            else:
                # Sinon on va filtrer en fonction du sélecteur
                content_list = []
                lignes = fp.readlines()
                for ligne in lignes:
                    infos = ligne.split(separateur)
                    id_user = infos[0]
                    heure_consult = infos[1]
                    id_device = infos[2]

                    chaine = ""
                    
                    if 'id_user' in selecteur:
                        chaine += id_user + " "
                    if 'heure' in selecteur:
                        chaine += heure_consult + " "
                    if 'id_device' in selecteur:
                        chaine += id_device

                    content_list.append(chaine)
                # Qu'importe le nombre de filtres sélectionnés, ils sont tous cassé 
                # et insérés dans la chaine <contenu_fichier>
                contenu_fichier = "\n".join(content_list)

    else:
        contenu_fichier = "Le fichier de file.txt est vide ou n'existe pas."
    # Retourner le contenu du fichier dans la réponse HTTP
    return HttpResponse(f"<pre>{contenu_fichier}</pre>")
    # return HttpResponse(f"<pre>{id_user}</pre>")
    # return HttpResponse("Espace users")

def users_details(request, id_user: int):
    return HttpResponse(f"Vous etes l'utilisateurs n°{id_user}")

def users_devices(request, id_user: int, id_device: int):
    # ajouter dans un fichier l'heure de consultation de la vue, l'id du user, et l'id device

    chemin = "file.txt"
    separateur = "   @@@   "

    heure_consult = datetime.now()
    info_consultation = f"{id_user}{separateur}{heure_consult}{separateur}{id_device}\n"

    with open(chemin, 'a') as fp:
        fp.write(info_consultation)
    return HttpResponse(f"l'utilisateur n°{id_user}, a consulté la vue à {heure_consult}, avec le device n°{id_device}\n")
