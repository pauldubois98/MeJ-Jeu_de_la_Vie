#importation
from tkinter import *

#classe barre de menu type pour un jeu
class menuAppli(Menu):
    def __init__(self, boss=None, commandNouvSimu=None, commandOptions=None, \
                 commandRegles=None, commandNotice=None, commandAbout=None, \
                 labJeu1="Nouvelle simulation       F2", \
                 labJeu2="Options                      Alt+O", \
                 labJeu3="Fermer", \
                 labJeu4="Quitter                      Ctrl+Q", \
                 labAide1="Règles de simulation", \
                 labAide2="Notice d'utilisation", \
                 labAide3="About..."):
        ###VARIABLES
        self.commandNouvSimu=commandNouvSimu
        self.commandOptions=commandOptions
        self.boss=boss
        
        ###MENUS
        self.barreMenu=Menu(boss)
        #Menu du simulateur
        self.menuJeu=Menu(self.barreMenu, tearoff=0)
        #bouton pour commencer
        self.menuJeu.add_command(label=labJeu1, activebackground='light green',\
                            activeforeground='black', command=commandNouvSimu)
        #bouton d'options
        self.menuJeu.add_command(label=labJeu2, \
                            activebackground='purple', command=commandOptions)
        #bouton pour fermer le menu
        self.menuJeu.add_command(label=labJeu3, activebackground='orange')
        #séparateur
        self.menuJeu.add_separator()
        #bouton pour quitter le simulateur
        self.menuJeu.add_command(label=labJeu4, \
                            activebackground='red', command=boss.destroy)
        self.barreMenu.add_cascade(label="Simulateur", menu=self.menuJeu)
        #Menu d'aide
        self.menuAide=Menu(self.barreMenu, tearoff=0)
        #bouton pour afficher les règles de simulation
        self.menuAide.add_command(label=labAide1,
                             activebackground='dark grey', \
                             activeforeground='black', command=commandRegles)
        #bouton pour afficher les règles du simulateur
        self.menuAide.add_command(label=labAide2,
                             activebackground='grey30', \
                             activeforeground='black', command=commandNotice)
        #bouton pour avoir des infos sur le dévellopeur, ses autres jeux...
        self.menuAide.add_command(label=labAide3, activebackground='black', \
                             command=commandAbout)
        self.barreMenu.add_cascade(label="Aide", menu=self.menuAide)
        boss.config(menu=self.barreMenu)
        
        ###RACCOURCITS
        boss.bind("<F2>", self.racourcit1)
        boss.bind("<Control-q>", self.racourcit2)
        boss.bind("<Alt-o>", self.racourcit3)

    #raccourcits:
    def racourcit1(self, event):
        self.commandNouvSimu()
    def racourcit2(self, event):
        self.boss.destroy()
    def racourcit3(self, event):
        self.commandOptions()

if __name__=='__main__':
    def nouv():
        print('Nouvelle Simulation')
    def options():
        print('Options')
    fen=Tk()
    M=menuAppli(fen, nouv, options)
    fen.mainloop()
