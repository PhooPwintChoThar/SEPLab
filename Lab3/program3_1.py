# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_1.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_form(object):
    def setupUi(self, form):
        if not form.objectName():
            form.setObjectName(u"form")
        form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hello_button = QPushButton(form)
        self.hello_button.setObjectName(u"hello_button")

        self.verticalLayout.addWidget(self.hello_button)


        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"Form", None))
        self.hello_button.setText(QCoreApplication.translate("form", u"PushButton", None))
    # retranslateUi

