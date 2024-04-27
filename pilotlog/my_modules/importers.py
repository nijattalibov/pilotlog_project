import json
import keyword
from django.core.exceptions import ImproperlyConfigured
from django.db import transaction
from django.apps import apps
import chardet  # Import chardet for encoding detection

def import_from_json(json_path):
    """
    Imports data from a specified JSON file into the corresponding Django models.

    This function reads a JSON file where each entry contains a 'table' key to indicate
    the target Django model, and a 'meta' key with a dictionary of data to be loaded into
    the model. It transforms all field names to lowercase and prefixes any Django model
    reserved keywords with an underscore to avoid conflicts. Each model entry is created
    in the database within an atomic transaction, ensuring that all entries are either
    committed successfully or rolled back in case of an error.

    Args:
        json_path (str): The filesystem path to the JSON file containing the data.

    Raises:
        ImproperlyConfigured: If the JSON file is not found, or there's a KeyError indicating
                              a missing required field in the data, or if any other exceptions
                              occur that indicate the data could not be processed correctly.
                              This includes issues like the 'table' key missing, which would
                              result in not being able to resolve the model, or any issue
                              accessing the file.

    Examples:
        # Given a JSON file at '/path/to/data.json' with the following content:
        # [
        #     {"table": "Aircraft", "meta": {"make": "Cessna", "model": "172"}},
        #     {"table": "Pilot", "meta": {"name": "John Doe", "license": "12345"}}
        # ]
        # This would create instances of the Aircraft and Pilot models.

        import_from_json('/path/to/data.json')
    """
    try:
        with open(json_path, 'rb') as file:  # Read in binary mode
            raw_data = file.read()
            encoding = chardet.detect(raw_data)['encoding']  # Detect encoding
            data = json.loads(raw_data.decode(encoding))  # Decode the data
            with transaction.atomic():
                for entry in data:
                    model_name = entry.get('table')
                    if not model_name:
                        continue  # or raise an exception if necessary
                    Model = apps.get_model('pilotlog', model_name)
                    field_mapping = {}
                    for key in entry['meta'].keys():
                        adjusted_key = key.lower()
                        if keyword.iskeyword(adjusted_key):
                            adjusted_key = f"_{adjusted_key}"
                        field_mapping[key] = adjusted_key

                    model_fields = {field_mapping[k]: v for k, v in entry['meta'].items() if k in field_mapping}
                    Model.objects.create(**model_fields)
    except FileNotFoundError:
        raise ImproperlyConfigured("The specified JSON file was not found.")
    except KeyError as e:
        raise ImproperlyConfigured(f"Missing field in JSON data: {e}")
    except Exception as e:
        raise ImproperlyConfigured(f"An error occurred: {str(e)}")
