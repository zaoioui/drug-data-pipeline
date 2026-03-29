# Drug Data Pipeline

## 🎯 Objective

Build a data pipeline that links drugs with their mentions in scientific publications.

## 🧱 Project Structure

* `data/raw`: input files
* `data/output`: generated JSON
* `src`: pipeline scripts

## ⚙️ How to run

Install dependencies:

```
pip install pandas
```

Run the pipeline:

```
python main.py
```

## 📊 Output

The pipeline generates a JSON file that links:

* drugs
* publications (PubMed & Clinical Trials)
* journals
* dates

## 🔍 Ad-hoc analysis

Run:

```
python src/ad_hoc.py
```

This returns the journal mentioning the highest number of distinct drugs.

## 🧠 Notes

* Drug detection is based on title matching
* Data is cleaned and normalized (lowercase)
* Duplicate entries are removed
