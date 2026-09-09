# Reused Day 17 normalization function

import re


def normalize_skill(raw_text, skill_lookup):
    text = str(raw_text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    if text in skill_lookup:
        return skill_lookup[text]

    stripped = re.sub(r"\b(programming|framework|language)\b", "", text).strip()
    if stripped in skill_lookup:
        return skill_lookup[stripped]

    return None