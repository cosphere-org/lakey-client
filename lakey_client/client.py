
from io import BytesIO

import pandas as pd

from .adls_downloader import ADLSDownloader


class LakeyClient:

    def download(self, spec=None, id=None):

        index = id.split('-')[1]
        content = ADLSDownloader().download(index)

        return pd.read_parquet(
            BytesIO(content),
            engine='fastparquet')

    def discover(self):
        from IPython.display import IFrame

        return IFrame('http://localhost:8000', width=1000, height=650)
