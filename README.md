NOTE: Par simplicité, je conseille de créer un dossier ou se trouveront tous les fichier (python, jeux, emulateur, ...).

Installer python 3.12:
 - "Customize Installation" et vérifier que "pip" est coché,
 - click Next,
 - Cocher "Add Python to environment variables",
 - Valider et installer.

Ouvrir CMD et exécuter:
 - "python --version", doit normalement retourner 3.12.2. Si pas le cas, il faut récuper le chemin d'accès à l'exécutable python et c'est ca qui devra être utilisé au lieu de juste "python" dans les autres commandes.
 - "pip3.12 --version", doit retourner "pip X.0 from ....". Si pas le cas, installer pip : "python -m ensurepip --upgrade".

Installer les lib externes: "pip3.12 install pydirectinput".

Télécharger le fichier python et "vba.ini" sur le github, l'émulateur ici :"https://visualboyadvance.org/" et les roms GameBoyAdvance(GBA) ici: "https://www.rpgamers.fr/roms.html"

Editer le fichier python "StreamersVsChat Basic Twitch Plays Code.py" et remplier les données pour PASS (a récupérer via l'url) et CHANNEL (pseudo twitch: fuury_off).

Exécuter l'émulateur "visualboyadvance-m.exe" et aller dans le menu "Options > Input > Configure...". Il faut vérifier que les touches sont bien (si non, "Clear All" puis les assigner):
 - Up -> W
 - Down -> S
 - Left -> A
 - Right -> D
 - A -> Q
 - B -> B
 - L -> L
 - R -> R
 - Select -> Y
 - Start -> X

Dans l'émulateur, tu peux maintenant "File > Open ..." et lancer le jeux que tu veux.

Dans le répertoire avec tous les fichiers, faire clic droit, "Ouvrir dans le terminal", et entrer la commande: python "StreamersVsChat Basic Twitch Plays Code.py"

Si tout est bon, le terminal doit donner un truc du genre, et tu devraia voir posté un message dans ton chat Twitch:
	TwitchPlaysPokemon has joined fuury_off's Channel!
	tmi.twitch.tv CAP * ACK  : twitch.tv/tags

Attention: Il faut absolument que la fenêtrede l'emulateur soit en premier plan, sinon les commande exécuté par le tchat seront envoyé a d'autre fenêtres

Note: J'ai mappé les touches de la facon suivante (aka nom des commande pour le tchat):
 - "haut", "bas", "gauche", "droite" pour les flêche directionnelles
 - "A" pour A, "B" pour B, "L" pour L, "R" pour R
 - "X" pour Start et "Y" pour select
 - Pour toi UNIQUEMENT, la commande "exit" permet de couper le script (Pour eviter que les tchat ne spam quand tu reprends le controle de ton PC)
