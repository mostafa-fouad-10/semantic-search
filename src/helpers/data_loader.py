import pandas as pd

from src.helpers.config import get_settings


class DocumentLoader:

    def __init__(self):
        settings = get_settings()
        self.data_path = settings.data_path

    def load(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)