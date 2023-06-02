# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:53:35 2023

@author: Jules
"""

###############################################################################
#PRODUITS
###############################################################################

class Produit:
    def __init__(self, nom, numero, prix_achat, prix_vente,
                 lot, stock, value, perime, ventes_moy, stock_secu, ecart_type,
                 hist_ventes, stock_a_zero):
        self.nom = nom
        self.numero = numero
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.lot = lot
        self.stock = stock
        self.value = value
        self.perime = perime
        self.ventes_moy = ventes_moy
        self.stock_secu = stock_secu
        self.ecart_type = ecart_type
        self.hist_ventes = hist_ventes
        self.stock_a_zero = stock_a_zero
        
        

    def afficher_informations(self):
        print(f"Nom: {self.nom}")
        print(f"numero : {self.numero}")
        print(f"Prix d'achat: {self.prix_achat}")
        print(f"Prix de vente: {self.prix_vente}")
        print(f"Taille d'un lot: {self.lot}")
        print(f"Stock: {self.stock}")
        print(f"value: {self.value}")
        print("\n")
        
        
###############################################################################
#AFFICHAGE
###############################################################################
        
#Afficher le catalogue, avec les infos produits 
def afficher_catalogue(catalogue):
    
    for i in range(len(catalogue)):
        catalogue[i].afficher_informations()
  
#Afficher l'historique des ventes        
def afficher_hist_ventes(catalogue):
    
    for i in range(len(catalogue)):
        print("ventes de",catalogue[i].nom, " : ", catalogue[i].hist_ventes[-7:])
        
def afficher_stocks(catalogue):
    for i in range(len(catalogue)):
        print("stock de",catalogue[i].nom, " : ", catalogue[i].stock)