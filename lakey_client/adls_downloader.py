
import requests


class ADLSDownloader:

    def __init__(self, account_name, filesystem, access_token):
        self.account_name = account_name
        self.filesystem = filesystem
        self.access_token = access_token

    def download(self, path):
        uri = (
            f'https://{self.account_name}.dfs.core.windows.net/'
            f'{self.filesystem}/{path}'),

        response = requests.head(
            uri,
            headers={
                'x-ms-version': '2018-11-09',
                'Authorization': 'Bearer {self.access_token}',
            })

        # FIXME: what is the destination???
        # what about showing some progress??
        response = requests.get(
            uri,
            stream=True,
            headers={
                'x-ms-version': '2018-11-09',
                'Authorization': 'Bearer {access_token}',
                'Range': 'bytes=0-8',
            })

        # r = requests.get('https://httpbin.org/stream/20', stream=True)

        # for line in r.iter_lines():

        #     # filter out keep-alive new lines
        #     if line:
        #         decoded_line = line.decode('utf-8')
        #         print(json.loads(decoded_line))
        #
