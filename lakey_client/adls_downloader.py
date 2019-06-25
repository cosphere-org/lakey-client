
import requests
from tqdm import tqdm


class ADLSDownloader:

    def download(self, index):

        resource_uri = (
            f'https://lakey.s3.eu-central-1.amazonaws.com/'  # noqa
            f'iot-workshop/{index}.parquet')
        response = requests.head(resource_uri)
        bytes_count = int(response.headers['content-length'])

        content = b''
        response = requests.get(resource_uri, stream=True)
        with tqdm(total=int(bytes_count / 1024)) as t:
            for chunk in response.iter_content(chunk_size=1024):
                content += chunk
                t.update()

        return content
