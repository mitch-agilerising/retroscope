from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,  QLabel, QComboBox, 
    QSizePolicy, QTreeView
)

class RetroScopeUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("RetroScope")

        mainLayout: QVBoxLayout = QVBoxLayout()
        topLayout: QVBoxLayout = QHBoxLayout()
        treeView: QTreeView = QTreeView()

        projectLabel: QLabel = QLabel("Project:")
        projectCombo: QComboBox = QComboBox()
        projectCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        boardLabel: QLabel = QLabel("Board:")
        boardCombo: QComboBox = QComboBox()
        boardCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        sprintLabel: QLabel = QLabel("Sprint:")
        sprintCombo: QComboBox = QComboBox()
        sprintCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        topLayout.addWidget(projectLabel)
        topLayout.addWidget(projectCombo)
        topLayout.addWidget(boardLabel)
        topLayout.addWidget(boardCombo)
        topLayout.addWidget(sprintLabel)
        topLayout.addWidget(sprintCombo)

        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(treeView)
        self.setLayout(mainLayout)
        
        model = QStandardItemModel(0, 4)
        headers = ["Assignee", "Day 1", "Day 2", "Day 3"]
        model.setHorizontalHeaderLabels(headers)

        model.appendRow(self.makeRow("Julius Alabaster", 0, 1, 2))
        model.appendRow(self.makeRow("Helene Trabene", 0, 1, 2))
        model.appendRow(self.makeRow("Oscar De Hoyos", 0, 1, 2))
        model.appendRow(self.makeRow("Sanda Keesman", 0, 1, 2))

        treeView.setModel(model);
        treeView.show()
        
    def makeRow(self, assignee, first, second, third) -> list[any]:
        row = []
        row.append(QStandardItem(assignee))
        row.append(QStandardItem(str(first)))
        row.append(QStandardItem(str(second)))
        row.append(QStandardItem(str(third)))
        return row