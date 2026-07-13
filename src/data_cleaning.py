from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "sweden_immigration.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "cleaned_immigration.csv"


df = pd.read_csv(DATA_PATH, encoding="cp1252")


df = df.rename(
    columns={
        "country of birth": "country",
        "sex": "sex",
        "year": "year",
        "observations": "migration_type",
        "Immigrations and emigrations": "count"
    }
)



df["sex"] = df["sex"].replace({
    "men": "Men",
    "women": "Women"
})


df["migration_type"] = df["migration_type"].replace({
    "Immigrations": "Immigration",
    "Emigrations": "Emigration"
})


print("\nRows with 'total':")
print(df[df["country"] == "total"].shape[0])

print("\nRows eith unknown county:")
print(df[df["country"] == "unknown country of birth"].shape[0])


df = df[
    (df["country"] != "total") &
    (df["country"] != "unknown country of birth")
]


print("\nRemaining rows:")
print(len(df))

print("\nRemaining countries:")
print(df["country"].nunique())


df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned data saved!")
print(f"Location: {OUTPUT_PATH}")