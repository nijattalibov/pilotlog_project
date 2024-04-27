import csv
from django.apps import apps

def export_models_to_csv(file_path,model_fields):
    """
    Exports data from the Aircraft and Flight models into a single CSV file with sections for each model.
    """

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

         # Write the header for the general section
        writer.writerow(["ForeFlight Logbook Import"])  # Section header

        # Optionally add a blank line between sections
        writer.writerow([])
        
        for model_name, fields in model_fields.items():
            # Write the header for the current model section
            writer.writerow([model_name + ' Table'])  # Section header
            writer.writerow(fields)  # Field names as headers

            # Get model class from apps
            Model = apps.get_model('pilotlog', model_name)

            # Query all instances of the model
            instances = Model.objects.all()

            # Write data rows
            for instance in instances:
                writer.writerow([getattr(instance, field) for field in fields])

            # Optionally add a blank line between sections
            writer.writerow([])


