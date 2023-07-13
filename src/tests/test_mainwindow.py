import pytest
from PyQt6.QtWidgets import QApplication
from todoapp.mainwindow import MainWindow
from pytest import MonkeyPatch

@pytest.fixture(scope="function")
def setup():
    app = QApplication([])
    yield app
    app.quit()

def test_add_task(setup):
    # Configurar
    main_window = MainWindow()

    # Ejecutar
    main_window.line_edit.setText("Task 1")
    main_window.add_button.click()

    # Comprobar
    assert len(main_window.tasks) == 1
    assert main_window.list_widget.count() == 1
    assert main_window.list_widget.item(0).text() == "Task 1"

def test_delete_task(monkeypatch: MonkeyPatch):
    pass 