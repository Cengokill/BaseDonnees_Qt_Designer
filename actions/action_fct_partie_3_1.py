
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
