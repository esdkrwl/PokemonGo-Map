# PokemonGo Map
Map im Browser und Tweets in der Tasche!

#[Official Twitter] 
https://twitter.com/bot_ketchum


## How to setup
0. Projekt (Develop Branch) als Zip herunterladen.
1. Python 2.7.12 installieren. Wichtig, dass eine Umgebungsvariable für Python erstellt wird. https://www.python.org/downloads/release/python-2712/ Pc nach Installation neu starten.
2. Pip installieren. https://bootstrap.pypa.io/get-pip.py. Skript runterladen, Konsole öffnen (Strg + X Eingabeaufforderung(Administrator)), mit dem cd Befehl zum Speicherort wechseln und 'python get-pip.py' eintippen und bestätigen.
3. Node JS installieren https://nodejs.org/en/download/
4. Restliche Requirements installieren. In den Easy Setup Ordner mit dem cd Befehl wechseln und 'pip install -r requirements.txt' in die Konsole eintippen und bestätigen. Sollte es zu Fehlern kommen, probiert diesen Befehl 'pip install setuptools==21.2.1' und versucht Schritt 4 dann nochmal.
5. Skript starten. Dazu in der Konsole, sofern ihr euch über den pkmn Trainer Club einloggt.
 python runserver.py -a ptc -u USERNAME -p PASSWORT -l "ORT oder Adresse oder Koordinanten wie "53.155591, 8.234257"" -st 10 -L 'de'. Weitere Parameter sind optinal. Alternativ in die Datei /config/config.ini Parameter eintragen und Skript mit python runserver.py -se starten. Dort können auch Twitter API Daten für einen eigenen Twitterbot oder Pokemon eingetragen werden nach denen gesucht werden soll.
6. Browser starten und 127.0.0.1:5000 eintippen und bestätigen. Schon erscheint die PokemonGo Map und ihr erhaltet Tweets.
7. Fast-Start Option: config.ini mit username, passwort und location füllen und den richtigen Pfad zum Projekt in die runServer.bat eintragen. Über die .bat kann der Server dann gestartet werden.

## Ups. Etwas ist schief gegangen.
Sollte diese Fehlermeldung erscheinen stimmt etwas mit dem Google Maps API Key, den ich euch vererbt habe, nicht mehr. Einfach unten stehende Anleitung befolgen. Hinweis: Falls ihr das Skript über python runserver.py -st startet, muss der API Key auch in die config.ini eingetragen werden.
https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Google-Maps-API:-a-brief-guide-to-your-own-key



## Warnings

Die Funktionen des Skript sind gegen die Nutzungsbedingungen von Pokemon Go. Erstellt euch am besten einen neuen Pokemontrainerclub Account um das Programm zu nutzen.


## Contributing

Please submit all pull requests to [develop](https://github.com/AHAAAAAAA/PokemonGo-Map/tree/develop) branch.

Building off [Mila432](https://github.com/Mila432/Pokemon_Go_API)'s PokemonGo API, [tejado's additions](https://github.com/tejado/pokemongo-api-demo), [leegao's additions](https://github.com/leegao/pokemongo-api-demo/tree/simulation) and [Flask-GoogleMaps](https://github.com/rochacbruno/Flask-GoogleMaps).
