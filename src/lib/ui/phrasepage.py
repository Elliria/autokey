#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from phrasepage.ui on Wed Jul 22 13:30:29 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_PhrasePage(object):
    def setupUi(self, PhrasePage):
        PhrasePage.setObjectName("PhrasePage")
        PhrasePage.resize(540, 602)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PhrasePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.descriptionLabel = QtGui.QLabel(PhrasePage)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.verticalLayout_2.addWidget(self.descriptionLabel)
        self.descriptionLineEdit = KLineEdit(PhrasePage)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.verticalLayout_2.addWidget(self.descriptionLineEdit)
        self.phraseText = KTextEdit(PhrasePage)
        self.phraseText.setObjectName("phraseText")
        self.verticalLayout_2.addWidget(self.phraseText)
        self.settingsGroupBox = QtGui.QGroupBox(PhrasePage)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = SettingsWidget(self.settingsGroupBox)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.settingsGroupBox)

        self.retranslateUi(PhrasePage)
        QtCore.QMetaObject.connectSlotsByName(PhrasePage)

    def retranslateUi(self, PhrasePage):
        PhrasePage.setWindowTitle(kdecore.i18n("Form"))
        self.descriptionLabel.setText(kdecore.i18n("Description"))
        self.settingsGroupBox.setTitle(kdecore.i18n("Settings"))

from configwindow import SettingsWidget
from PyKDE4.kdeui import KTextEdit, KLineEdit