
from unittest import TestCase

import pandas as pd
import pytest

from lakey_client.adls_downloader import ADLSDownloader
from lakey_client.client import LakeyClient


LAKEY_ACCESS_TOKEN = 'lakey.access.token'

LAKEY_ADLS_ACCOUNTNAME = 'lakey.adls.accountname'

LAKEY_ADLS_FILESYSTEM = 'lakey.adls.filesystem'


class LakeyClientTestCase(TestCase):

    @pytest.fixture(autouse=True)
    def initifixtures(self, mocker):
        self.mocker = mocker

    def test_download(self):

        download = self.mocker.patch.object(ADLSDownloader, 'download')
        download.return_value = '... replace with correct parquet ...'

        df = LakeyClient().download(14)

        assert df == []
