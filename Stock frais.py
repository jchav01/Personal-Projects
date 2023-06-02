# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:50:39 2023

@author: Jules
"""

from functions import *

# Création d'un objet


stock_a_zero1 = []
hist_ventes1 = []

yaourt = Produit("yaourt",35423, 10.0, 20.0, 4, 0, 0, 0, 1, 2, 0.75,
                 hist_ventes1,stock_a_zero1)

yaourt.afficher_informations()

stock_a_zero2 = []
hist_ventes2 = []

pizza = Produit("pizza",35421, 10.0, 20.0, 4, 0, 0, 0, 3, 3, 0.75,
                 hist_ventes2,stock_a_zero2)

pizza.afficher_informations()


#Creation d'un catalogue (articles en mag)

catalogue = []
catalogue.append(yaourt)
catalogue.append(pizza)


"""
##############################################################################
#test le simulateur by hand first

faire_commande(4,catalogue, livret_commandes)


reception_commande(livret_commandes, catalogue)

afficher_catalogue(catalogue)

vente(35423, 2, catalogue)
afficher_catalogue(catalogue)

vente(35423, 1, catalogue)
afficher_catalogue(catalogue)

perime(35423, 13, catalogue)
afficher_catalogue(catalogue)

afficher_hist_ventes(catalogue)

###############################################################################
"""
livret_init = [[35423, 4], [35421, 2] ]

magasin_virtuel(catalogue,livret_init)


    
