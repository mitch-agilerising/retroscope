from collections import defaultdict
import json
from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (
    QVBoxLayout, QTreeView
)
import sys

def create_stories_model(file_path: str) -> QStandardItemModel:
    """
    Loads story data from a JSON file and prepares a QStandardItemModel.

    The data is structured in a tree where top-level rows are assignees
    and child rows are the stories assigned to them.

    Args:
        file_path: The path to the JSON file.

    Returns:
        A populated QStandardItemModel instance.
    """
    # --- 1. Load and Group the JSON Data ---
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        # Return an empty model on error
        return QStandardItemModel()

    # Use defaultdict to easily group stories by assignee
    stories_by_assignee = defaultdict(list)
    for story in data:
        # Use .get() to avoid errors if a key is missing
        assignee = story.get("Assignee", "Unassigned")
        stories_by_assignee[assignee].append(story)

    # --- 2. Set up the Model ---
    model = QStandardItemModel()
    
    # Define the column headers
    headers = [
        'Title', 'Story ID', 'Points', 'Day 1', 'Day 2', 'Day 3', 
        'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10'
    ]
    model.setHorizontalHeaderLabels(headers)

    # --- 3. Populate the Model with Grouped Data ---
    root_item = model.invisibleRootItem()

    # Define a bold font for the top-level assignee names
    bold_font = QFont()
    bold_font.setBold(True)

    # Sort assignees alphabetically for consistent order
    for assignee, stories in sorted(stories_by_assignee.items()):
        # Create a top-level, non-editable item for the assignee
        assignee_item = QStandardItem(f"{assignee} ({len(stories)} stories)")
        assignee_item.setFont(bold_font)
        assignee_item.setEditable(False)
        
        # Add the assignee as a new row under the root
        root_item.appendRow([assignee_item])

        # Add each story as a child of the assignee item
        for story in stories:
            # Create a list of QStandardItems for the story's data
            row_items = [
                QStandardItem(story.get("Story ID", "")),
                QStandardItem(story.get("Title", "")),
                QStandardItem(str(story.get("Points", ""))),
            ]
            # Add status for each day
            for i in range(1, 11):
                day_status = story.get(f"Day {i}", "")
                row_items.append(QStandardItem(day_status))

            # Make all child items non-editable
            for item in row_items:
                item.setEditable(False)
            
            # Append the story row as a child of the assignee
            assignee_item.appendRow(row_items)
            
    return model

# --- Example Usage ---
if __name__ == '__main__':
    # You need a QApplication instance to handle fonts, but no window is needed

    app = QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.resize(850, 600)

    json_file_path = 'StoryData.json'
    story_model = create_stories_model(json_file_path)

    main_layout: QVBoxLayout = QVBoxLayout()
    tree_view: QTreeView = QTreeView()
    tree_view.setModel(story_model)
    main_layout.addWidget(tree_view)
    widget.setLayout(main_layout)
    widget.show()
    

    # Verification: Check if the model was populated correctly
    if story_model.rowCount() > 0:
        print(f"Successfully created the model from '{json_file_path}'.")
        print(f"Found {story_model.rowCount()} assignees (top-level items).")
        
        # Get the first assignee and check their stories
        first_assignee_index = story_model.index(0, 0)
        first_assignee_name = story_model.data(first_assignee_index)
        num_stories = story_model.rowCount(first_assignee_index)
        print(f"The first assignee '{first_assignee_name}' has {num_stories} stories.")
    else:
        print("Failed to create or populate the model.")

    sys.exit(app.exec())