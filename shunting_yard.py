def tokenize(expression: str) -> list[str]:
    tokens = []
    i = 0
    
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue 
        elif expression[i].isdigit() or expression[i] == ".":

            """ isdigit retourne True pour les chiffres de 0 à 9, donc ça permet de continuer 
            pour le "." c'est permet de continuer s'il voit un point comme 3.14 """

            start = i  # mémorise la position où le nombre commence dans la chaîne
            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                i += 1
            nombre = (expression[start:i])
            if nombre.count(".") > 1:
                raise ValueError("Nombre mal formé : {nombre")
            tokens.append(nombre)
        elif expression[i] in "+-*/()": 
            tokens.append(expression[i])
            i += 1

        else:
            raise ValueError(f"Opérateur inconnu : {expression[i]}")

    return tokens
    
def infix_to_postfix(tokens: list[str]) -> list[str]:
    
    priorite = {'+': 1, '-': 1, '*': 2, '/': 2}

    output = []
    stack_operateur = []

    for token in tokens:
        if token not in "+-*/()":
            output.append(token)

        elif token in "+-*/":
            while (stack_operateur and stack_operateur[-1] in priorite and priorite[stack_operateur[-1]] >= priorite[token]):
                output.append(stack_operateur.pop())

            stack_operateur.append(token)

        elif token =="(":
            stack_operateur.append(token)

        elif token == ")":
            while stack_operateur and stack_operateur[-1] != "(":
                output.append(stack_operateur.pop())
            if not stack_operateur:
                raise ValueError("Parenthèses non appariées : ) sans (")
            stack_operateur.pop()  # Retire la parenthèse ouvrante

    while stack_operateur:
        if stack_operateur[-1] in "()":
            raise ValueError("Parenthèses non appariées : ( sans )")
        output.append(stack_operateur.pop())
    return output

def evaluate_postfix(tokens: list[str]) -> float:
    
    stack: list[float] = []
    for token in tokens:
        if token in ("+", "-", "*", "/"):
            if len(stack) < 2:
                raise ValueError(f"Expression invalide : pas assez d'opérandes pour '{token}'")
            
            b = stack.pop()  
            a = stack.pop()  
            
            if token == "+":
                resultat = a + b
            elif token == "-":
                resultat = a - b
            elif token == "*":
                resultat = a * b
            else:
                if b == 0:
                    raise ZeroDivisionError("Division par zéro")
                resultat = a / b
            
            stack.append(resultat)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Token invalide : '{token}'")
    
    # Vérification finale : la pile doit contenir exactement 1 valeur
    if len(stack) != 1:
        raise ValueError("Expression postfix mal formée")
    
    return stack[0]