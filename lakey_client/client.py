
from io import BytesIO
import os

import requests
import pandas as pd


class LakeyClient:

    def __init__(self, base_uri, auth_token):
        self.base_uri = base_uri
        self.auth_token = auth_token

    def estimate_download(self, name, spec):

        response = requests.post(
            os.path.join(
                self.base_uri,
                'downloader/requests/estimate/'),
            headers={
                'Authorization': f'Bearer {self.auth_token}'  # noqa
            },
            json={
                'spec': spec,
                'catalogue_item_name': name
            })

        # TODO: make it to MB, KB etc. and wrap into HTML
        return response.json()['estimated_size']

    def download(self, name, spec):

        response = requests.post(
            os.path.join(
                self.base_uri,
                'downloader/requests/'),
             headers={
                'Authorization': f'Bearer {self.auth_token}'  # noqa
            },
            json={
                'spec': spec,
                'catalogue_item_name': name
            })

        chunk_dfs = []
        for chunk in response.json()['chunks']:
            chunk_df = pd.read_parquet(chunk['data_path'], engine='pyarrow')

            # TODO: here we should build a filter for those DataFrames in
            # order to remove all rows that are not inline with the `spec`.
            chunk_dfs.append(chunk_df)

        return pd.concat(chunk_dfs)

    # def discover(self):
    #     from IPython.display import IFrame

    #     return IFrame('http://localhost:8000', width=1000, height=650)
