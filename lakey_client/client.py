
from io import BytesIO

import pandas as pd

from .adls_downloader import ADLSDownloader


class LakeyClient:

    def download_to_df(self, path):

        global LAKEY_ACCESS_TOKEN
        global LAKEY_ADLS_ACCOUNTNAME
        global LAKEY_ADLS_FILESYSTEM

        downloader = ADLSDownloader(
            account_name=LAKEY_ADLS_ACCOUNTNAME,
            filesystem=LAKEY_ADLS_FILESYSTEM,
            access_token=LAKEY_ACCESS_TOKEN)

        content = downloader.download(path)

        return pd.read_parquet(
            BytesIO(content),
            engine='fastparquet')
