def match_drugs(drugs_df, df, title_col, source_name):
    results = []

    drugs = drugs_df["drug"].dropna().str.lower().str.strip().tolist()

    for _, row in df.iterrows():
        title = str(row.get(title_col, "")).lower().strip()
        journal = str(row.get("journal", "")).strip()
        date = str(row.get("date", "")).strip()
        publication_id = str(row.get("id", "")).strip()

        for drug in drugs:
            if drug in title:
                results.append({
                    "drug": drug,
                    "source": source_name,
                    "id": publication_id,
                    "title": title,
                    "journal": journal,
                    "date": date
                })

    return results