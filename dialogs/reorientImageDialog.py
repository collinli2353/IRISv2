import sys

import PySide6
from PySide6 import QtWidgets
from qt_material import *

from dialogs.ui_ReorientImage import *
from utils.globalConstants import IMG_OBJ

class ReorientImageDialog(PySide6.QtWidgets.QDialog):
    reorient_choices = [
        'Superior to Inferior',
        'Posterior to Anterior',
        'Left to Right',
        'Right to Left',
        'Anterior to Posterior',
        'Inferior to Superior'
    ]

    letter_mapping = ['S', 'P', 'L', 'R', 'A', 'I']
    possible_combos = ['LSA', 'LSI', 'LPA', 'LPI', 'RSA', 'RSI', 'RPA', 'RPI']

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_ReorientImage_Widget()
        self.ui.setupUi(self)

        self.IMG_OBJ = IMG_OBJ()

        self.ui.currentVoxelXAxis_comboBox.addItems(self.reorient_choices)
        self.ui.currentVoxelYAxis_comboBox.addItems(self.reorient_choices)
        self.ui.currentVoxelZAxis_comboBox.addItems(self.reorient_choices)

        self.ui.newVoxelXAxis_comboBox.addItems(self.reorient_choices)
        self.ui.newVoxelYAxis_comboBox.addItems(self.reorient_choices)
        self.ui.newVoxelZAxis_comboBox.addItems(self.reorient_choices)

        self.ui.newVoxelXAxis_comboBox.currentTextChanged.connect(self.updateNewVoxelXAxis)
        self.ui.newVoxelYAxis_comboBox.currentTextChanged.connect(self.updateNewVoxelYAxis)
        self.ui.newVoxelZAxis_comboBox.currentTextChanged.connect(self.updateNewVoxelZAxis)

        self.ui.voxelXAxis_button.clicked.connect(self.IMG_OBJ.swapVoxelXAxis)
        self.ui.voxelZAxis_button.clicked.connect(self.IMG_OBJ.swapVoxelZAxis)
        self.ui.voxelYAxis_button.clicked.connect(self.IMG_OBJ.swapVoxelYAxis)

        self.ui.newNIFTI_tableView.setHorizontalHeaderLabels(['X', 'Y', 'Z', 'W'])

    def updateRaiCode(self, text):
        print(len(text) == 3)
        if len(text) == 3:
            self.ui.newRaiCode_textEdit.setText(text)
            self.ui.newVoxelXAxis_comboBox.setCurrentIndex(self.letter_mapping.index(text[0]))
            self.ui.newVoxelYAxis_comboBox.setCurrentIndex(self.letter_mapping.index(text[1]))
            self.ui.newVoxelZAxis_comboBox.setCurrentIndex(self.letter_mapping.index(text[2]))

            if not self.IMG_OBJ.CURRENT_RAI_CODE[0] == text[0]:
                self.swapVoxelXAxis()
            if not self.IMG_OBJ.CURRENT_RAI_CODE[1] == text[1]:
                self.swapVoxelYAxis()
            if not self.IMG_OBJ.CURRENT_RAI_CODE[2] == text[2]:
                self.swapVoxelZAxis()

            self.IMG_OBJ.CURRENT_RAI_CODE = text
        else:
            self.ui.newRaiCode_textEdit.setText('###')

    def updateNewVoxelXAxis(self, text):
        currentRaiCode = self.letter_mapping[self.ui.newVoxelXAxis_comboBox.currentIndex()] + self.ui.raiCode_label.text()[1] + self.ui.raiCode_label.text()[2]
        self.updateRaiCode(currentRaiCode)

    def updateNewVoxelYAxis(self, text):
        currentRaiCode = self.ui.raiCode_label.text()[0] + self.letter_mapping[self.ui.newVoxelYAxis_comboBox.currentIndex()] + self.ui.raiCode_label.text()[2]
        self.updateRaiCode(currentRaiCode)

    def updateNewVoxelZAxis(self, text):
        currentRaiCode = self.ui.raiCode_label.text()[0] + self.ui.raiCode_label.text()[1] + self.letter_mapping[self.ui.newVoxelZAxis_comboBox.currentIndex()]
        self.updateRaiCode(currentRaiCode)

    def exec(self):
        print(self.IMG_OBJ.CURRENT_RAI_CODE[0] + self.IMG_OBJ.CURRENT_RAI_CODE[1] + self.IMG_OBJ.CURRENT_RAI_CODE[2])
        if self.IMG_OBJ.CURRENT_RAI_CODE:
            self.updateRaiCode(self.IMG_OBJ.CURRENT_RAI_CODE[0] + self.IMG_OBJ.CURRENT_RAI_CODE[1] + self.IMG_OBJ.CURRENT_RAI_CODE[2])
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReorientImageDialog()
    sys.exit(app.exec())
