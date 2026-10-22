def calcule(num1, operator, num2):
    """Retourne le résultat de num1 <operator> num2.
 
    Opérateurs supportés : +, -, *, /, %
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Erreur : division par zéro impossible"
        return num1 / num2
    elif operator == "%":
        if num2 == 0:
            return "Erreur : modulo par zéro impossible"
        return num1 % num2
    else:
        return "Erreur : opérateur invalide"