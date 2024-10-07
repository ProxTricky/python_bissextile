def is_leap_year(year):
    """
    Vérifie si l'année est bissextile.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def leap_year_in_period(start_year, end_year):
    """
    Retourne une liste contenant toutes les années
    bissextiles entre deux années données.
    """
    leap_year = []
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_year.append(year)
    return leap_year


def menu():
    """
    Affiche le menu permettant de choisir entre plusieurs options :
    1. Vérifier si une année est bissextile
    2. Trouver toutes les années bissextiles dans une période donnée
    3. Quitter le script
    """
    while True:
        print("Choisissez une option :")
        print("1. Vérifier si une année est bissextile")
        print("2. Trouver toutes les années bissextiles dans une période")
        print("3. Quitter")

        choix = input("Entrez votre choix (1, 2 ou 3) : ")

        if choix == "1":
            year = int(input("Entrez une année : "))
            if is_leap_year(year):
                print(f"{year} est une année bissextile.")
            else:
                print(f"{year} n'est pas une année bissextile.")
        elif choix == "2":
            start_year = int(input("Entrez l'année de début : "))
            end_year = int(input("Entrez l'année de fin : "))
            leap_year = leap_year_in_period(start_year, end_year)
            if leap_year:
                print(f"Année(s) bissextiles entre {start_year} et {end_year} : {leap_year}")
            else:
                print(f"Il n'y a pas d'années bissextiles entre {start_year} et {end_year}.")
        elif choix == "3":
            print("Fermeture du script.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    menu()