# Dagster Project: Fetch ABIs using I/O Manager

This Dagster project demonstrates a data pipeline that reads contract addresses from a CSV file containing 500 contract addresses. It utilizes an IO manager to read and write CSV file values to the file system. The pipeline fetches ABI data for each contract address and saves the results into another CSV file. The project consists of the following files:

* asset.py : This file contains the code to fetch the ABIs and also defines asset.
* init.py : This file defines the jobs and schedules that are used by the project.

## Features

* The project can fetch ABIs (Application Binary Interfaces) for 500 contract addresses from the Etherscan API.
* It reads the contract addresses from a CSV file and saves the fetched ABIs to a CSV file in the file system with the help of I/O Manager.
* The project includes a scheduled pipeline that is configured to run automatically every hour.
* The pipeline consists of a predefined job and schedule, ensuring regular execution and data updates.
* A sensor is implemented to periodically check for changes to the contract API assets. It monitors the assets at a 30-second interval and triggers pipeline execution when changes are detected.
* The project uses the File System I/O Manager, allowing it to store the fetched ABIs in a directory called 'data' on the local file system. This provides a more permanent and accessible location     for the data.

## Setup

To run the project, you will need to have Dagster installed (installation instructions: https://docs.dagster.io/getting_started/installation). Once you have Dagster installed in your python local environment, you can run the project by following these steps:

1. Clone the repository or download the project files.

2. Install the dependencies

pip install -e ".[dev]"

    Note: Don't forget to import, install necessary packages

pip install package_name

3. The input CSV file is already placed in the data directory named address.csv, this CSV file contains one column named "ADDRESS" that holds the contract addresses.

4. Run the command

dagster dev

This will start the Dagster UI on your local machine. You can then use the UI to interact with the project.

Open your web browser and navigate to http://localhost:3000 to access the Dagster UI.

Click on the Materialize in the Dagster UI and execute it. Monitor the pipeline execution in the Dagster web UI. Once completed, the fetch_api.csv file in the data directory will contain the fetched ABI data.
