from todoapp.operations import DataOps
from todoapp.models import Tarea


def test_transform_data_to_storage_is_correct_dicctionary():
    task_list = []
    for idx in range(100):
        task = Tarea(definition=f'Tarea {idx}', completed=False)
        task_list.append(task)
    
    result = DataOps.transform_data_to_storage(task_list)
    for task in task_list:
        assert task.definition in result
        assert result[task.definition] == task.completed

def test_transform_storage_to_data_is_correct_list():
    data_dict = {}
    for idx in range(100):
        data_dict[f"Tarea {idx}"] = False
    result = DataOps.transform_storage_to_data(data_dict)
    for task in result:
        assert task.definition in data_dict
        assert data_dict[task.definition] == task.completed

# def test_get_tasks_is_correct():
#     pass