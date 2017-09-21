from tkinter import *

class graphDamier(Canvas):
    """Fenetre permetant de créer des graphiques de damiers facilement"""
    def __init__(self, boss=None, larg=500, haut=500, nblignes=10, \
                 nbcolonnes=10):
        "Construction du damier... \n\
/!\: le damier est une liste de liste \n\
/!\: les coordonés du damier sont en [ligne][colonnes]"
        #initialisation du canvas
        Canvas.__init__(self, boss)
        #configuration
        self.configure(width=larg, height=haut, bg='white')
        #Paramètres généraux
        #largeur/hauteur
        self.larg=larg
        self.haut=haut
        #widget parent
        self.boss=boss
        #nombre de lignes & colonnes
        self.nbli=nblignes
        self.nbcol=nbcolonnes
        #nombre de pixels par lignes & colonnes
        self.pasl=haut/self.nbli
        self.pasc=larg/self.nbcol
        
    def color(self, ligne, colonne, couleur):
        "Coloration d'une case du damier"
        x0=int(colonne*self.pasc)
        x1=int((colonne+1)*self.pasc)
        y0=int(ligne*self.pasl)
        y1=int((ligne+1)*self.pasl)
        self.create_rectangle(x0, y0, x1, y1, width=0, fill=couleur)

    def dim(self, larg=None, haut=None, nblignes=None, nbcolonnes=None):
        #Paramètres généraux
        #largeur/hauteur
        if larg!=None:
            self.larg=larg
        if haut!=None:
            self.haut=haut
        #configuration
        self.configure(width=self.larg, height=self.haut, bg='white')
        #nombre de lignes & colonnes
        if nblignes!=None:
            self.nbli=nblignes
        if nbcolonnes!=None:
            self.nbcol=nbcolonnes
        #nombre de pixels par lignes & colonnes
        self.pasl=self.haut/self.nbli
        self.pasc=self.larg/self.nbcol

if __name__=='__main__':
    root=Tk()
    root.title("Damier - Exemple")
    damier=graphDamier(root)
    damier.pack()
    for i in range(10):
        damier.color(i,i,'red')
    root.mainloop()
