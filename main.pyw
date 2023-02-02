from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import ISE_get_dacl_by_user
import ISE_get_dacl_by_name
import ISE_get_dacls_by_str
import os
import datetime
import json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ise_primary_PAN_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ise_primary_PAN_text.setFont(font)
        self.ise_primary_PAN_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ise_primary_PAN_text.setTextFormat(QtCore.Qt.RichText)
        self.ise_primary_PAN_text.setAlignment(QtCore.Qt.AlignCenter)
        self.ise_primary_PAN_text.setWordWrap(True)
        self.ise_primary_PAN_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.ise_primary_PAN_text.setObjectName("ise_primary_PAN_text")
        self.verticalLayout.addWidget(self.ise_primary_PAN_text)
        self.username_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_text.setFont(font)
        self.username_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.username_text.setTextFormat(QtCore.Qt.RichText)
        self.username_text.setAlignment(QtCore.Qt.AlignCenter)
        self.username_text.setWordWrap(True)
        self.username_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.username_text.setObjectName("username_text")
        self.verticalLayout.addWidget(self.username_text)
        self.password_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_text.setFont(font)
        self.password_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.password_text.setTextFormat(QtCore.Qt.RichText)
        self.password_text.setAlignment(QtCore.Qt.AlignCenter)
        self.password_text.setWordWrap(True)
        self.password_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.password_text.setObjectName("password_text")
        self.verticalLayout.addWidget(self.password_text)
        self.user_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_text.setFont(font)
        self.user_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.user_text.setTextFormat(QtCore.Qt.RichText)
        self.user_text.setAlignment(QtCore.Qt.AlignCenter)
        self.user_text.setWordWrap(True)
        self.user_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.user_text.setObjectName("user_text")
        self.verticalLayout.addWidget(self.user_text)
        self.dacl_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dacl_text.setFont(font)
        self.dacl_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dacl_text.setTextFormat(QtCore.Qt.RichText)
        self.dacl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.dacl_text.setWordWrap(True)
        self.dacl_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.dacl_text.setObjectName("dacl_text")
        self.verticalLayout.addWidget(self.dacl_text)
        self.str_in_dacl_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.str_in_dacl_text.setFont(font)
        self.str_in_dacl_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.str_in_dacl_text.setTextFormat(QtCore.Qt.RichText)
        self.str_in_dacl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.str_in_dacl_text.setWordWrap(True)
        self.str_in_dacl_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.str_in_dacl_text.setObjectName("str_in_dacl_text")
        self.verticalLayout.addWidget(self.str_in_dacl_text)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 10, 341, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ise_primary_PAN_field = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.ise_primary_PAN_field.setObjectName("ise_primary_PAN_field")
        self.verticalLayout_2.addWidget(self.ise_primary_PAN_field)
        self.username_field = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.username_field.setObjectName("username_field")
        self.verticalLayout_2.addWidget(self.username_field)
        self.password_field = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.password_field.setObjectName("password_field")
        self.verticalLayout_2.addWidget(self.password_field)
        self.user_field = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.user_field.setObjectName("user_field")
        self.verticalLayout_2.addWidget(self.user_field)
        self.dacl_field = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.dacl_field.setObjectName("dacl_field")
        self.verticalLayout_2.addWidget(self.dacl_field)
        self.str_in_dacl_field = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.str_in_dacl_field.setObjectName("str_in_dacl_field")
        self.verticalLayout_2.addWidget(self.str_in_dacl_field)
        self.show_rules_by_user = QtWidgets.QPushButton(self.centralwidget)
        self.show_rules_by_user.setGeometry(QtCore.QRect(640, 10, 261, 61))
        self.show_rules_by_user.setObjectName("show_rules_by_user")
        self.rules_for_dacl = QtWidgets.QLabel(self.centralwidget)
        self.rules_for_dacl.setGeometry(QtCore.QRect(10, 260, 441, 401))
        self.rules_for_dacl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rules_for_dacl.setText("")
        self.rules_for_dacl.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard |
            QtCore.Qt.LinksAccessibleByMouse |
            QtCore.Qt.TextBrowserInteraction |
            QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse
        )
        self.rules_for_dacl.setObjectName("rules_for_dacl")
        self.dacl_name = QtWidgets.QLabel(self.centralwidget)
        self.dacl_name.setGeometry(QtCore.QRect(10, 210, 441, 41))
        self.dacl_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dacl_name.setText("")
        self.dacl_name.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard |
            QtCore.Qt.LinksAccessibleByMouse |
            QtCore.Qt.TextBrowserInteraction |
            QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse
        )
        self.dacl_name.setObjectName("dacl_name")
        self.dacls_with_str = QtWidgets.QLabel(self.centralwidget)
        self.dacls_with_str.setGeometry(QtCore.QRect(460, 260, 441, 401))
        self.dacls_with_str.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dacls_with_str.setText("")
        self.dacls_with_str.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard |
            QtCore.Qt.LinksAccessibleByMouse |
            QtCore.Qt.TextBrowserInteraction |
            QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse
        )
        self.dacls_with_str.setObjectName("dacls_with_str")
        self.str_for_search = QtWidgets.QLabel(self.centralwidget)
        self.str_for_search.setGeometry(QtCore.QRect(460, 210, 441, 41))
        self.str_for_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.str_for_search.setText("")
        self.str_for_search.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard |
            QtCore.Qt.LinksAccessibleByMouse |
            QtCore.Qt.TextBrowserInteraction |
            QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse
        )
        self.str_for_search.setObjectName("str_for_search")
        self.show_dacls_with_str = QtWidgets.QPushButton(self.centralwidget)
        self.show_dacls_with_str.setGeometry(QtCore.QRect(640, 80, 261, 51))
        self.show_dacls_with_str.setObjectName("show_dacls_with_str")
        self.show_rules_for_dacl = QtWidgets.QPushButton(self.centralwidget)
        self.show_rules_for_dacl.setGeometry(QtCore.QRect(640, 140, 261, 51))
        self.show_rules_for_dacl.setObjectName("show_rules_for_dacl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 915, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.triggered.connect(self.saveas)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.actionClose.triggered.connect(self.close)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ISE dACL rules"))
        self.ise_primary_PAN_text.setText(_translate("MainWindow", "ISE Primary Admin node hostname/ip"))
        self.username_text.setText(_translate("MainWindow", "имя пользователя с API правами"))
        self.password_text.setText(_translate("MainWindow", "пароль пользователя с API правами"))
        self.user_text.setText(_translate("MainWindow", "имя пользователя ISE"))
        self.dacl_text.setText(_translate("MainWindow", "имя dACLа"))
        self.str_in_dacl_text.setText(_translate("MainWindow", "строчка в dACL"))
        self.ise_primary_PAN_field.setPlainText(_translate("MainWindow", "172.22.242.16"))
        self.username_field.setPlainText(_translate("MainWindow", "API_user"))
        self.password_field.setPlainText(_translate("MainWindow", ""))
        self.user_field.setPlainText(_translate("MainWindow", ""))
        self.show_rules_for_dacl.setText(_translate("MainWindow", "Покажи правила\ndACLа"))
        self.show_rules_by_user.setText(_translate("MainWindow", "Покажи правила\nдля пользователя"))
        self.show_dacls_with_str.setText(_translate("MainWindow", "Покажи dACLы\nсо строчкой"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.actionOpen.setText(_translate("MainWindow", "Открыть"))
        self.actionSave.setText(_translate("MainWindow", "Сохранить"))
        self.actionSave_as.setText(_translate("MainWindow", "Сохранить как ..."))
        self.actionClose.setText(_translate("MainWindow", "Закрыть"))

    def close(self):
        app.quit()

    def save(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dt = datetime.datetime.now().strftime("%Y%B%d-%H%M%S")
        if self.dacl_name.text():
            with open(f'{dir_path}\\{dt}-{self.dacl_name.text().rstrip()}.txt', 'w') as file:
                save_settings = self.search()
                del save_settings['password']
                file.write(f'{save_settings}\n{self.dacl_name.text()}\n{self.dacl_name.text().rstrip()}')
            self.info_msg("Сохранено", f'Сохранено здесь:\n{dir_path}\\{dt}-{self.dacl_name.text().rstrip()}.txt')
        else:
            error = QMessageBox()
            error.setWindowTitle("Нет правил для сохранения")
            error.adjustSize()
            error.setIcon(QMessageBox.Warning)
            if self.rules_for_dacl.text():
                error.setText("Сохранить ошибку?")
                error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                error.buttonClicked.connect(self.btn_action)
            else:
                error.setText("Нечего сохранять")
                error.setStandardButtons(QMessageBox.Ok)

            error.exec_()

    def saveas(self):
        name = QFileDialog.getSaveFileName(QMessageBox(), "save")
        if name[0]:
            with open(f'{name[0]}', 'w') as file:
                save_settings = self.search()
                del save_settings['password']
                file.write(f'{save_settings}\n{self.dacl_name.text()}\n{self.rules_for_dacl.text().rstrip()}')
        else:
            pass

    def open(self):
        name = QFileDialog.getOpenFileName(QMessageBox(), "open")
        if name[0]:
            self.ise_primary_PAN_field.clear()
            self.username_field.clear()
            self.dacl_name.clear()
            self.user_field.clear()
            self.rules_for_dacl.clear()
            with open(f'{name[0]}', 'r') as file:
                first_line = file.readline()
                second_line = file.readline()
                other_text = file.read()
                if 'acl_' in second_line:
                    self.dacl_name.setText(second_line)
                    whole_text = other_text
                else:
                    whole_text = second_line + other_text
                try:
                    settings = json.loads(first_line)
                except json.JSONDecodeError as jer:
                    settings = first_line
                    if 'Expecting property name enclosed in double quotes' in jer.msg:
                        try:
                            settings = json.loads(first_line.replace('\'', '\"'))
                        except json.JSONDecodeError as jer:
                            print(jer)
                            settings = first_line
                finally:
                    if type(settings) == dict:
                        self.ise_primary_PAN_field.setPlainText(settings['ise_primary_PAN'])
                        self.username_field.setPlainText(settings['username'])
                        self.user_field.setPlainText(settings['user'])
                    elif 'acl_' in settings:
                        self.dacl_name.setText(settings)
                    else:
                        self.rules_for_dacl.setText(first_line + whole_text)
                    self.rules_for_dacl.setText(whole_text)
        else:
            pass

    def btn_action(self, btn):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dt = datetime.datetime.now().strftime("%Y%B%d-%H%M%S")
        if btn.text() == "OK":
            with open(f'{dir_path}\\{dt}-error-{self.rules_for_dacl.text()[:3]}.txt', 'w') as file:
                save_settings = self.search()
                del save_settings['password']
                file.write(f'{save_settings}\n{self.rules_for_dacl.text()}')
            self.info_msg("Сохранено", f"Сохранено здесь:\n{dir_path}\\{dt}-error-{self.rules_for_dacl.text()[:3]}.txt")
        elif btn.text() == "Cancel":
            pass

    def info_msg(self, title, msg):
        info = QMessageBox()
        info.setWindowTitle(title)
        info.adjustSize()
        info.setIcon(QMessageBox.Information)
        info.setText(msg)
        info.setStandardButtons(QMessageBox.Ok)
        info.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard |
            QtCore.Qt.LinksAccessibleByMouse |
            QtCore.Qt.TextBrowserInteraction |
            QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse
        )
        info.exec_()

    def search(self):
        try:
            params = {'ise_primary_PAN': self.ise_primary_PAN_field.toPlainText(),
                      'username': self.username_field.toPlainText(),
                      'password': self.password_field.toPlainText(),
                      'user': self.user_field.toPlainText(),
                      'dacl_str': self.str_in_dacl_field.toPlainText(),
                      'dacl_name': self.dacl_field.toPlainText()}
        except Exception as e:
            print(e)
        else:
            return params

    def add_functions(self):
        self.show_rules_by_user.clicked.connect(lambda: self.do_request_get_dacl_by_user(self.search()))
        self.show_dacls_with_str.clicked.connect(lambda: self.do_request_get_dacls_by_str(self.search()))
        self.show_rules_for_dacl.clicked.connect(lambda: self.do_request_get_dacl_by_name(self.search()))

    def do_request_get_dacl_by_user(self, param_dict):
        try:
            dacls = ISE_get_dacl_by_user.GetDaclByUser(**param_dict)
        except Exception as e:
            self.rules_for_dacl.setText(f"{e}")
        else:
            if type(dacls.result) == dict:
                self.dacl_name.setText(f"{dacls.result['name']}")
                self.rules_for_dacl.setText(f"{dacls.result['dacl']}")
            else:
                self.dacl_name.clear()
                self.rules_for_dacl.setText(dacls.result)

    def do_request_get_dacls_by_str(self, param_dict):
        try:
            dacls = ISE_get_dacls_by_str.GetDaclByStr(**param_dict)
        except Exception as e:
            self.str_for_search.setText(f"{param_dict['dacl_str']}")
            self.dacls_with_str.setText(f"{e}")
        else:
            if type(dacls.result) == dict:
                dacl_names = '\n'.join(dacls.result.keys())
                self.str_for_search.setText(f"{param_dict['dacl_str']}")
                self.dacls_with_str.setText(dacl_names)
            else:
                self.str_for_search.clear()
                self.dacls_with_str.setText(dacls.result)

    def do_request_get_dacl_by_name(self, param_dict):
        try:
            dacls = ISE_get_dacl_by_name.GetDaclByName(**param_dict)
        except Exception as e:
            self.dacl_name.setText(f"{param_dict['dacl_name']}\n")
            self.rules_for_dacl.setText(f"{e}")
        else:
            if type(dacls.result) == dict:
                self.dacl_name.setText(f"{dacls.result['name']}")
                self.rules_for_dacl.setText(f"{dacls.result['dacl']}")
            else:
                self.dacl_name.clear()
                self.rules_for_dacl.setText(dacls.result)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
