
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class AppFctPartie2_1(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_partie2_1.ui", self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):
        display.refreshLabel(self.ui.label_partie2_1, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "SELECT ROUND(AVG(age),1) as ageMoyen, numEq FROM LesAgesSportifs JOIN LesSportifsEQ S USING(numSp) JOIN LesResultats R ON(S.numEq=R.gold) GROUP BY numEq")
        except Exception as e:
            self.ui.table_partie2_1.setRowCount(0)
            display.refreshLabel(self.ui.label_partie2_1, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_partie2_1, result)