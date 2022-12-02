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
        self.donnee1 = ""
        self.donnee2 = ""
        self.refreshResult()

    # Fonction de mise à jour de l'affichage

    def afficherInscription(self):
        rowid = self.ui.table_3_1.selectionModel().currentIndex().row()
        self.donnee1 = self.ui.table_3_1.item(rowid, 0).text()
        self.donnee2 = self.ui.table_3_1.item(rowid, 1).text()
        display.refreshLabel(self.ui.label_numIn_affiche, self.donnee1)
        display.refreshLabel(self.ui.label_numEp_affiche, self.donnee2)
        #display.refreshLabel(self.ui.label_erreur_modif, "inscription sélectionnée : numIn = " + self.donnee1 + ", numEp = " + self.donnee2)
        self.ui.modif_numIn.setText(self.donnee1)
        self.ui.modif_numEp.setText(self.donnee2)

    def supprimerInscription(self):
        if self.donnee1 == "" or self.donnee2 == "":
            display.refreshLabel(self.ui.label_erreur_modif, "Aucune inscription sélectionnée !")
            return
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "DELETE FROM LesInscriptions WHERE (numIn = "+self.donnee1+" AND numEp = "+self.donnee2+")")
                display.refreshLabel(self.ui.label_erreur_supprimer, "Inscription supprimée avec succès !")
                self.refreshResult()
            except Exception as e:
                self.ui.table_3_1.setRowCount(0)
                display.refreshLabel(self.ui.label_erreur_3_1,
                                     "Impossible d'afficher les résultats : " + repr(e))

    def modifierInscription(self):
        if self.donnee1 == "" or self.donnee2 == "":
            display.refreshLabel(self.ui.label_erreur_modif, "Aucune inscription sélectionnée !")
            return
        if self.ui.input_numIn_modif.text() == self.donnee1 and self.ui.input_numEp_modif.text() == self.donnee2:
            display.refreshLabel(self.ui.label_erreur_modif, "Veuillez modifier la sélection !")
            return
        else:
            numIn = self.ui.modif_numIn.text()  # récupération de la valeur dans le champ modif_numIn
            numEp = self.ui.modif_numEp.text()  # récupération de la valeur dans le champ modif_numEp
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "UPDATE LesInscriptions SET numIn = " + numIn + ", numEp = " + numEp + " WHERE (numIn = " + self.donnee1 + "AND numEp = " + self.donnee2 + ")")
                self.refreshResult()
            except Exception as e:
                self.ui.table_3_1.setRowCount(0)
                display.refreshLabel(self.ui.label_erreur_3_1,
                                     "Impossible d'ajouter les données : " + repr(e))

    def ajouterInscription(self):
        if self.ui.input_numIn.text() == "" or self.ui.input_numEp.text() == "":
            display.refreshLabel(self.ui.label_erreur_ajouter, "Veuillez remplir tous les champs !")
            return
        else:
            numIn = self.ui.input_numIn.text()  # récupération de la valeur dans le champ input_numIn
            numEp = self.ui.input_numEp.text()  # récupération de la valeur dans le champ input_numEp
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "INSERT INTO LesInscriptions VALUES (" + numIn + ", " + numEp + ")")
                display.refreshLabel(self.ui.label_erreur_ajouter, "Inscription ajoutée (à la fin de la table) avec succès !")
                self.refreshResult()
            except Exception as e:
                self.ui.table_3_1.setRowCount(0)
                display.refreshLabel(self.ui.label_erreur_3_1, "Impossible d'insérer les données : " + repr(e))

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
