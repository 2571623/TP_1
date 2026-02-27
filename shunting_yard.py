def tokenize(expression: str) -> list[str]:
    tokens = []
    i = 0
    
    while i < len(expression):
        if expression[i] == "":
            i += 1
            continue 
        elif expression[i].isdigit() or expression[i] == ".":

            """ isdigit retourne True pour les chiffres de 0 à 9, donc ça permet de continuer 
            pour le "." c'est permet de continuer s'il voit un point comme 3.14 """

            start = i  # mémorise la position où le nombre commence dans la chaîne
            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                i += 1
            tokens.append(expression[start:i])

        else:
            tokens.append(expression[i])
            i += 1

    return tokens
    
def infix_to_postfix(tokens: list[str]) -> list[str]:
    wewe


def evaluate_postfix(tokens: list[str]) -> float:
    wdw