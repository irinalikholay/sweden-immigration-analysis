### SWEDEN IMMIGRATION ANALYSIS ###

This project analyzes immigration trends in Sweden using official public data. 
The goal is to expore how immigration has changes since 2000, identify long-term trends , analyze countries of origin , regional distribution and demographic patterns using SQL, Python and data visualization.

# Source:
Statistic Sweden (SCB)

The dataset contains official migration statistic covering immigration and emigration by year, country of birth, sex, age and region.

## Data Exploration ##
The raw dataset was explored using Python and Pandas before the data cleaning.

Exploration Summary:
- Total records: 20,900
- Columns: 5
- Time period: 2000-2024
- Missing values: 0
- Duplicate rows: 0
- Unique countries: 209

## Data Cleaning ##

The raw dataset was cleaned and standardized before loading it into the database.

The following tasks were completed:
- Rename columns to use clear and consistent names.
- Standardized categorical value:
   - `men` - `Men``
   - `women` - `Women`
   - `Immigrations` - `Immigration`
   - `Emigrations` - `Emigration`
- Removed aggregated rows where the country was `total`
- Removed rows with `unknown country of birth`
- Verified data types
- Saved the clean dataset `data/processed/cleaned_immigration.csv`

# Cleaning Summary
- Rows:
    Before: 20,900
    After: 20,700
- Countries:
    Before: 209
    After: 207
- Missng values: 0
- Dublicate Rows: 0
