
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class AppFctPartie3_1(QDialog):

    #Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_partie3_1.ui", self)
        self.data = data

    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_partie3_1, "")
        if not self.ui.lineEdit.text().strip():
            self.ui.table_fct_partie3_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_partie3_1, "Veuillez indiquer un numéro d'équipe ou de sportif")
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "INSERT INTO LesInscriptions VALUES(",
                    [self.ui.lineEdit.text().strip()])
            except Exception as e:
                self.ui.table_fct_partie3_1.setRowCount(0)
                display.refreshLabel(self.ui.label_fct_partie3_1, "Impossible d'afficher les résultats : " + repr(e))
            else:
                i = display.refreshGenericData(self.ui.table_fct_partie3_1, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_fct_partie3_1, "Aucun résultat")