# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputGroupNum.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 97)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 10, 61, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(8, "")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "请选择存入的动作组："))
        self.comboBox_3.setCurrentText(_translate("Dialog", "G1"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "G1"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "G2"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "G3"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "G4"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "G5"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "G6"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "G7"))
        self.comboBox_3.setItemText(7, _translate("Dialog", "G8"))
        self.pushButton_3.setText(_translate("Dialog", "确定"))
        self.pushButton_4.setText(_translate("Dialog", "取消"))