from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPainter, QColorConstants
from PySide6.QtCore import Qt, QModelIndex, QRect
from ImportJSON import create_stories_model
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout,  QLabel, QComboBox, 
    QSizePolicy, QTreeView, QHeaderView, QStyledItemDelegate,
    QStyleOptionViewItem
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
        
        json_file_path = 'StoryData.json'
        self.model = create_stories_model(json_file_path)

        treeView.setModel(self.model);
        treeView.setItemDelegate(TreeViewDelegate())
        treeView.setStyleSheet("QTreeView::item { height: 24px; }")

        header = treeView.header()
        header.resizeSection(0, 220)
        header.resizeSection(1, 80)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)


        for i in range(2, 13):
            header.resizeSection(i, 50)
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Fixed)
        treeView.expandAll()
        treeView.setItemsExpandable(False)
        treeView.show()
    
class TreeViewDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option, index):
        modelIndex: QModelIndex = index;
        if (modelIndex.column() == 2):
            option.displayAlignment = Qt.AlignmentFlag.AlignCenter
        elif (modelIndex.column() > 2):
            if (self.paint_color(painter, option, modelIndex)):
                return
        super().paint(painter, option, index)
        return
    
    def paint_color(self, painter: QPainter, 
                    option: QStyleOptionViewItem, index: QModelIndex) -> bool :
        cell_text = index.data(Qt.ItemDataRole.DisplayRole)
        newRect: QRect = option.rect.adjusted(0, 0, -1, -1)
        if (cell_text == "Done"):
            painter.fillRect(newRect, QColorConstants.Black)
            return True
        elif (cell_text == "In Progress"):
            painter.fillRect(newRect, QColorConstants.DarkGreen)
            return True
        elif (cell_text == "In Review"):
            painter.fillRect(newRect, QColorConstants.Blue)
            return True
        elif (cell_text == "Blocked"):
            painter.fillRect(newRect, QColorConstants.Red)
            return True
        elif (cell_text == "To Do"):
            # do not paint
            return True
        return False