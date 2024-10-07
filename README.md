
# Année bissextile checker

Ce script Python permet de vérifier si une année est bissextile et de trouver toutes les années bissextiles dans une période donnée.
Fonctionnalités

    Vérifier si une année est bissextile : Vous pouvez entrer une année spécifique pour savoir si elle est bissextile.
    Trouver toutes les années bissextiles dans une période : Entrez une année de début et une année de fin pour obtenir une liste des années bissextiles dans cette période.
    Quitter : Permet de fermer le programme.

## Utilisation

Exécutez le script en utilisant Python :

    python script_bissextile.py

Un menu vous permettra de choisir entre les options suivantes :

    Vérifier si une année est bissextile : Entrez une année pour vérifier si elle est bissextile.
    Trouver toutes les années bissextiles dans une période : Entrez une année de début et de fin pour lister toutes les années bissextiles dans cette plage.
    Quitter : Ferme le programme.

Pour se faire il vous suffit de rentrer le numéro correspondant à votre choix : 

    Choisissez une option :
        1. Vérifier si une année est bissextile
        2. Trouver toutes les années bissextiles dans une période
        3. Quitter
    Entrez votre choix (1, 2 ou 3) : 
## Exemple

    Vérification d'une année bissextile :
        Si vous entrez l'année 2024, le programme vous indiquera que 2024 est une année bissextile.

    Trouver des années bissextiles dans une période :
        Si vous entrez la période de 2000 à 2020, le programme retournera : [2000, 2004, 2008, 2012, 2016, 2020].
## Structure des fonctions

    is_leap_year(year): Vérifie si une année donnée est bissextile.

    leap_year_in_period(start_year, end_year): Retourne une liste d'années bissextiles entre deux années.

    menu(): Affiche le menu principal pour choisir entre les différentes options.