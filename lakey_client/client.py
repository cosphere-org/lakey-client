
from io import BytesIO

import pandas as pd

from .adls_downloader import ADLSDownloader


class LakeyClient:

    def download_to_df(self, index):

        content = ADLSDownloader().download(index)

        return pd.read_parquet(
            BytesIO(content),
            engine='fastparquet')
