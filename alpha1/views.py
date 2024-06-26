import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index(request, route: str):
    # return HttpResponse("<h1>path parameter dynamique</h1>")
    return render(request, "harouna.html")

def users(request):
    # retourner le contenu du fichier
    chemin = "file.txt"
    separateur = "   @@@   "
    # print(request.GET)

    # Vérifier si le fichier existe et lire son contenu
    if os.path.exists(chemin):
        with open(chemin, 'r') as fp:
            lignes = fp.readlines()

            id_users = []
            for ligne in lignes:
                infos = ligne.split(separateur)
                id_user = infos[0]
                id_users.append(id_user)
        contenu_fichier = "\n".join(id_users)

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
