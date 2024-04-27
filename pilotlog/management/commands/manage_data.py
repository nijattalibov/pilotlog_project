from django.core.management.base import BaseCommand
from pilotlog.my_modules.importers import import_from_json
from pilotlog.my_modules.exporters import export_models_to_csv


class Command(BaseCommand):
    help = 'Imports data from JSON and optionally exports to CSV'

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str, help='Path to the JSON file')
        parser.add_argument('--csv_path', type=str, help='Path to the CSV export')

    def handle(self, *args, **options):
        json_path = options['json_path']
        csv_path = options['csv_path']

        # Import data
        import_from_json(json_path)
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))

        # Export data to CSV if requested
        model_fields = {
            'Aircraft': ['aircraftcode', 'fnpt', 'devicecode', 'record_modified', 'make', 'model', 'category', '_class', 'model', 'model', 'model', 'model', 'model', 'model'],
            'Flight': ['datebase', 'aircraftcode', 'arrcode', 'depcode', 'route', 'totimeutc', 'arrtimeutc', 'baseoffset', 'deptimeutc', 'ldgtimeutc', 'fuelplanned']
        }
        export_models_to_csv(csv_path,model_fields)
        self.stdout.write(self.style.SUCCESS(f'Successfully exported data to {csv_path}'))
