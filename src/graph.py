def build_drug_graph(pubmed_matches, clinical_matches):
    graph = {}

    all_matches = pubmed_matches + clinical_matches

    for match in all_matches:
        drug = match["drug"]

        if drug not in graph:
            graph[drug] = {
                "pubmed": [],
                "clinical_trials": [],
                "journals": []
            }

        publication_entry = {
            "id": match["id"],
            "title": match["title"],
            "journal": match["journal"],
            "date": match["date"]
        }

        journal_entry = {
            "journal": match["journal"],
            "date": match["date"]
        }

        if match["source"] == "pubmed":
            if publication_entry not in graph[drug]["pubmed"]:
                graph[drug]["pubmed"].append(publication_entry)

        elif match["source"] == "clinical_trials":
            if publication_entry not in graph[drug]["clinical_trials"]:
                graph[drug]["clinical_trials"].append(publication_entry)

        if journal_entry not in graph[drug]["journals"]:
            graph[drug]["journals"].append(journal_entry)

    return graph