import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction à compléter 3
class AppFctComp1Partie1(QDialog):

    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_1.ui", self)
        self.data = data

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):
        # TODO 1.1 : fonction à modifier pour remplacer la zone de saisie par une liste de valeurs prédéfinies
        #  dans l'interface une fois le fichier ui correspondant mis à jour
        display.refreshLabel(self.ui.label_fct_comp_1, "")
        if(self.Femmes.isChecked()):
            sexe = "'feminin'"
        if(self.Hommes.isChecked()):
            sexe = "'masculin'"
        if(self.Mixtes.isChecked()):
            sexe = "'mixte'"
        try:
            cursor = self.data.cursor()
            commande = "SELECT numEp, nomEp, formeEp, nomDi, categorieEp, nbSportifsEp, strftime(""'%Y-%m-%d',dateEp,'unixepoch') FROM V0_LesEpreuves WHERE categorieEp = "+sexe
            result = cursor.execute(commande)
            #nb = cursor.execute("SELECT COUNT (numEp) as nombre, nomDi FROM V0_LesEpreuves WHERE categorieEp = "+sexe+" GROUP BY nomDi")
            #display.refreshLabel(self.ui.affichage_taille,"lignes affichées")
        except Exception as e:
            self.ui.table_fct_comp_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_1, "Impossible d'afficher les résultats : " + repr(e))
        else:
            i = display.refreshGenericData(self.ui.table_fct_comp_1, result)
            if i == 0:
                display.refreshLabel(self.ui.label_fct_comp_1, "Aucun résultat")