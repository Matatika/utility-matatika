"""Unittest module for matatika-utils pipelines"""

import unittest
from pathlib import Path
from click.testing import CliRunner


class TestPipelines(unittest.TestCase):
    """Unittest class for matatika-utils pipelines"""

    def setUp(self):
        """matatika-utils pipelines test setup"""
        self.package_dir = Path(__file__).parent.parent.absolute()
        self.notebook_path = self.package_dir.joinpath("test_files/test_notebook.ipynb")
        self.notebook_dir_path = self.package_dir.joinpath("test_files/notebook_dir/")
        self.test_files_path = self.package_dir.joinpath("test_files/")
        self.text_file_path = self.test_files_path.joinpath("text_file.txt")

        self.runner = CliRunner()
