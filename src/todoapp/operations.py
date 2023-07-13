from typing import Iterable
from models import Tarea
from storage import Storage

class DataOps:
    '''
    It collects main dato ops to serve storage contents in UI.
    '''
    @classmethod
    def transform_storage_to_data(cls, storage_data: dict) -> Iterable[Tarea]:
        return [Tarea(element, storage_data[element]) for element in storage_data]
 
    @classmethod
    def transform_data_to_storage(cls, data: Iterable[Tarea]) -> dict:
        return {element.definition: element.completed for element in data}

    @classmethod
    def get_tasks(cls) -> Iterable[Tarea]:
        storage_data = Storage.read()
        return cls.transform_storage_to_data(storage_data)

    @classmethod
    def save_tasks(cls, tasks) -> None:
        data = cls.transform_data_to_storage(tasks)
        Storage.write(data)