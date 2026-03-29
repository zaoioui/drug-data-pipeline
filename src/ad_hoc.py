import json

def get_journal_with_most_distinct_drugs(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    journal_to_drugs = {}

    for drug, content in data.items():
        for journal_item in content.get("journals", []):
            journal_name = journal_item.get("journal", "").strip()

            if not journal_name:
                continue

            if journal_name not in journal_to_drugs:
                journal_to_drugs[journal_name] = set()

            journal_to_drugs[journal_name].add(drug)

    if not journal_to_drugs:
        return None, 0

    best_journal = max(journal_to_drugs.items(), key=lambda x: len(x[1]))
    return best_journal[0], len(best_journal[1])


if __name__ == "__main__":
    journal, nb_drugs = get_journal_with_most_distinct_drugs("data/output/result.json")
    print("Journal avec le plus de médicaments différents :", journal)
    print("Nombre de médicaments différents :", nb_drugs)