from PySide6 import  QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPainter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,  QLabel, QComboBox, 
    QSizePolicy, QTreeView, QHeaderView, QStyledItemDelegate
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
        
        self.model = QStandardItemModel(0, 1)
        headers = ["Assignee"]
        for i in range(1, 11):
            headers.append("Day " + str(i))
        self.model.setHorizontalHeaderLabels(headers)

        self.model.appendRow(self.makeRow("Julius Alabaster", list(range(1, 11))))
        self.model.appendRow(self.makeRow("Helene Trabene", list(range(1, 11))))
        self.model.appendRow(self.makeRow("Oscar De Hoyos", list(range(1, 11))))
        self.model.appendRow(self.makeRow("Sanda Keesman", list(range(1, 11))))

        n = Qt
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
        treeView.setModel(self.model);
        treeView.setItemDelegate(TreeViewDelegate())
        treeView.setStyleSheet("QTreeView::item { height: 50px; }")

        header = treeView.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(0, 150)
        for i in range(1, 11):
            header.resizeSection(i, 50)

        treeView.show()
        
    def makeRow(self, assignee, values) -> list[any]:
        row = []
        row.append(QStandardItem(assignee))
        
        for i in range(1,11):
            row.append(QStandardItem(str(i)))
        return row
    
class TreeViewDelegate(QStyledItemDelegate):

    def paint(self, painter: QPainter, option, index):
        super().paint(painter, option, index)
        #print(f"{index} -{option}")
        return