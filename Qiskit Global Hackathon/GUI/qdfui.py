from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QVBoxLayout, QMessageBox
from pathlib import Path
import os
import sys
import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute


class Ui_qdfMainWindow(object):
    def setupUi(self, qdfMainWindow):
        qdfMainWindow.setObjectName("qdfMainWindow")
        qdfMainWindow.resize(380, 335)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/qdf/qdflogo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        qdfMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(qdfMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 401, 661))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lbl_qdf = QtWidgets.QLabel(self.frame)
        self.lbl_qdf.setGeometry(QtCore.QRect(100, 20, 271, 71))
        self.lbl_qdf.setStyleSheet("font: 20pt \"Segoe UI Historic\";")
        self.lbl_qdf.setObjectName("lbl_qdf")
        self.btn_filediag = QtWidgets.QPushButton(self.frame)
        self.btn_filediag.setGeometry(QtCore.QRect(90, 120, 231, 51))
        self.btn_filediag.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.btn_filediag.setStyleSheet("font: 12pt \"Segoe UI Historic\";\n"
                                        "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/qdf/icons8-binary-file-64.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.btn_filediag.setIcon(icon1)
        self.btn_filediag.setIconSize(QtCore.QSize(32, 32))
        self.btn_filediag.setObjectName("btn_filediag")
        self.btn_exit = QtWidgets.QPushButton(self.frame)
        self.btn_exit.setGeometry(QtCore.QRect(170, 280, 91, 41))
        self.btn_exit.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.btn_exit.setStyleSheet("font: 12pt \"Segoe UI Historic\";\n"
                                    "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/qdf/icons8-cancel-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_exit.setIcon(icon2)
        self.btn_exit.setIconSize(QtCore.QSize(32, 32))
        self.btn_exit.setObjectName("btn_exit")
        self.lbl_logo = QtWidgets.QLabel(self.frame)
        self.lbl_logo.setGeometry(QtCore.QRect(0, 10, 121, 101))
        self.lbl_logo.setStyleSheet("image: url(:/qdf/icons8-processor-64.png);")
        self.lbl_logo.setText("")
        self.lbl_logo.setObjectName("lbl_logo")
        self.btn_verifyoutput = QtWidgets.QPushButton(self.frame)
        self.btn_verifyoutput.setGeometry(QtCore.QRect(30, 210, 171, 41))
        self.btn_verifyoutput.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.btn_verifyoutput.setStyleSheet("font: 12pt \"Segoe UI Historic\";\n"
                                            "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/qdf/icons8-check-file-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_verifyoutput.setIcon(icon3)
        self.btn_verifyoutput.setIconSize(QtCore.QSize(32, 32))
        self.btn_verifyoutput.setObjectName("btn_verifyoutput")
        self.btn_ckt_show = QtWidgets.QPushButton(self.frame)
        self.btn_ckt_show.setGeometry(QtCore.QRect(220, 210, 161, 41))
        self.btn_ckt_show.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.btn_ckt_show.setStyleSheet("font: 12pt \"Segoe UI Historic\";\n"
                                        "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/qdf/icons8-electronics-64.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.btn_ckt_show.setIcon(icon4)
        self.btn_ckt_show.setIconSize(QtCore.QSize(32, 32))
        self.btn_ckt_show.setObjectName("btn_ckt_show")
        self.lbl_logo.raise_()
        self.lbl_qdf.raise_()
        self.btn_filediag.raise_()
        self.btn_exit.raise_()
        self.btn_verifyoutput.raise_()
        self.btn_ckt_show.raise_()
        qdfMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(qdfMainWindow)
        QtCore.QMetaObject.connectSlotsByName(qdfMainWindow)

    def retranslateUi(self, qdfMainWindow):
        _translate = QtCore.QCoreApplication.translate
        qdfMainWindow.setWindowTitle(_translate("qdfMainWindow", "Quantum Data Feeder"))
        self.lbl_qdf.setText(_translate("qdfMainWindow",
                                        "<html><head/><body><p><span style=\" color:#000000;\">Quantum Data Feeder</span></p></body></html>"))
        self.btn_filediag.setText(_translate("qdfMainWindow", "Select the file to Send"))
        self.btn_exit.setText(_translate("qdfMainWindow", "Exit"))
        self.btn_verifyoutput.setText(_translate("qdfMainWindow", "Verify the Output"))
        self.btn_ckt_show.setText(_translate("qdfMainWindow", "View the Circuit"))

class qdfmainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(qdfmainwindow, self).__init__()
        self.ui = Ui_qdfMainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.ui.btn_filediag.clicked.connect(self.btn_fd_clicked)
        self.ui.btn_exit.clicked.connect(self.btn_exit_clicked)
        self.ui.btn_verifyoutput.clicked.connect(self.btn_verifyoutput_clicked)
        self.ui.btn_ckt_show.clicked.connect(self.btn_ckt_show_clicked)

    def btn_exit_clicked(self):
        QtWidgets.QMessageBox.information(self,"Quantum Data Feeder","Thank You (^_^)")

    def btn_fd_clicked(self):
        file_nme = self.getFileName()
        print(file_nme)
        file_extn = Path(file_nme).suffix
        print(file_extn)
        qdf_start = self.startQDF(file_nme)

    def getFileName(self):
        file_fltr = 'Data file (*.txt *.png)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_fltr,
        )
        return response[0]

    def startQDF(self, file_nme):
        # opening a file and converting each sentence into a list element.
        fileobj = open(file_nme)
        lines = []
        for line in fileobj:
            lines.append(line.strip())

        # for each in lines:
        #     print('Your Input file contains : \n')
        #     print(each, end='')
        # print('\n')

        ''' STEP - 2 '''
        # converting single indexed list into multiple indexed list.
        list = []
        for each in lines:
            list.append([each])

        ''' STEP - 3 '''

        # converting each multiple indexed element(each sentence) into single word.

        def convert(each):
            return ' '.join(each).split()

        word_list = []
        for each in list:
            lst = convert(each)

            for i in lst:

                # adding '@' symbol in place of period (',')
                if (i[-1] == ','):
                    i = i[:-1] + '@'

                # adding '$' symbol in place of period ('.')
                if (i[-1] == '.' and i):
                    i = i[:-1] + '$'

                # adding '#' symbol after each word
                i = i + '#'

                # addind each word into final_list
                word_list.append(i)

        # Remove space or # symbol at the end of the final content in the file
        str = ''
        for i in word_list[-1]:
            if (i == word_list[-1][-1]):
                pass
            else:
                str = str + i
        word_list.pop()
        word_list.append(str)

        ''' STEP - 4 '''
        # using join() + ord() + format()
        # Converting each String in final_list to "single character" and then
        # Converting each character to binary and then storing into binary_list

        binary_list = []
        for each in word_list:
            for i in each:
                res = ''.join(format(ord(i), '08b'))
                binary_list.append(res)

        ''' STEP - 5 '''
        # Check whether all binarycharacters length is 8 or not
        # if not print(false)

        for each in binary_list:
            if (len(each) == 8):
                value = True
            else:
                value = False

        ''' STEP - 6 '''
        if (value == True):
            # if value is True, pass each binary character to the "Quantum FTP Circuirt".
            # print('The Binary values for each character are : \n')
            for each in binary_list:
                n = each
                # print(n)
        # Circuit starts
        counts_list = []
        for each in binary_list:
            single_char = each
            n = len(single_char)

            Alice_data = QuantumRegister(n, 'aD')
            Alice_qubit = QuantumRegister(n, 'aQ')
            Bob_qubit = QuantumRegister(n, 'bQ')
            cr = ClassicalRegister(n * 3, 'c')
            circuit = QuantumCircuit(Alice_data, Alice_qubit, Bob_qubit, cr)

            i = 0
            for each in single_char:
                if (each == '1'):
                    circuit.x(Alice_data[int(i)])
                i += 1
            circuit.barrier()

            for i in range(n):
                circuit.h(Alice_qubit[i])
                circuit.cx(Alice_qubit[i], Bob_qubit[i])
            circuit.barrier()

            for i in range(n):
                circuit.cx(Alice_data[n - 1 - i], Alice_qubit[n - 1 - i])
                circuit.h(Alice_data[n - 1 - i])
            circuit.barrier()

            for i in range(n):
                circuit.measure(Alice_data[i], cr[i])

            for i in range(n):
                circuit.measure(Alice_qubit[i], cr[i])
            circuit.barrier()

            for i in range(n):
                circuit.cx(Alice_qubit[i], Bob_qubit[i])
                circuit.cz(Alice_data[i], Bob_qubit[i])
            circuit.barrier()

            for i in range(n):
                circuit.measure(Bob_qubit[i], cr[i])

            circuit.draw(output='text', filename='./cktart.txt')

            ''' Getting counts from backend '''
            simulator_backend = Aer.get_backend('qasm_simulator')
            result = execute(circuit, simulator_backend, shots=1).result()
            counts = result.get_counts()

            for key in counts:
                key_var = key
                a = key_var[len(key_var) - 8:]
                b = ''
                for i in range(len(a)):
                    b = b + a[(-i - 1)]
                counts_list.append(b)

            # print('.', end='')

        # print('\n Process completed !')
        QtWidgets.QMessageBox.information(self,"Quantum Data Feeder","File has been successfully Teleported")

        # print('\n Hurray!😊 you have successfully Teleporated entire File using Quantum Teleportation.')

        def decode_binary_string(s):
            return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))

        char_list = []
        for each in counts_list:
            a = decode_binary_string(each)
            char_list.append(a)

        modified_string = ''
        for each in char_list:
            for i in each:
                if (i == '@'):
                    each = each.replace('@', ',')
                    i = i + each
                if (i == '#'):
                    each = each.replace('#', ' ')
                    i = i + each
                if (i == '$'):
                    each = each.replace('$', '.')
                    i = i + each
            modified_string += each

        # print('The final output after Teleporting is : \n')
        # for each in modified_string:
        #     print(each, end='')

        file_name = 'Teleported_data.txt'
        f = open(file_name, 'w')  # open file in append mode
        for each in modified_string:
            f.write(each)
        f.close()

    def btn_verifyoutput_clicked(self):
        os.startfile('Teleported_data.txt')

    def btn_ckt_show_clicked(self):
        os.startfile('cktart.txt')