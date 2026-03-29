def normalize_text(text):
    if isinstance(text, str):
        return text.lower().strip()
    return ""

def clean_dataframe(df, col):
    df[col] = df[col].apply(normalize_text)
    return df