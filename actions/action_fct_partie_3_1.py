import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class AppFctPartie3_1(QDialog):

    #Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_partie3_1.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage

    def afficherInscription(self):
        rowid = self.ui.table_3_1.selectionModel().currentIndex().row()
        donnee1 = self.ui.table_3_1.item(rowid, 0).text()
        donnee2 = self.ui.table_3_1.item(rowid, 1).text()
        display.refreshLabel(self.ui.label_numIn_affiche, donnee1)
        display.refreshLabel(self.ui.label_numEp_affiche, donnee2)


    def refreshResult(self):
        display.refreshLabel(self.ui.label_erreur_3_1, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT numIn, numEp FROM LesInscriptions")
        except Exception as e:
            self.ui.table_3_1.setRowCount(0)
            display.refreshLabel(self.ui.label_erreur_3_1, "Impossible d'afficher les résultats : " + repr(e))
        else:
            i = display.refreshGenericData(self.ui.table_3_1, result)
            if i == 0:
                display.refreshLabel(self.ui.label_erreur_3_1, "Aucun résultat")
