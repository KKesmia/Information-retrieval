# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'view.ui'
# Created by: PyQt5 UI code generator 5.13.0
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append('C:/Users/Moi/Desktop/RI')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Modele import BoolMod,VectMod
from Eval import Eval
import operator
from cacm import dictionner

import pickle

with open('cacm/Full_Dict.pickle', 'rb') as handle:
    FD = pickle.load(handle)

with open('cacm/Dict_Inv1.pickle', 'rb') as handle:
    Dinv1 = pickle.load(handle)

with open('cacm/Dict_Inv2.pickle', 'rb') as handle:
    Dinv2 = pickle.load(handle)

with open('cacm/Dict_Inv1_Pond.pickle', 'rb') as handle:
    Dinvpond1 = pickle.load(handle)

with open('cacm/Dict_Inv2_Pond.pickle', 'rb') as handle:
    Dinvpond2 = pickle.load(handle)

with open('cacm/ALL_titles.pickle', 'rb') as handle:
    All_titles = pickle.load(handle)

with open('cacm/All_texts.pickle', 'rb') as handle:
    All_texts = pickle.load(handle)


bmod = BoolMod.Basic(FD, Dinv1, Dinv2, Dinvpond1, Dinvpond2)
vmod = VectMod.VectMod(FD, Dinv1, Dinv2, Dinvpond1, Dinvpond2, "cacm/common_words")

evaal = Eval.Eval(vmod)

qrels = open("cacm/qrels.text","r+").read().split("\n")
Cardiq = int(qrels[-1].split(" ")[0])

Vect_modes = ['Inner product', 'Coef. de Dice', 'Mesure du cosinus', 'Mesure du Jaccard']
Bool_modes = ['Basic']

class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(953, 609)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(800, 70, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(False)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(650, 70, 121, 31))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setEditable(False)

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 420, 81, 21))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(240, 420, 81, 21))
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setObjectName("comboBox_4")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(630, 30, 311, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 30, 311, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 170, 391, 211))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(550, 170, 391, 211))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(30, 460, 391, 121))
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_4")

        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(550, 460, 391, 121))
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_4")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(140, 80, 95, 20))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(300, 80, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 110, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 110, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 470, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        # self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_6.setGeometry(QtCore.QRect(440, 510, 93, 28))
        # self.pushButton_6.setObjectName("pushButton_6")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 21))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 55, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 150, 55, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 30, 81, 21))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 400, 81, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 440, 81, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 440, 81, 16))
        self.label_7.setObjectName("label_7")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onChanged(self):
        self.comboBox.setDisabled(False)
        if self.comboBox_2.count() == 3 :
            self.comboBox_2.removeItem(0)

        while self.comboBox.count() != 0 :
            self.comboBox.removeItem(0)

        if(self.comboBox_2.currentText() == "Vectoriel"):
            self.comboBox.addItem('Choisir type')
            for i in Vect_modes:
                self.comboBox.addItem(i)

        if(self.comboBox_2.currentText() == "Boolean"):
            self.comboBox.addItem('Choisir extention')
            for i in Bool_modes:
                self.comboBox.addItem(i)

        self.comboBox.activated.connect(self.onChanged_2) 
        
    def onChanged_2(self):
        if(self.comboBox.count() == len(Bool_modes) + 1 and self.comboBox_2.currentText() == "Boolean" ) or ( self.comboBox.count() == len(Vect_modes) + 1  and self.comboBox_2.currentText() == "Vectoriel"):
            self.comboBox.removeItem(0)
            
    def onChanged_3(self):
        if not self.comboBox_3.itemText(0).isdigit(): 
            self.comboBox_3.removeItem(0)
        qid = self.comboBox_3.currentText()
        question = "Query is:" + evaal.questions[qid] + "\n   best answers:"
        if int(qid) in range(1,10):
            answers = evaal.ideals["0"+qid]
        else:
            answers = evaal.ideals[qid]
        for i in answers:
            question = question + "\n   " + i
        self.textEdit_6.setText(question)

    def onChanged_4(self):
        if not (self.comboBox_4.itemText(0) in Vect_modes): 
            self.comboBox_4.removeItem(0)

    def reset(self):
        _translate = QtCore.QCoreApplication.translate

        self.textEdit.setPlainText("")

        while self.comboBox.count() != 0 :
            self.comboBox.removeItem(0)
        self.comboBox.setEnabled(False)

        while self.comboBox_2.count() != 0 :
            self.comboBox_2.removeItem(0)    

        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setCurrentText(_translate("MainWindow", "Choisir modéle"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Choisir modele"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Vectoriel"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Boolean"))
    
    def reset_2(self):
        self.textEdit_2.setPlainText("")
        self.textEdit_3.setPlainText("")
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)

    def search_rech(self):
        error = QtWidgets.QErrorMessage(self)
        if self.radioButton.isChecked():
            word = self.textEdit_2.toPlainText().lower()
            if len(word.split()) > 1:
                error.showMessage("Error! Expected one word but more is given.")
            else:
                results = dictionner.call_docsv(word, Dinv2)
                answer = "------------------------------- Results -------------------------------\n"
                answer = answer + "DocID Freq " + "\n"
                for item in results:
                    answer = answer + item[0] + (4-len(item[0]))*" "  +  "   " + str(item[1]) + "\n"
                self.textEdit_3.setText(answer)

        if self.radioButton_2.isChecked():
            try:
                indice = int(self.textEdit_2.toPlainText())
                results = dictionner.call_Termsv(indice, FD)
                answer = "------------------------------- Results -------------------------------\n"
                answer = answer + "Mot  Freq " + "\n"
                for item in results:
                    answer = answer + item[0] +  "   " + str(item[1]) + "\n"
                self.textEdit_3.setText(answer)
            except:
                error.showMessage("Error! Expected file ID.")

    def search_req(self):
        answer = str()
        self.textEdit_4.setText(answer)
        error = QtWidgets.QErrorMessage(self)

        if self.textEdit.toPlainText() == "":
            error.showMessage("Error: Request first")
            error.exec_()
        else:
            if self.comboBox_2.currentText() == "Boolean":
                if self.comboBox.currentText() not in Bool_modes:
                    error.showMessage("Error Select type de Boolean")
                    error.exec_()
                else:
                    results = bmod.Answer( self.textEdit.toPlainText() )
                    if results == 0:
                        error.showMessage("Error Wrong request")
                        error.exec_()
                    else:
                        if len(results) == 0:
                            error.showMessage("Aucun results")
                            error.exec_()
                        else:
                            answer = "------------------------------- Results -------------------------------\n"
                            for i in results:
                                answer = answer + i + " " + All_titles[i] + "\n"
                            self.textEdit_4.setText(answer)

            if self.comboBox_2.currentText() == "Vectoriel":
                request = self.textEdit.toPlainText().lower()
                choice =self.comboBox.currentText()
                results = list()
                answer = "------------------------------- Results -------------------------------\n"
                if choice not in Vect_modes:
                    error.showMessage("Error: Select type de Vectoriel")
                    error.exec_()
                else:
                    if choice == "Inner product":
                        results = vmod.InnerProd(request)

                    if choice == "Coef. de Dice":
                        results = vmod.COEFD(request)

                    if choice == "Mesure du cosinus":
                        results = vmod.cosinusM(request)

                    if choice == "Mesure du Jaccard":
                        results = vmod.jaccardM(request)
                    results = sorted(results, key= operator.itemgetter(1), reverse=True)
                    results = [i for i in results if i[1] > 0]

                    for i in results:
                        answer += str(i[0]) + " " + All_titles[str(i[0])] + " "+ str(i[1])  + "\n"
                    self.textEdit_4.setText(answer)

    def evalute(self):
        error = QtWidgets.QErrorMessage(self)
        qid = self.comboBox_3.currentText()
        print(qid)
        measure = self.comboBox_4.currentText()
        if measure in Vect_modes and qid.isdigit():
            question = evaal.questions[qid][1:]
            results = list()
            if measure == "Inner product":
                results = vmod.InnerProd(question)

            if measure == "Coef. de Dice":
                results = vmod.COEFD(question)

            if measure == "Mesure du cosinus":
                results = vmod.cosinusM(question)

            if measure == "Mesure du Jaccard":
                results = vmod.jaccardM(question)
            question = "Query is:" + question + "\n   best answers:"
            results = sorted(results, key= operator.itemgetter(1), reverse=True)
            results = [ r for r in results if r[1] > 0 ]

            for i in results:
                question = question + "\n   " + str(i[0])

            if int(qid) in range(1,10):
                qid = "0"+qid  
            rappel , precesion = evaal.rap_pre(qid, results, len(results))
            question = question + "\n   Rappel: "+str(rappel)+"     Precision: "+str(precesion)
            self.textEdit_5.setText(question)
        else:
            error.showMessage("Error! measure or query not selected.")

    def disply(self):
        print("hey")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recherche Information"))

        self.comboBox.setCurrentText(_translate("MainWindow", "Choisir type"))

        self.comboBox_2.setCurrentText(_translate("MainWindow", "Choisir modéle"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Choisir modele"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Vectoriel"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Boolean"))
        self.comboBox_2.activated.connect(self.onChanged)

        self.comboBox_3.setCurrentText(_translate("MainWindow", "Requete"))
        self.comboBox_3.addItem("Req_id")
        for i in range(0, Cardiq):
            self.comboBox_3.addItem(str(i+1))
        self.comboBox_3.activated.connect(self.onChanged_3) 

        self.comboBox_4.addItem("measure")
        for i in Vect_modes:
            self.comboBox_4.addItem(str(i))
        self.comboBox_4.activated.connect(self.onChanged_4) 

        self.radioButton.setText(_translate("MainWindow", "Mot"))
        self.radioButton_2.setText(_translate("MainWindow", "document"))

        self.pushButton.setText(_translate("MainWindow", "reset"))
        self.pushButton.clicked.connect(self.reset)

        self.pushButton_4.setText(_translate("MainWindow", "reset"))
        self.pushButton_4.clicked.connect(self.reset_2)

        self.pushButton_2.setText(_translate("MainWindow", "search"))
        self.pushButton_2.clicked.connect(self.search_req)

        self.pushButton_3.setText(_translate("MainWindow", "search"))
        self.pushButton_3.clicked.connect(self.search_rech)

        self.pushButton_5.setText(_translate("MainWindow", "Evaluate"))
        self.pushButton_5.clicked.connect(self.evalute)

        # self.pushButton_6.setText(_translate("MainWindow", "Disply"))
        # self.pushButton_6.clicked.connect(self.disply)

        self.label.setText(_translate("MainWindow", "Recherche :"))
        self.label_2.setText(_translate("MainWindow", "Resultat :"))
        self.label_3.setText(_translate("MainWindow", "Resultat :"))
        self.label_4.setText(_translate("MainWindow", "Request :"))
        self.label_5.setText(_translate("MainWindow", "Evaluation :"))
        self.label_6.setText(_translate("MainWindow", "Results :"))
        self.label_7.setText(_translate("MainWindow", "Expected :"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
