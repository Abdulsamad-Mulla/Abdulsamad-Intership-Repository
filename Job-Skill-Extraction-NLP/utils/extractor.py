# Day 7 Reusable model
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAXONOMY_PATH = os.path.join(BASE_DIR, "data", "skill_taxonomy.csv")


def load_skill_list(taxonomy_path=TAXONOMY_PATH):
    tax = pd.read_csv(taxonomy_path)
    skill_lookup = {}
    category_lookup = {}
    for _, row in tax.iterrows():
        canonical = row["skill"]
        category = row["category"]
        skill_lookup[canonical.lower()] = canonical
        category_lookup[canonical] = category
        if isinstance(row["aliases"], str) and row["aliases"].strip():
            for alias in row["aliases"].split(";"):
                skill_lookup[alias.strip().lower()] = canonical
    return skill_lookup, category_lookup


def extract_skills(text, skill_lookup):
    text = str(text).lower()
    found = set()
    for term, canonical in skill_lookup.items():
        if term in text:
            found.add(canonical)
    return sorted(found)