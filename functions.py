# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:25:25 2023

@author: Jules
"""
import numpy as np
import math
from Affichage import *

"""
Ce fichier regroupe les fonctions nécéssaires pour simuler un magasin ,
ainsi que les fonctions nécessaires à automatiser les commandes
"""

###############################################################################
#Mises à jour 
###############################################################################


def maj_vente_moy(catalogue):
    
    for i in range(len(catalogue)):
        m = len(catalogue[i].hist_ventes)
        ventes_moy = 0
        days = 0
        ones = [0]*m
        
        for j in range(m):
            ones[j] = 1 - catalogue[i].stock_a_zero[j]
        
        for j in range(m):
            days += ones[j]
        
        for j in range(m):
            ventes_moy += ones[j]*catalogue[i].hist_ventes[j]
        
        catalogue[i].ventes_moy = ventes_moy / days
    

def maj_ecart_type(catalogue):

    for i in range(len(catalogue)):
        
        sum = 0
        m = len(catalogue[i].hist_ventes)
        for j in range(len(catalogue[i].hist_ventes)):
            
            sum += (catalogue[i].hist_ventes[j] - catalogue[i].ventes_moy)**2
            sum = math.sqrt(sum/m)
            
        catalogue[i].ecart_type = sum

def mise_a_jour_stock_secu(catalogue):
    
    for i in range(len(catalogue)):
        
        rac_n = math.sqrt(len(catalogue[i].hist_ventes))
        catalogue[i].stock_secu = round(1.96 * catalogue[i].ecart_type / rac_n)
        
def maj_params(catalogue):
    
    maj_vente_moy(catalogue)
    #maj_ecart_type(catalogue)
    #mise_a_jour_stock_secu(catalogue)       
        
        

###############################################################################
#COMMANDES
###############################################################################


def reception_commande(livret_commandes, catalogue):
    #Commande est une liste de tuples (numero_produit, nb_lots)
    
    for j in range(len(livret_commandes)):
        
        # Recherche de l'objet dans le catalogue
        for i in range(len(catalogue)) :
            if catalogue[i].numero == livret_commandes[j][0]:
               
                catalogue[i].stock += livret_commandes[j][1]
                

    

    
def modifier_livret(livret, catalogue):
    
    #On parcours le livret
    for j in range(len(livret)):
        
        # On matche avec le catalogue
        for i in range(len(catalogue)) :
            if catalogue[i].numero == livret[j][0]:
                
                #On determine s'il y a besoin de commander
                
                cmd = round((catalogue[i].ventes_moy * 7)) - catalogue[i].stock + catalogue[i].stock_secu
                
                if cmd > 0:
               
                    livret[j][1] = cmd
        

###############################################################################
#VENTES
###############################################################################

#fonction qui modifie les infos du magasin lors d'une vente
def vente(num_produit, nb, catalogue):
    
    # Recherche de l'objet dans le catalogue
    for i in range(len(catalogue)) :
        if catalogue[i].numero == num_produit:
    
            # retirer le nb de produits vendus du stock, et update la value du produit
            catalogue[i].stock -= nb
            catalogue[i].hist_ventes += [nb]
            
            
#fonction qui retire du stock le nb de périmés
def perime(num_produit, nb, catalogue):
    # Recherche de l'objet dans le catalogue
    for i in range(len(catalogue)) :
        if catalogue[i].numero == num_produit:
           
            # retirer le nb de produits vendus du stock, et update la value du produit
            catalogue[i].stock -= nb
            catalogue[i].perime += nb
            catalogue[i].value -= nb * catalogue[i].prix_achat

def clear_hist(catalogue):
    
    for i in range(len(catalogue)):
        
        catalogue[i].hist_ventes = []
        catalogue[i].stock_a_zero = []
  
###############################################################################
#MAGASIN VIRTUEL
###############################################################################        


def magasin_virtuel(catalogue, livret_init):
    
    livret = livret_init

    for l in range(7):
    
        reception_commande(livret, catalogue)
        afficher_stocks(catalogue)
        
        for i in range(7):
            
            for j in range(len(catalogue)):
                
                if catalogue[j].stock > 0:
                    
                    k = np.random.normal(catalogue[j].ventes_moy, catalogue[j].ecart_type)
                    
                    if k < 0 : 
                        k = 0
                    else :
                        k = round(k)
                    
                    if k > catalogue[j].stock:
                        k = catalogue[j].stock
                    
                    if catalogue[j].stock == 0:
                        catalogue[j].stock_a_zero += [1]
                    else:
                        catalogue[j].stock_a_zero += [0]
                        
                    vente(catalogue[j].numero, k, catalogue)
                
            
        afficher_hist_ventes(catalogue)
        afficher_stocks(catalogue)
        print("\n")
        maj_params(catalogue)
        modifier_livret(livret, catalogue)
     #  clear_hist(catalogue)
        
        
        
        print("\n")

    
   
          
        