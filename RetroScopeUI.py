from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, QComboBox, QSizePolicy

class RetroScopeUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        scrollArea = QScrollArea()

        projectLabel = QLabel("Project:")
        projectCombo = QComboBox()
        projectCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        boardLabel = QLabel("Board:")
        boardCombo = QComboBox()
        boardCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        sprintLabel = QLabel("Sprint:")
        sprintCombo = QComboBox()
        sprintCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        topLayout.addWidget(projectLabel)
        topLayout.addWidget(projectCombo)
        topLayout.addWidget(boardLabel)
        topLayout.addWidget(boardCombo)
        topLayout.addWidget(sprintLabel)
        topLayout.addWidget(sprintCombo)


        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(scrollArea)
        self.setLayout(mainLayout)

        self.setWindowTitle("RetroScope")


