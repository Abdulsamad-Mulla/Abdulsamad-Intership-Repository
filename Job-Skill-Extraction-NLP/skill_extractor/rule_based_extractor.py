
import os
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))          # .../skill_extractor
DATA_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "data"))  # .../Job_Skill_Extraction/data

CLEAN_JOBS_PATH = os.path.join(DATA_DIR, "clean_jobs.csv")
TAXONOMY_PATH = os.path.join(DATA_DIR, "skill_taxonomy.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "rule_based_skills.csv")


def load_skill_list(taxonomy_path=TAXONOMY_PATH):
    
    if not os.path.exists(taxonomy_path):
        raise FileNotFoundError(
            f"Could not find skill_taxonomy.csv at: {taxonomy_path}\n"
            f"Check that the file actually exists there — this script looks "
            f"for it next to itself in ../data, regardless of your current "
            f"working directory."
        )
    tax = pd.read_csv(taxonomy_path)
    skill_lookup = {}
    for _, row in tax.iterrows():
        canonical = row["skill"]
        skill_lookup[canonical.lower()] = canonical
        if isinstance(row["aliases"], str) and row["aliases"].strip():
            for alias in row["aliases"].split(";"):
                skill_lookup[alias.strip().lower()] = canonical
    return skill_lookup


def extract_skills(text, skill_lookup):
    
    text = str(text).lower()
    found = set()
    for term, canonical in skill_lookup.items():
        if term in text:
            found.add(canonical)
    return sorted(found)


def main():
   
    print(f"Reading clean jobs from: {CLEAN_JOBS_PATH}")
    if not os.path.exists(CLEAN_JOBS_PATH):
        raise FileNotFoundError(
            f"Could not find clean_jobs.csv at: {CLEAN_JOBS_PATH}\n"
            f"Check that the file actually exists there — this script looks "
            f"for it next to itself in ../data, regardless of your current "
            f"working directory."
        )
    df = pd.read_csv(CLEAN_JOBS_PATH)

    skill_lookup = load_skill_list(TAXONOMY_PATH)

    df["rule_based_skills"] = df["clean_description"].apply(
        lambda t: extract_skills(t, skill_lookup)
    )
    df["rule_based_skill_count"] = df["rule_based_skills"].apply(len)

    print("Sample extraction:")
    for i in range(3):
        print(f"- {df['job_title'].iloc[i]}: {df['rule_based_skills'].iloc[i]}")

    print("\nAverage skills found per job:", df["rule_based_skill_count"].mean().round(2))
    print("Jobs with zero skills matched:", (df["rule_based_skill_count"] == 0).sum())

    out = df[["job_id", "job_title", "rule_based_skills", "rule_based_skill_count"]]
    out.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
