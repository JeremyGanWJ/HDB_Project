# HDB Resale ETL Pipeline

## Prerequisites

Ensure the following software is installed:

* Python 3.11 or later
* Git (optional, for cloning the repository)
* JupyterLab or Jupyter Notebook (for running the demonstration notebook)

Verify your Python installation:

```bash
python --version
```

---

# Project Structure

```
HDB_Project/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── transformed/
│   ├── failed/
│   └── hashed/
│
├── notebook/
│   └── ETL_demo.ipynb
│
├── src/
│   ├── extract.py
│   ├── profiling.py
│   ├── validation.py
│   ├── cleaning.py
│   ├── transformation.py
│   ├── hashing.py
│   └── pipeline.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

# Installation

## Step 1 – Create a Virtual Environment


Windows:

```bash
python -m venv venv


a) Activate the virtual environment.

Windows Command Prompt:

```cmd
venv\Scripts\activate
```


## Step 2 – Install Required Packages

```bash
python -m pip install --upgrade pip
```or```
python -m pip install -r requirements.txt
```

---

# Input Data

Copy all HDB resale CSV files into the following directory:

```
data/raw/
```
```
Example:
Resale Flat Prices (Based on Approval Date), 1990 - 1999.csv
Resale Flat Prices (Based on Approval Date), 2000 - Feb 2012.csv
Resale Flat Prices (Based on Registration Date), From Jan 2015 to Dec 2016.csv
Resale Flat Prices (Based on Registration Date), From Mar 2012 to Dec 2014.csv
Resale flat prices based on registration date from Jan-2017 onwards.csv
```

---

# Running the ETL Pipeline

From the project root directory, execute:

```bash
python run.py
```

The pipeline will perform the following steps:

1. Read and combine all CSV files.
2. Perform data profiling.
3. Validate data quality.
4. Clean and standardize the dataset.
5. Remove duplicate records.
6. Calculate the remaining lease.
7. Generate the Resale Identifier.
8. Hash the Resale Identifier using SHA-256.
9. Save all output datasets.

---

# Running the Jupyter Notebook

Start JupyterLab:

```bash
jupyter lab
```

Open:

```
notebook/ETL_demo.ipynb
```

Run all cells from top to bottom.

The notebook demonstrates:

* Data extraction
* Data profiling
* Data validation
* Data cleaning
* Transformation
* Hashing
* Output generation

---

# Output Files

After successful execution, the following files will be generated.

## Raw

```
data/raw/
```

Contains the original input CSV files.

---

## Cleaned

```
data/cleaned/clean.csv
```

Contains records that passed all validation rules.

---

## Failed

```
data/failed/failed.csv
```

Contains records removed due to validation failures or duplicate composite keys.

---

## Transformed

```
data/transformed/transformed.csv
```

Contains the cleaned dataset with the generated Resale Identifier.

---

## Hashed

```
data/hashed/hashed.csv
```

Contains the transformed dataset with the SHA-256 hashed identifier.

---

# Expected Console Output

```
Loading resale_2012.csv
Loading resale_2013.csv
Loading resale_2014.csv
Loading resale_2015.csv
Loading resale_2016.csv

Data profiling completed.
Validation completed.
Duplicate records removed.
Remaining lease calculated.
Resale Identifier generated.
SHA-256 hashing completed.

ETL Pipeline completed successfully.
```

---

# Troubleshooting

## ModuleNotFoundError

Ensure all dependencies have been installed:

```bash
python -m pip install -r requirements.txt
```

---

## No CSV Files Found

Verify that the input files are located in:

```
data/raw/
```

---

## pandas Not Found

Install the required packages:

```bash
python -m pip install pandas
```

or

```bash
python -m pip install -r requirements.txt
```

---

# Notes

* The pipeline automatically combines all CSV files located in the `data/raw/` directory.
* Duplicate records are identified using the composite key (all columns except `resale_price`), with the record having the higher resale price retained.
* Remaining lease is recalculated based on a 99-year lease and the current execution date.
* The generated Resale Identifier is hashed using the SHA-256 algorithm.
* Output folders are created automatically if they do not already exist.
