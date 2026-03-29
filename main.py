import json
import pandas as pd

from src.ingestion import load_csv, load_json
from src.transformation import clean_dataframe
from src.matching import match_drugs
from src.graph import build_drug_graph

# Load data
drugs = load_csv("data/raw/drugs.csv")
pubmed_csv = load_csv("data/raw/pubmed.csv")
pubmed_json = load_json("data/raw/pubmed.json")
clinical = load_csv("data/raw/clinical_trials.csv")

# Standardize columns
clinical = clinical.rename(columns={"scientific_title": "title"})

# Clean text
drugs["drug"] = drugs["drug"].astype(str).str.lower().str.strip()

pubmed_csv = clean_dataframe(pubmed_csv, "title")
pubmed_json = clean_dataframe(pubmed_json, "title")
clinical = clean_dataframe(clinical, "title")

# Merge PubMed sources
pubmed_all = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)

# Match drugs
pubmed_matches = match_drugs(drugs, pubmed_all, "title", "pubmed")
clinical_matches = match_drugs(drugs, clinical, "title", "clinical_trials")

# Build graph
drug_graph = build_drug_graph(pubmed_matches, clinical_matches)

# Save output
with open("data/output/result.json", "w", encoding="utf-8") as f:
    json.dump(drug_graph, f, indent=2, ensure_ascii=False)

print(" Graph JSON généré avec succès")