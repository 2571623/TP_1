from shunting_yard import tokenize, infix_to_postfix, evaluate_postfix
import tkinter as tk

def calculer():
    expression = entry.get()

    # On vide les 3 champs avant chaque calcul
    for champ in [text_postfix, text_resultat, text_erreur]:
        champ.config(state="normal")
        champ.delete("1.0", tk.END)
    
    try:
        tokens = tokenize(expression)
        postfix = infix_to_postfix(tokens)
        resultat = evaluate_postfix(postfix)

        text_postfix.insert("1.0", " ".join(postfix))
        text_resultat.insert("1.0", resultat)

    except Exception as e:
        text_erreur.insert("1.0", str(e))

    for champ in (text_postfix, text_resultat, text_erreur):
        champ.config(state="disabled")
    
fenetre = tk.Tk()
fenetre.title("Calculatrice Shunting Yard")

tk.Label(fenetre, text="Expression Infixe:").pack()
entry = tk.Entry(fenetre)
entry.pack()

tk.Button(fenetre, text="Convertir", command=calculer).pack()

tk.Label(fenetre, text="Expression postfixée:").pack()
text_postfix  = tk.Text(fenetre, height=4, width=100)
text_postfix.pack()

tk.Label(fenetre, text="Résultat:").pack()
text_resultat = tk.Text(fenetre, height=4, width=100)  
text_resultat.pack()

tk.Label(fenetre, text="Erreur:").pack()
text_erreur   = tk.Text(fenetre, height=5, width=100)  
text_erreur.pack()

fenetre.mainloop()


