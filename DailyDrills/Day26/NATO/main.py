import pandas as pd
from typing import List, Any

def read_csv_to_dict(file_path: str,
                     key_col: str = "letter",
                     value_col: str = "code",
                     skipinitialspace: bool = False) -> dict:
    """
    Read CSV from file_path and return a mapping dict {key: value}.
    - Only accepts a file path
    - Trims whitespace from headers and string cells.
    - If duplicate keys exist, later rows overwrite earlier ones (pandas behavior).
    """
    try:
        df = pd.read_csv(file_path, skipinitialspace=skipinitialspace)
    except FileNotFoundError:
        print(f"Error Happened : The Csv file is not found")
        return {}
        # Normalize column names -- cleaning
    df.columns = df.columns.str.strip()

    try:
        if key_col not in df.columns or value_col not in df.columns:
            raise ValueError(f"CSV must contain columns '{key_col}' and '{value_col}'. Found: {list(df.columns)}")

        keys = df[key_col].astype(str).str.strip().tolist()
        vals = df[value_col].astype(str).str.strip().tolist()
        mapping = {k: v for k, v in zip(keys, vals)}
        return mapping
    except ValueError as e:
        print(f"Error: {e}")
        return {}

def parse_letters_input(s: str) -> List[str]:
    """
    Parse a user string into tokens preserving order and duplicates.
    Supported: "A,B,C", "A B C", "ABC" -> ['A','B','C']
    Single-character tokens are normalized to uppercase.
    """
    if not s:
        return []
    s = s.strip()
    if "," in s:
        parts = [p.strip() for p in s.split(",") if p.strip()]
    elif " " in s:
        parts = [p.strip() for p in s.split() if p.strip()]
    else:
        parts = list(s)

    # Normalize tokens (list comprehension example)
    tokens = [p.upper() if len(p.strip()) == 1 else p.strip() for p in parts]
    return tokens

def lookup_values_from_csv(file_path: str,
                           letters_input: str,
                           key_col: str = "letter",
                           value_col: str = "code",
                           skipinitialspace: bool = False,
                           allow_missing: bool = True,
                           missing_value: Any = None) -> List[Any]:
    """
    One-shot helper:
    - reads CSV -> mapping
    - parses letters_input -> tokens
    - returns a LIST of values in input order, preserving duplicates.

    If allow_missing is False, a missing key raises KeyError.
    If allow_missing is True, missing keys are replaced with missing_value.
    """
    mapping = read_csv_to_dict(file_path, key_col=key_col, value_col=value_col, skipinitialspace=skipinitialspace)
    tokens = parse_letters_input(letters_input)

    # Use list comprehension for the lookup (preserves order & duplicates).
    # We use mapping.get for placeholder behavior, then optionally enforce no-missing policy.
    result = [mapping.get(t, missing_value) for t in tokens]

    if not allow_missing:
        # detect first missing and raise with informative message
        missing_tokens = [t for t, v in zip(tokens, result) if v is missing_value or t not in mapping]
        if missing_tokens:
            raise KeyError(f"Keys not found in CSV mapping: {missing_tokens}")

    # Filtering out None Values before returning
    return [v for v in result if v is not None]


if __name__ == "__main__":
    try:
        letters = input("Enter your name: ").strip()
        values = lookup_values_from_csv(
            'nato_phonetic_alphabet.csv',  # Fixed typo
            letters,
            skipinitialspace=True,
            allow_missing=True,
            missing_value=None
        )
        print("Nato Phonetic List:", values)
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"Error processing request: {e}")