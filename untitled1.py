# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 09:24:16 2021

@author: Mohamed
"""
import datetime as date
from typing import AsyncGenerator

def calcul_de_salaire(sh,nh):
    if nh<160:
        return sh*nh
    elif nh>=160 and nh<200:
        return ((160*sh) + (1.25*(nh - 160)*sh))
    else:
        return ((160*sh) + (1.5*(nh - 160)*sh))

def reconnaissance_de_caracteres(cal):
    if ord(cal)>=65 and ord(cal)<= 90:
        print("Il s'agit d'une lettre majuscule")
    elif ord(cal)>=97 and ord(cal)<= 122:
        print("Il s'agit d'une lettre minuscule")
    elif ord(cal)>=48 and ord(cal)<= 57:
        print("Il s'agit d'un chiffre")
    else:
        print("Il s'agit d'un caractére")

def impots(x):
    s=input("etes vous un h ou une f: ")
    if x>20 and ord(s)==104:
        print("vous etes imposable")
    elif x>18 and x<35 and ord(s)==102:
        print("vous etes imposable")
    else:
        print("vous n'etes pas imposable")

def reprographie():
    nb=int(input("quel est le nombre de photographies effectuées: "))
    if nb<=10:
        print("votre facture est",nb*0.10)
    elif nb>10 and nb<=30:
        print("votre facture est",(10*0.10)+(nb-10)*0.09)
    else:
        print("votre facture est",(10*0.10)+(20*0.09)+(nb-30)*0.08)
            
        
def calcul_de_frais_portuaires():
    nom=input("le nom du voilier: ")
    longueur=int(input("la longueur du voilier: "))
    categorie=int(input("la catégorie du voilier: "))
    if longueur<5:
        print("le cout mensuel est 100 euros")
        cm=100
    elif longueur>=5 and longueur<=10:
        print("le cout mensuel est 200 euros")
        cm=200
    elif longueur>10 and longueur<=12:
        print("le cout mensuel est 400 euros")
        cm=400
    else:
        print("le cout mensuel est 600 euros")
        cm=600
    if categorie==1:
        print("la taxe spéciale anneulle est 100 euros")
        tsa=100
    elif categorie==2:
        print("la taxe spéciale anneulle est 150 euros")
        tsa=150
    else:
        print("la taxe spéciale anneulle est 250 euros")
        tsa=250
    ca=cm+tsa
    print("le cout annuel d'une place au port pour le voilier",nom,"est de",ca,"euros.")
    
def calcul_frais_mensuel_vehicule():
    NLCS2000KM = 10
    NLCI2000KM = 8
    FD = 1.70
    FE = 1.50
    NKD = 100
    NKCA = int(input("Combien de kilometre parcourez vous en une année ? "))
    typeCa = input("Quel type de carburant disposez vous ? (E essence, D diesel)")
    CyV = int(input("quel est la taille de la voiture ?"))
    couCa = float(input("Prix du carburant ? "))
    NKCM = NKCA/12
    if(typeCa == "E"):
        if(CyV >= 2000):
            nbLitres = (NKCM/NKD)*NLCS2000KM
            CM = nbLitres*couCa*FE
        elif(CyV < 2000):
            nbLitres = (NKCM/NKD)*NLCI2000KM
            CM = nbLitres*couCa*FE
    elif(typeCa == "D"):
        nbLitres = (NKCM/NKD)* NLCI2000KM
        CM = nbLitres*couCa*FD
    return  CM + "euros"

def election():
    nbC = 4
    ScoCa = list(map(float,input("Entrez le score des candidats(separer d'espaces)").split(" ")))
    i=1
    prC = ScoCa[0]
    CST = []
    nbCST = 0
    canPlusDe50 = False
    premierCanF = True
    
    if(prC>=50):
        return "Candidat Elu"
    if(prC < 12.5):
        return "candidat battut"
    while(i<nbC):
        if(ScoCa[i]>=50):
            canPlusDe50 = True
            return "Candidat Battut"
        
        
        if(ScoCa[i] > 12.5):
            CST.append(ScoCa[i])
        i+=1
    nbCST = len(CST)
    i = 1
    
    while(i < nbCST):
        if(prC < CST[i]):
            premierCanF = False
        i+=1

    if( premierCanF):
        return "le candidat est en balotage favorable"
    
    return "le candidat est en balotage defavorable"



def saisieDonnees():
    AMPermis = 2
    age = int(input("Quel age avez vous ? "))
    AOPermis = int(input("En quel annee avez vous obtenue votre permis"))
    accident = input("Avez vous deja eu des accidents taper O(oui), N(non)")
    nbAcc = 0
    TPermis = 0
    tarif = ("Refus","Bleu","Vert","Orange","Rouge")
    if(accident == "O"):
        nbAcc = int(input("Combien d'accident? "))
    TPermis = date.date.today().year - AOPermis
    
    if(age<25):
        if(TPermis<AMPermis):
            if(nbAcc == 0):
                TaDe = tarif[4]
            else:
                TaDe = tarif[0]
        elif(TPermis>AMPermis):
            if(nbAcc == 0):
                TaDe = tarif[3]
            elif(nbAcc == 1):
                TaDe = tarif[4]
            else:
                TaDe = tarif[0]
    elif(age>25):
        if(TPermis<AMPermis):
            if(nbAcc == 0):
                    TaDe = tarif[3]
            elif(nbAcc == 1):
                TaDe = tarif[4]  
            else:
                TaDe = tarif[0] 
        else:
            if(nbAcc ==0):
                TaDe = tarif[2]
            elif(nbAcc == 1):
                TaDe = tarif[3]
            elif (nbAcc == 2):
                TaDe = tarif[4]
            else:
                TaDe = tarif[0]
    return TaDe    
               
        
cal="_"
age=50
reconnaissance_de_caracteres(cal)
impots(age)
reprographie()
calcul_de_frais_portuaires()
print(calcul_frais_mensuel_vehicule())
print(election())
print(saisieDonnees())
    