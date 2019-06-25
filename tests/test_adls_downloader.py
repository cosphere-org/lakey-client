
from unittest import TestCase

from lakey_client.adls_downloader import ADLSDownloader


class ADLSDownloaderTestCase(TestCase):

    def test_download(self):

        content = ADLSDownloader().download('0')
