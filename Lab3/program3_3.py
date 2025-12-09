# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_3.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.display_text = QLabel(Form)
        self.display_text.setObjectName(u"display_text")
        self.display_text.setGeometry(QRect(100, 30, 401, 16))
        self.one = QPushButton(Form)
        self.one.setObjectName(u"one")
        self.one.setGeometry(QRect(100, 50, 75, 31))
        self.two = QPushButton(Form)
        self.two.setObjectName(u"two")
        self.two.setGeometry(QRect(170, 50, 75, 31))
        self.three = QPushButton(Form)
        self.three.setObjectName(u"three")
        self.three.setGeometry(QRect(240, 50, 75, 31))
        self.six = QPushButton(Form)
        self.six.setObjectName(u"six")
        self.six.setGeometry(QRect(240, 80, 75, 31))
        self.four = QPushButton(Form)
        self.four.setObjectName(u"four")
        self.four.setGeometry(QRect(100, 80, 75, 31))
        self.five = QPushButton(Form)
        self.five.setObjectName(u"five")
        self.five.setGeometry(QRect(170, 80, 75, 31))
        self.nine = QPushButton(Form)
        self.nine.setObjectName(u"nine")
        self.nine.setGeometry(QRect(240, 110, 75, 31))
        self.sharp = QPushButton(Form)
        self.sharp.setObjectName(u"sharp")
        self.sharp.setGeometry(QRect(240, 140, 75, 31))
        self.zero = QPushButton(Form)
        self.zero.setObjectName(u"zero")
        self.zero.setGeometry(QRect(170, 140, 75, 31))
        self.star = QPushButton(Form)
        self.star.setObjectName(u"star")
        self.star.setGeometry(QRect(100, 140, 75, 31))
        self.seven = QPushButton(Form)
        self.seven.setObjectName(u"seven")
        self.seven.setGeometry(QRect(100, 110, 75, 31))
        self.eight = QPushButton(Form)
        self.eight.setObjectName(u"eight")
        self.eight.setGeometry(QRect(170, 110, 75, 31))
        self.talk = QPushButton(Form)
        self.talk.setObjectName(u"talk")
        self.talk.setGeometry(QRect(100, 170, 111, 31))
        self.d = QPushButton(Form)
        self.d.setObjectName(u"d")
        self.d.setGeometry(QRect(210, 170, 101, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.display_text.setText("")
        self.one.setText(QCoreApplication.translate("Form", u"1", None))
        self.two.setText(QCoreApplication.translate("Form", u"2", None))
        self.three.setText(QCoreApplication.translate("Form", u"3", None))
        self.six.setText(QCoreApplication.translate("Form", u"6", None))
        self.four.setText(QCoreApplication.translate("Form", u"4", None))
        self.five.setText(QCoreApplication.translate("Form", u"5", None))
        self.nine.setText(QCoreApplication.translate("Form", u"9", None))
        self.sharp.setText(QCoreApplication.translate("Form", u"#", None))
        self.zero.setText(QCoreApplication.translate("Form", u"0", None))
        self.star.setText(QCoreApplication.translate("Form", u"*", None))
        self.seven.setText(QCoreApplication.translate("Form", u"7", None))
        self.eight.setText(QCoreApplication.translate("Form", u"8", None))
        self.talk.setText(QCoreApplication.translate("Form", u"Talk", None))
        self.d.setText(QCoreApplication.translate("Form", u"<", None))
    # retranslateUi

