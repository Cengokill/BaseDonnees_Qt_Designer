import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class AppFctPartie3_2(QDialog):

    #Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_partie3_2.ui", self)
        self.data = data
        self.donnee1 = ""
        self.donnee2 = ""
        self.donnee3 = ""
        self.donnee4 = ""
        self.refreshResult()

    # Fonction de mise à jour de l'affichage

    def afficherResultat(self):
        rowid = self.ui.table_3_2.selectionModel().currentIndex().row()
        self.donnee1 = self.ui.table_3_2.item(rowid, 0).text()
        self.donnee2 = self.ui.table_3_2.item(rowid, 1).text()
        self.donnee3 = self.ui.table_3_2.item(rowid, 2).text()
        self.donnee4 = self.ui.table_3_2.item(rowid, 3).text()
        display.refreshLabel(self.ui.label_numEp_affiche, self.donnee1)
        display.refreshLabel(self.ui.label_gold_affiche, self.donnee2)
        display.refreshLabel(self.ui.label_silver_affiche, self.donnee3)
        display.refreshLabel(self.ui.label_bronze_affiche, self.donnee4)
        #display.refreshLabel(self.ui.label_erreur_modif, "inscription sélectionnée : numIn = " + self.donnee1 + ", numEp = " + self.donnee2)
        self.ui.modif_numEp.setText(self.donnee1)
        self.ui.modif_gold.setText(self.donnee2)
        self.ui.modif_silver.setText(self.donnee3)
        self.ui.modif_bronze.setText(self.donnee4)

    def supprimerResultat(self):
        if self.donnee1 == "" or self.donnee2 == "" or self.donnee3 == "" or self.donnee4 == "":
            display.refreshLabel(self.ui.label_erreur_modif, "Aucun résultat sélectionné !")
            return
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "DELETE FROM LesResultats WHERE (numEp = "+self.donnee1+")")
                display.refreshLabel(self.ui.label_erreur_supprimer, "Resultats supprimés avec succès !")
                self.refreshResult()
            except Exception as e:
                self.ui.table_3_2.setRowCount(0)
                display.refreshLabel(self.ui.label_erreur_3_2,
                                     "Impossible d'afficher les résultats : " + repr(e))

    def modifierResultat(self):
        numEp = self.ui.modif_numEp.text()  # récupération de la valeur dans le champ modif_numEp
        gold = self.ui.modif_gold.text()  # récupération de la valeur dans le champ modif_gold
        silver = self.ui.modif_silver.text()  # récupération de la valeur dans le champ modif_silver
        bronze = self.ui.modif_bronze.text()  # récupération de la valeur dans le champ modif_bronze

        if self.donnee1 == "" or self.donnee2 == "" or self.donnee3 == "" or self.donnee4 == "" :
            display.refreshLabel(self.ui.label_erreur_modif, "Aucun résultat sélectionné !")
            return
        if numEp == self.donnee1 and gold == self.donnee2 and silver == self.donnee2 and bronze == self.donnee4 :
            display.refreshLabel(self.ui.label_erreur_modif, "Veuillez modifier la sélection !")
            return
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "UPDATE LesResultats SET numEp = " + numEp + ", gold = " + gold + ", silver = " + silver + ", bronze = " + bronze + " WHERE (numEp = " + self.donnee1 + ")")
                display.refreshLabel(self.ui.label_erreur_modif, "Résultats modifiés avec succès !")
                self.refreshResult()
            except Exception as e:
                self.ui.table_3_2.setRowCount(0)
                display.refreshLabel(self.ui.label_erreur_3_2,
                                     "Impossible d'ajouter les données : " + repr(e))

    def ajouterResultat(self):
        if self.ui.input_numEp.text() == "" or self.ui.input_gold.text() == "" or self.ui.input_silver.text() == "" or self.ui.input_bronze.text() == "":
            display.refreshLabel(self.ui.label_erreur_ajouter, "Veuillez remplir tous les champs !")
            return
        else:
            numEp = self.ui.input_numEp.text()  # récupération de la valeur dans le champ input_numEp
            gold = self.ui.input_gold.text()  # récupération de la valeur dans le champ input_gold
            silver = self.ui.input_silver.text()  # récupération de la valeur dans le champ input_silver
            bronze = self.ui.input_bronze.text()  # récupération de la valeur dans le champ input_bronze
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "INSERT INTO LesResultats VALUES (" + numEp + ", " + gold + ", " + silver + ", " + bronze + ")")
                display.refreshLabel(self.ui.label_erreur_ajouter, "Résultats ajoutés (à la fin de la table) avec succès !")
                self.refreshResult()
            except Exception as e:
                self.ui.table_3_2.setRowCount(0)
                display.refreshLabel(self.ui.label_erreur_3_2, "Impossible d'insérer les données : " + repr(e))

    def refreshResult(self):
        display.refreshLabel(self.ui.label_erreur_3_2, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT numEp, gold, silver, bronze FROM LesResultats")
        except Exception as e:
            self.ui.table_3_2.setRowCount(0)
            display.refreshLabel(self.ui.label_erreur_3_2, "Impossible d'afficher les résultats : " + repr(e))
        else:
            i = display.refreshGenericData(self.ui.table_3_2, result)
            if i == 0:
                display.refreshLabel(self.ui.label_erreur_3_2, "Aucun résultat")
