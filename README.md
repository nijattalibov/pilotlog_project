# pilotlog_project
# PilotLog Documentation

## Setup Instructions

### Environment Setup
1. Ensure Python is installed on your system.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
### Prepare the Django application:
```bash
python manage.py migrate
 ```

### Running the Application:
To process data, use the following command:
  ```bash
  python manage.py manage_data "files/import - pilotlog_mcc.json" --csv_path "files/export - logbook_template.csv"
  ```
This command reads data from a JSON file (pilotlog_mcc.json) and exports it into an Excel format using a template (logbook_template.csv). 

### Overview of Functionality
Data Import: The application can read data from specified JSON files.
Data Export: After processing, it exports the data into a structured Excel file based on a predefined template.
Command Line Interface: The application is primarily interacted with through command-line arguments that specify file paths for import and export.

### Custom Modules
my_modules: This directory could contain customized logic for reading from JSON, processing data, and formatting the output for Excel export.
