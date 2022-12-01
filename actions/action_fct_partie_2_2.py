
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class AppFctPartie2_2(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_partie2_2.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):

        display.refreshLabel(self.ui.label_partie2_2, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "SELECT DISTINCT pays FROM LesResultats A JOIN LesSportifsEQ B ON(A.gold=B.numSp OR A.gold=B.numEq OR A.silver=B.numSp OR A.silver=B.numEq OR A.bronze=B.numSp OR A.bronze=B.numEq)")
        except Exception as e:
            self.ui.table_partie2_2.setRowCount(0)
            display.refreshLabel(self.ui.label_partie2_2, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_partie2_2, result)