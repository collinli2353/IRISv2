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

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_ReorientImage_Widget()
        self.ui.setupUi(self)

        self.IMG_OBJ = IMG_OBJ

        self.ui.currentVoxelXAxis_comboBox.addItems(self.reorient_choices)
        self.ui.currentVoxelYAxis_comboBox.addItems(self.reorient_choices)
        self.ui.currentVoxelZAxis_comboBox.addItems(self.reorient_choices)

        self.ui.newVoxelXAxis_comboBox.addItems(self.reorient_choices)
        self.ui.newVoxelYAxis_comboBox.addItems(self.reorient_choices)
        self.ui.newVoxelZAxis_comboBox.addItems(self.reorient_choices)

        self.ui.newVoxelXAxis_comboBox.currentTextChanged.connect(self.updateNewVoxelXAxis)
        self.ui.newVoxelYAxis_comboBox.currentTextChanged.connect(self.updateNewVoxelYAxis)
        self.ui.newVoxelZAxis_comboBox.currentTextChanged.connect(self.updateNewVoxelZAxis)

        def flipAxial():
            self.IMG_OBJ.FLIP[0] = not self.IMG_OBJ.FLIP[0]
            print(self.IMG_OBJ.FLIP)

        self.ui.voxelXAxis_button.clicked.connect(lambda: flipAxial)

        self.ui.newNIFTI_tableView.setHorizontalHeaderLabels(['X', 'Y', 'Z', 'W'])

    def updateRaiCode(self, text):
        if(len(text == 3)):
            self.ui.raiCode_label.setText(text)
            self.ui.newVoxelXAxis_comboBox.setCurrentIndex(self.letter_mapping.index(text[0]))
            self.ui.newVoxelYAxis_comboBox.setCurrentIndex(self.letter_mapping.index(text[1]))
            self.ui.newVoxelZAxis_comboBox.setCurrentIndex(self.letter_mapping.index(text[2]))

    def updateNewVoxelXAxis(self, text):
        currentRaiCode = self.letter_mapping[self.ui.newVoxelXAxis_comboBox.currentIndex()] + self.ui.raiCode_label.text()[1:]
        self.updateRaiCode(currentRaiCode)

    def updateNewVoxelYAxis(self, text):
        currentRaiCode = self.ui.raiCode_label.text()[0] + self.letter_mapping[self.ui.voxelYAxis_comboBox.currentIndex()] + self.ui.raiCode_label.text()[2:]
        self.updateRaiCode(currentRaiCode)

    def updateNewVoxelZAxis(self, text):
        print(text)
        currentRaiCode = self.ui.raiCode_label.text()[0] + self.ui.raiCode_label.text()[1] + self.letter_mapping[self.ui.voxelYAxis_comboBox.currentIndex()]
        self.updateRaiCode(currentRaiCode)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReorientImageDialog()
    sys.exit(app.exec())
