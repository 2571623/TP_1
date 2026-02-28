from shunting_yard import tokenize, infix_to_postfix, evaluate_postfix
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Shunting Yard")

tk.Label(fenetre, text="Entrez une expression :").pack()
entry = tk.Entry(fenetre)
entry.pack()

def calculer():
    expression = entry.get()
    try:
        tokens = tokenize(expression)
        postfix = infix_to_postfix(tokens)
        resultat = evaluate_postfix(postfix)
        tk.Label(fenetre, text=f"Résultat : {resultat}").pack()
    except ValueError as e:
        tk.Label(fenetre, text=f"Erreur : {e}").pack()
        