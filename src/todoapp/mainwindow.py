from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import ( 
    QMainWindow, 
    QListWidget, 
    QListWidgetItem,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLineEdit,
    QAbstractItemView,
    QHBoxLayout
)
from operations import DataOps
from models import Tarea


class MainWindow(QMainWindow):
    '''
    To-Do App Main Window.
    '''
    def __init__(self):
        super().__init__()

        self.tasks = DataOps.get_tasks()

        self.setWindowTitle("To-Do App")
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.list_widget.setAlternatingRowColors(True)

        self.delete_button = QPushButton('Delete')
        self.complete_button = QPushButton('Toggle Done')
        self.line_edit = QLineEdit()
        self.add_button = QPushButton("Add Item")
        
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        buttons_layout = QHBoxLayout()
        layout.addLayout(buttons_layout)
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.complete_button)

        layout.addWidget(self.line_edit)
        layout.addWidget(self.add_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.init_tasks()

        self.list_widget.currentItemChanged.connect(self.list_item_checked)
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.complete_button.clicked.connect(self.mark_as_completed)

    def init_tasks(self) -> None:
        for task in self.tasks:
            item = QListWidgetItem()
            item.setText(task.definition)
            item.setFlags(
                item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            state = Qt.CheckState.Checked if \
                 task.completed else \
                    Qt.CheckState.Unchecked
            item.setCheckState(state)
            self.list_widget.addItem(item)

    def add_task(self) -> None:
        text = self.line_edit.text()
        if text:
            task = Tarea(text, False)
            self.tasks.append(task)
            item = QListWidgetItem()
            item.setText(task.definition)
            item.setFlags(
                item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.list_widget.addItem(item)
            self.line_edit.clear()
        DataOps.save_tasks(self.tasks)

    def delete_task(self):
        selected_index = self.list_widget.currentIndex()
        if selected_index:
            self.list_widget.takeItem(selected_index.row())
            self.tasks.pop(selected_index.row())
        DataOps.save_tasks(self.tasks)
    
    def mark_as_completed(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            item_index = self.list_widget.row(selected_item)
            new_state = Qt.CheckState.Unchecked if \
                 self.tasks[item_index].completed else \
                    Qt.CheckState.Checked
            selected_item.setCheckState(new_state)
            self.tasks[item_index].completed = not self.tasks[item_index].completed
        DataOps.save_tasks(self.tasks)

    def list_item_checked(self, new_item, old_item) -> None:
        pass