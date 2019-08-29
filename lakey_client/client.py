
from io import BytesIO
import os

import requests
import pandas as pd
import operator


operators_to_def = {
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    '=': operator.eq,
}


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

        size = int(response.json()['estimated_size']) / 1000000
        return (f'<div style="display: block; width: 100%; height: 100px; '
                f'background-color: blue; text-align: center;"> '
                f'<b style="color: white;">{size} MB</b> '
                f'</div> ')

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

            for f in spec['filters']:
                chunk_df = chunk_df[
                    operators_to_def[f['operator']](chunk_df[f['name']], f['value'])
                ]
            chunk_dfs.append(chunk_df)

        return pd.concat(chunk_dfs)[spec['columns']]

    # def discover(self):
    #     from IPython.display import IFrame

    #     return IFrame('http://localhost:8000', width=1000, height=650)
