# MeJ-Jeu_de_la_Vie
Codage du jeu de la vie pour le club Maths.en.Jean 2015/2016 au Lycée Jean Pierre Vernant (PINS-JUSTARET, 31)
En savoir plus sur le club sur: http://www.mathenjeans.fr/

-------------------

Cette application python (utilisant la biliothèque graphique tkinter) simule le 'Jeu de la vie'

Le jeu de la vie se présente sous la forme d'un univers à deux dimensions (une grille). Chaque cellule occupe une zone délimitée \n\
de cet univers (une case).
En plus de cette univers à deux dimension, nous ajoutons la dimension du temps. Celui-ci est découpé en pulsations. A chaque pulsation, le programe calcule la nouvelle configuration des cellules dans l'univers.
        
        Chaque cellule est régie par trois règles simples:
-Une cellule morte entourée d'exactement 3 cellules vivantes naît.
-Une cellule vivante entourée de 2 ou 3 cellules vivantes reste en vie.
-Dans les autres cas, la cellule meure.
    ->On peut donc considérer qu'une cellule naît de l'entourage de congénères et que sa mort est due à l'isolement.

