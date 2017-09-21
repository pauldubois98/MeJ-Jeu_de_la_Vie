from damierMEJ import *
from menuBar import *

class Simulateur(object):
    def __init__(self):
        ##Fenêtre mère
        self.root=Tk()
        #titre
        self.root.title("Damier de M.e.J.")
        self.root.resizable(0,0)

        ##Damier graphique
        self.graphDam=damierMEJ(self.root, larg=600, haut=600, nblignes=10, \
                         nbcolonnes=10)
        self.graphDam.graph.grid(row=1, column=1, columnspan=3)

        ##Bouttons
        #1  étape
        self.b1=Button(self.root, text='1 étape', command=self.graphDam.parcours,\
                  bg='orange', fg='black', activebackground='red')
        self.b1.grid(row=2, column=2)
        #tout blanc
        self.br=Button(self.root, text='Tout blanc', \
                       command=self.graphDam.blanc, bg='white', fg='black', \
                       activebackground='grey')
        self.br.grid(row=2, column=1, sticky='w')
        #tout noir
        self.bn=Button(self.root, text='Tout noir', \
                       command=self.graphDam.noir, fg='white', bg='black', \
                       activebackground='grey')
        self.bn.grid(row=2, column=3, sticky='e')
        #affichage:
        self.llect=Label(self.root, text='  Etapes sans pauses: OFF', \
                         bg="light blue")
        self.llect.grid(row=3, column=1, sticky='w', pady=1)
        #début de lecture
        self.bd=Button(self.root, text='Début', \
                       command=self.start, bg='light green', \
                       fg='black', activebackground='green')
        self.bd.grid(row=3, column=1, sticky='e')
        #fin de lecture
        self.bf=Button(self.root, text='Fin', \
                       command=self.stop, bg='pink', \
                       fg='black', activebackground='red')
        self.bf.grid(row=3, column=2, sticky='w')
        

        ##Barre de menu
        self.menu=menuAppli(self.root, self.graphDam.blanc, \
                            self.options, self.regles, self.notice, self.about)

        ##Evenements
        #redimentionnement fenetre
        self.redimFen=0
        self.root.bind('<Control_L>', self.redimFen0)



        #initialisation du damier:
        for i in [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), \
                  (8,8), (9,9), (0,9), (1,8), (2,7), (3,6), (4,5), (5,4), \
                  (6,3), (7,2), (8,1), (9,0)]:
            self.graphDam.damier[0+i[0]][0+i[1]]=1
        #affichage
        self.graphDam.afficher()


        #mainloop
        self.root.mainloop()




    def redimFen0(self, evt=None):
        if self.redimFen:
            self.root.unbind('<Configure>')
            self.redimFen=0
            print('0')
            print(self.root.geometry)
            
        else:
            self.root.bind('<Configure>', self.redimFen)
            self.redimFen=1
            print('1')
    def redimFen(self, evt=None):
        cote=min(evt.height-53, evt.width-4)
        print(cote, evt.height, evt.width)
        self.graphDam.graph.dim(larg=cote, haut=cote)

    def entr(self, event=None):
        ch=self.entrO.get()
        try:
            nb=int(ch)
        except:
            self.entrO.config(bg='red')
        else:
            if nb>0:
                self.entrO.config(bg='white')
                self.graphDam.redim(nb, nb)


    def start(self, event=None):
        self.graphDam.lecture=True
        self.graphDam.play()
        self.llect.config(text="  Etapes sans pauses: ON ")

    def stop(self, event=None):
        self.graphDam.lecture=False
        self.llect.config(text="  Etapes sans pauses: OFF")


    def options(self, event=None):
        ##Fenêtre (Toplevel)
        fenOptions=Toplevel(bg='white')
        fenOptions.title('Damier M.e.J. - Réglages')
        fenOptions.geometry('260x100')
        #choix de la taille
        Label(fenOptions, bg='white', text='Côté du damier (en cases):', \
              fg='black').grid(row=1)
        self.entrO=Entry(fenOptions)
        self.entrO.grid(row=2)
        self.entrO.bind('<Return>', self.entr)
        #taille par défault
        Button(fenOptions, bg='purple', text='Damier en 10*10', fg='black', \
               activebackground ='purple', activeforeground ='white', \
               command=lambda: self.graphDam.redim(10, 10))\
               .grid(row=3, padx=25, pady=25)
        

    def regles(self, event=None):
        fenRegles=Toplevel(bg='white')
        fenRegles.title('Damier M.e.J. - Règles')
        Label(fenRegles, text="""\
        Le jeu de la vie se présente sous la forme d'un univers à deux \n\
dimensions (une grille). Chaque cellule occupe une zone délimitée \n\
de cet univers (une case).\n\
        En plus de cette univers à deux dimension, nous ajoutons la \n\
dimension du temps. Celui-ci est découpé en pulsations. A chaque \n\
pulsation, le programe calcule la nouvelle configuration des cellules \n\
dans l'univers.\n\
\n\n\
        Chaque cellule est régie par trois règles simples:\n\
-Une cellule morte entourée d'exactement 3 cellules vivantes naît.\n\
-Une cellule vivante entourée de 2 ou 3 cellules vivantes reste en vie.\n\
-Dans les autres cas, la cellule meure.\n\n\
    ->On peut donc considérer qu'une cellule naît de l'entourage de \n\
congénères et que sa mort est due à l'isolement."""\
              , bg='white', justify=LEFT).pack()
        

    def notice(self, event=None):
        fenRegles=Toplevel(bg='white')
        fenRegles.title("Damier M.e.J. - Notice d'utilisation")
        Label(fenRegles, text="""        Utilisation du simulateur:""", \
              bg='white', fg='red', justify=LEFT).pack()
        Label(fenRegles, text="""\
    >Fenêtre principale:\n\
-Un clic gauche colorie la case en NOIR.\n\
-Un clic droit colorie la case en BLANC.\n\
-Le bouton "1 étape" calcule et afficfe la génération sivante.\n\
-Les boutons 'Début" et "Fin" affichent les générations sans pauses\n\
les unes entre les autres.\n\
-Les boutons "Tout blanc" et "Tout noir" colorient respectivement\n\
toutes les cases en BLANC et NOIR.\n\n\
    >Fenêtre d'options:\n\
-Le champs d'entrée permet de redimentionner le nombre de cases \n\
par côtés de la grille.\n\
-Le bouton "Damier en 10*10" permet de revenir au damier initial de \n\
10 cases par 10."""\
              , bg='white', justify=LEFT).pack()
        



    def about(self, event=None):
        fenAbout=Toplevel(bg='black')
        fenAbout.title('Damier M.e.J. - About...')
        Label(fenAbout, text="""Damier M.e.J.\n\
Cette aplication créée pour le club Math-en-Jean\n\
simule le 'Jeu de la vie'.\n\
\n\
En savoir plus sur le club sur:\n\
http://www.mathenjeans.fr/\n\
\n\
======Développé en septembre 2015=======\n\
Pour le club M.e.J. 2015\n\
Lycée Jean Pierre Vernant (PINS-JUSTARET, 31)""", bg='black', fg='white', \
        justify=LEFT).pack()






#test si principal
if __name__=='__main__':
    S=Simulateur()


