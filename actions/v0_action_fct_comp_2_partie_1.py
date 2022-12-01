import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction à compléter 4
class AppFctComp2Partie1(QDialog):

    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_2.ui", self)
        self.data = data
        self.refreshCategories()

    # Fonction de mise à jour de l'affichage
    def refreshCategories(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT DISTINCT categorieEp FROM V0_LesEpreuves")
            self.ui.liste_categories.clear()
            for row in result:
                self.ui.liste_categories.addItem(row[0])
        except Exception as e:
            display.refreshLabel(self.ui.label_fct_comp_2, "Impossible d'afficher les résultats : " + repr(e))

    def refreshResult(self):
        # TODO 1.2 : fonction à modifier pour remplacer la zone de saisie par une liste de valeurs issues de la BD une
        #  fois le fichier ui correspondant mis à jour

        display.refreshLabel(self.ui.label_fct_comp_2, "")
        if not self.ui.liste_categories.currentItem().text():
            self.ui.table_fct_comp_2.setRowCount(0)
            display.refreshLabel(self.ui.label, "Aucune catégorie sélectionnée")
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "SELECT numEp, nomEp, formeEp, nomDi, categorieEp, nbSportifsEp, strftime('%Y-%m-%d',dateEp,"
                    "'unixepoch') FROM V0_LesEpreuves WHERE categorieEp = ?",
                        [self.ui.liste_categories.currentItem().text()])
                display.refreshLabel(self.ui.label,"Catégorie sélectionnée : "+self.ui.liste_categories.currentItem().text())
            except Exception as e:
                self.ui.table_fct_comp_3.setRowCount(0)
                display.refreshLabel(self.ui.label_fct_comp_2, "Impossible d'afficher les résultats : " + repr(e))
            else:
                i = display.refreshGenericData(self.ui.table_fct_comp_2, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_fct_comp_2, "Aucun résultat")
