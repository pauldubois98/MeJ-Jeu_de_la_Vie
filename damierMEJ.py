from graphDamier import *

#classe principale
class damierMEJ(object):
    def __init__(self, boss=None, larg=500, haut=500, nblignes=10, \
                 nbcolonnes=10):
        #Paramètres généraux
        #largeur/hauteur
        self.larg=larg
        self.haut=haut
        #widget parent
        self.boss=boss
        #nombre de lignes & colonnes
        self.nbli=nblignes
        self.nbcol=nbcolonnes
        #lecture sans pause
        self.lecture=False
        ##Création d'un damier
        #initialisation a 0:
        self.damier=[[0 for i in range(nblignes)] for j in range(nbcolonnes)]
        
        #Graphique
        #initialisataion du damier graphique
        self.graph=graphDamier(boss=boss, larg=larg, haut=haut, \
                               nblignes=nblignes, nbcolonnes=nbcolonnes)

        ##Lien des évènements:
        self.graph.bind('<Button-1>', self.clicG)
        self.graph.bind('<Button-3>', self.clicD)


    #méthode pour parcourir le graph
    def parcours(self):
        nvxDamier=[[0 for i in range(self.nbli)] for j in range(self.nbcol)]
        for i in range(self.nbli):
            for j in range(self.nbcol):
                voisins=0
                for k in [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), \
                          (1,0), (1,1)]:
                    if (i+k[0])>=0 and (i+k[0])<self.nbli and \
                       (j+k[1])>=0 and (j+k[1])<self.nbcol:
                        voisins+=self.damier[i+k[0]][j+k[1]]
                if self.damier[i][j]:
                    if voisins==2 or voisins==3:
                        nvxDamier[i][j]=1
                        self.graph.color(i, j, 'black')
                    else:
                        nvxDamier[i][j]=0
                        self.graph.color(i, j, 'white')
                
                else:
                    if voisins==3:
                        nvxDamier[i][j]=1
                        self.graph.color(i, j, 'black')
        #sauvegarde des changements
        self.damier=nvxDamier

    #méthode pour afficher le damier
    def afficher(self):
        for i in range(0, self.nbli):
            for j in range(0, self.nbcol):
                if self.damier[i][j]:
                    self.graph.color(i, j, 'black')
                else:
                    self.graph.color(i, j, 'white')

    #méthode pour mettre toutes les cases en blanc
    def blanc(self, event=None):
        self.damier=[[0 for i in range(self.nbli)] for j in range(self.nbcol)]
        self.afficher()

    #méthode pour mettre toutes les cases en noir
    def noir(self, event=None):
        self.damier=[[1 for i in range(self.nbli)] for j in range(self.nbcol)]
        self.afficher()

    #méthode pour afficher les étapes sans pauses
    def play(self, event=None):
        self.parcours()
        if self.lecture:
            self.graph.after(500, self.play)

    #méthode d'ajout d'une case noire au clic (gauche)
    def clicG(self, event=None):
        if event!=None:
            #calcul de la case du damier conscernée
            i=int((event.y-(event.y%self.graph.pasl))/self.graph.pasl)
            j=int((event.x-(event.x%self.graph.pasc))/self.graph.pasc)
            #enregistrement
            self.damier[i][j]=1
            #affichage
            self.graph.color(i, j, 'black')

    #méthode d'ajout d'une case blanche au clic (droit)
    def clicD(self, event=None):
        if event!=None:
            #calcul de la case du damier conscernée
            i=int((event.y-(event.y%self.graph.pasl))/self.graph.pasl)
            j=int((event.x-(event.x%self.graph.pasc))/self.graph.pasc)
            #enregistrement
            self.damier[i][j]=0
            #affichage
            self.graph.color(i, j, 'white')

    def redim(self, nblignes=10, nbcolonnes=10, event=None):
        self.blanc()
        try:
            #enregistrement des valeurs
            self.nbli=int(nblignes)
            self.nbcol=int(nbcolonnes)
        except:
            print('Erreur')
        else:
            #enregistrement graphique
            self.graph.dim(nblignes=nblignes, nbcolonnes=nbcolonnes)
            #mise à jour du damier
            self.damier=[[0 for i in range(self.nbli)] \
                         for j in range(self.nbcol)]


#test si principal
if __name__=='__main__':
    root=Tk()
    root.title('Damier M.e.J. - Test')
    d=damierMEJ(root, 500, 500, 10, 10)
    d.graph.pack()
    Button(root, text='1 étape', command=d.parcours, bg='orange', fg='black', \
           activebackground='red').pack()
    root.mainloop()
