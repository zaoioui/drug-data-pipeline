import pandas as pd
import json

def load_csv(path):
    return pd.read_csv(path)

def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)