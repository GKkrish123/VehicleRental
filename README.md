# VEHICLE RENTAL APP (Python/FastAPI)

* This project contains APIs related to features of the VEHICLE RENTAL APP.

* Setting up the environment
  1. Visual Studio Code (`https://code.visualstudio.com/download`)
  2. Python (`https://www.python.org/downloads/`)
  3. SQL Server (Example: PostgreSQL,SQLite) (Tested with PostgreSQL)
  4. Clone this repository into VSCode, open the CMD terminal in the installed path (inside the `VehicleRental` folder)
  5. Install `pipenv` by running the command `pip install pipenv`
  5. Create virtual environment by running the command `pipenv shell`
  6. Run the command `pipenv install --dev --skip-lock` to install all Python dependencies.

* Creating the mock database tables (MANDATORY IF YOU DON'T HAVE THE SPECIFIED TABLES IN YOUR SQL SERVER)
  1. Start your local SQL server.
  2. Apply your SQL server configuration in the `config.py`.
  3. Run the command `python mock_db_tables.py` to create the mock tables in your specified SQL server.

# Deploying the APP server
  * Run the command `python startup.py` to start the app.
    * http://localhost:5000/docs -> Swagger URL
    * http://localhost:5000/redoc -> Documentation URL
