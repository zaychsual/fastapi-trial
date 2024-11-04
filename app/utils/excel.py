import pandas as pd

def import_excel(file_path: str):
    return pd.read_excel(file_path)

def export_excel(data: list, file_path: str):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)