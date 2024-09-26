#### Fonction secondaire
"""
Un palindrome est un mot ou une phrase qui se lit de droite à gauche et de gauche à droite. 
L'objectif est d'écrire du code qui permet de vérifier si une chaine de caractère est un palindrome.
"""

def ispalindrome(p):

    # votre code ici
    """
    verifie si une chaine de caractere est un palindrome.

    args:
        p (str): la chaine de caractere a verifier.

    returns:
       bool: True si la chaine de caractere est un palindrome.

    """
    for i in range(1,len(p)//2):
        if p[i-1]!=p[-i]:
            return False
    return True

#### Fonction principale


def main():
    """
    Fonction principale qui teste la fonction ispalindrome() avec plusieurs exemples.
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()