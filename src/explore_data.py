from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "sweden_immigration.csv"


df = pd.read_csv(DATA_PATH, encoding="cp1252")


print(df.head())

print("\nData Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Value:")
print(df.isnull().sum())

print("\nDublicate Rows:")
print(df.duplicated().sum())

print("\nNumber of unique countries:")
print(df["country of birth"].nunique())

print("\nFirst 20 countries:")
print(df["country of birth"].unique()[:20])