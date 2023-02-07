from tkinter import *
from tkinter import messagebox
import random
 
""" déclaration des éléments qui seront utilisé dans le code """
 
# text de fin
TextPerdant="Vous avez perdu voulez-vous rejouer?"
TextGagnant="Vous avez gagné voulez-vous rejour?"
 
# création d'un liste vide pour la disposition des mines
tableauMines = []
 
# nombre de lignes et de colonnes que contiendra le tableau
nb_col_Jeu = 10
nb_lgn_Jeu = 10
 
# création d'une variable qui servira à vérifier si tout les bouton (or mines) ont bien étais cliqué
nbclic =  0
 
# nombre de mine dans le tableau
nbMines = 12
 
 
 
""" création des fonctions utilisé """
 
# création d'un tableau avec le nombre de lignes et de colonnes défini précédemment et placement des mines
def CreeTerrainMine(nb_col_Jeu, nb_lgn_Jeu):
 
    """
        création du tableau exemple : [[0, 1, 2,]
                                       [0, 1, 2,]
                                       [0, 1, 2,]]
    """
    tableauMines = [[0 for colonne in range(nb_col_Jeu)]for ligne in range(nb_lgn_Jeu)]
 
    # création du liste vide qui va contenir l'emplacement des mines
    liste_mines=[]
 
    # boucle pour placer les mines dans le tableau
    print(nbMines)
    while len(liste_mines)<nbMines:
        # on prends un nombre aléatoire entre 0 et lignes X colonnes-1 puis on le mets dans la variable 'n'
        # lignes X colonnes-1 permet de savoir combien il y a des cases dans la tableau. On mets -1 à la fin car le tableau commence à 0
        n = random.randint(0,nb_lgn_Jeu*nb_col_Jeu-1)
 
        # on vérifie si 'n' pris précédemment n'a pas déjà été pris
        if not n in liste_mines:
            #on mets l'n' dans la liste des mines
            liste_mines.append(n)
 
            # on mets dans la variable 'ligne' le résultat d'un "floor division"
            # une "floor division" sert à faire la division de deux nombres et
            ligne = n//nb_lgn_Jeu
 
            # on mets dans la variable 'colonne' le résultat d'un "modulo"
            # un "modulo" c'est le reste de la division eclidienne
            """
                exemple de division eclidienne: 11 / 2 = 5 et il reste 1
            """
            colonne = n% nb_col_Jeu
 
            # grâce à ces variables on va pouvoir placer la mines dans la tableau. On va dire que une mine c'est tout les 9 du tableau
            tableauMines[ligne][colonne]=9
 
    # on parcourt les différentes lignes du tableau
    for ligne in range (nb_lgn_Jeu):
        # on parcourt les différentes colonnes du tableau
        for colonne in range (nb_col_Jeu):
            # vérifie si la cases est une mine
            if tableauMines[ligne][colonne]==9:
                # on parcourt les différentes lignes du tableau autour de la case
                for lgn in range(ligne-1,ligne+2):
                    # on parcourt les différentes colonnes du tableau autour de la case
                    for col in range(colonne-1,colonne+2):
                        # vérifie si 'lgn' et 'col' sont supérieur ou égale à 0
                        # vérifie si 'lgn' est inférieur à la longueur de la ligne
                        # vérifie si 'col' est inférieur à la longueur de la colone
                        # vérifie si la case voisine n'est pas une mine
                        if 0<=lgn<nb_lgn_Jeu and 0<=col<nb_col_Jeu and tableauMines[lgn][col]!=9:
                            # on ajoute 1 à case voisine
                            tableauMines[lgn][col]=tableauMines[lgn][col]+1
 
    # affichage du tableau en ligne de commande
    # for lgn in tableauMines:
    #     print(lgn)
 
    return tableauMines
 
# affichage du tableau pour que l'utilisateur puissent voir le terrain de jeu  
def bouton(can, tableauMines):
    # on parcourt les différentes lignes du tableau
    for nbRangee in range(nb_lgn_Jeu):
        # on parcourt les différentes colonnes du tableau
        for nbColonne in range(nb_col_Jeu):
            # affichage du bouton pour chaque cases du tableau
            carre = Button(can, text=tableauMines[nbRangee][nbColonne],height=3, width=6, fg="snow3",bg="snow3", activebackground="snow3",activeforeground="snow3")  
            carre.grid(row = nbRangee, column = nbColonne )
            # on envoie les informations du bouton cliqué par l'utilisateur à la fonction 'boutonClic()'
            carre.bind ("<Button-1>", boutonClic)
 
# récupère les information du bouton et on l'envoie à la fonction 'isMine'
def boutonClic(event):
    bouton = event.widget
    isMine(bouton)
   
# vérifie les informations du bouton pour savoir l'issue du jeu
def isMine(bouton):
    # permet de récupérer la valeur du bouton
    valeurBouton = bouton.cget("text")  
 
    # vérifie si le bouton cliqué est une mine
    if (valeurBouton == 9):
        # affichage du texte perdant
        print(TextPerdant)
        bouton.configure(fg="black",bg='red')
 
        # affiche un message à l'utilisateur
        MsgBox = messagebox.askquestion("résultat", message = TextPerdant)
        # si il clique sur yes
        if MsgBox == 'yes':
            # nouvelle partie
            jouerDemineur()
        else:
            # quitte la fenêtre
            fenetre.destroy()
 
    # si le bouton cliqué n'est pas un mine
    else:
        # permet de récupérer la couleur du texte du bouton
        couleurPolice = bouton.cget("fg")
 
        # si la couleur du bouton n'a pas changé
        if (couleurPolice == 'snow3'):
           
            # variable qui est utilisée à l'intérieur de la fonction est la même que celle qui est définie à l'extérieur de la fonction
            global nbclic
 
            # on ajoute 1 au nombre de clic
            nbclic += 1
 
            if (valeurBouton == 0):
                # change la couleur de la police et du fond du bouton
                # '#FFBA08' correspond a une teinte de couleur
                # divers teinte de couleur: https://coolors.co/palettes/trending
                bouton.configure(fg = "black",bg = '#FFBA08')
            elif (valeurBouton == 1):
                bouton.configure(fg = "black",bg = '#FAA307')
            elif (valeurBouton == 2):
                bouton.configure(fg = "black",bg = '#F48C06')
            elif (valeurBouton == 3):
                bouton.configure(fg = "black",bg = '#E85D04')
            else:
                bouton.configure(fg = "black",bg = '#DC2F02')
 
        # si toutes les cases sans mines sont cliquées
        if (nbclic == nbClicTotal):
           # affiche un message à l'utilisateur
            MsgBox = messagebox.askquestion("résultat", message = TextGagnant)
            # si il clique sur yes
            if MsgBox == 'yes':
                # nouvelle partie
                jouerDemineur()
            else:
                # quitte la fenêtre
                fenetre.destroy()
                 
# création du plateau de jeu
def jouerDemineur():
    # variable qui est utilisée à l'intérieur de la fonction est la même que celle qui est définie à l'extérieur de la fonction
    global nbclic
    global entry
    global entry2
    global nb_col_Jeu
    global nb_lgn_Jeu
    global nbMines
    global nbClicTotal
 
    # création d'une variable qui servira à vérifier si tout les bouton (or mines) ont bien étais cliqué
    nbclic =  0

    if entry.get() != '':
        nbMines = int(entry.get())

    if entry2.get() != '':
        nb_col_Jeu = int(entry2.get())
        nb_lgn_Jeu = int(entry2.get())

    # nombre de case qui ne contiennent pas de mines
    nbClicTotal = nb_col_Jeu * nb_lgn_Jeu - nbMines
   
    terrainMine = CreeTerrainMine(nb_col_Jeu, nb_lgn_Jeu)
    bouton(can,terrainMine)
 
   
if __name__ == "__main__":
    # création de le fenêtre grace au tkinter
    fenetre = Tk()
    fenetre.title("Jeu du démineur")
 
    #création de la zone graphique  
    can = Canvas(fenetre, width = 550, height = 550, bg = "white")
    can.pack(side = TOP, padx = 5, pady = 10)

    
    Label(fenetre, text="Entrez le nombre de mines", font=('Calibri 10')).pack()

    # entrez le nombre de mines
    entry= Entry(fenetre, width= 30)
    entry.pack(padx=5, pady=5)


    Label(fenetre, text="Entrez le nombre de lignes/colonnes", font=('Calibri 10')).pack()

    # entrez le nombre de colonne et de ligne
    entry2= Entry(fenetre, width= 30)
    entry2.pack()

    button = Button(fenetre, text="Nouvelle partie", command=jouerDemineur)
    button.pack(padx=5, pady=10)
   
    fenetre.mainloop()

