import json
import os

class Storage:
    '''
    Data storage operations.
    It accepts configuration through "storage_type" class attribute.
    It accept Json or CsV backends.
    '''
    file_name = 'storage.json'
    storage_type = "JSON"

    @classmethod
    def store_in_json(cls, data: dict) -> None:
        with open(cls.file_name, 'w', encoding="utf-8") as file:
            json.dump(data, file)
        
    @classmethod
    def retrieve_from_json(cls) -> dict:
        if os.path.exists(cls.file_name):
            with open(cls.file_name, 'r') as file:
                data = json.load(file)
            return data
        return {}

    @classmethod
    def store_in_csv(cls) -> None:
        pass

    @classmethod
    def retrieve_from_csv(cls) -> dict:
        pass

    @classmethod
    def storage_config_mapper(cls) -> dict:
        ''''
        It holds a mapper to be used in more wide calls to storage usage.
        '''
        mapper = {
            "JSON": {
                "read": cls.retrieve_from_json,
                "write": cls.store_in_json
            },
            "CSV": {
                "read": cls.retrieve_from_csv,
                "write": cls.store_in_csv
            }
        }
        return mapper
    
    @classmethod
    def read(cls) -> dict:
        return cls.storage_config_mapper()[cls.storage_type]["read"]()

    @classmethod
    def write(cls, data) -> None:
        return cls.storage_config_mapper()[cls.storage_type]["write"](data)