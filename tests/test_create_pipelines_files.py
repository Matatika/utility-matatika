"""Unittest module for create_pipelines_files"""

import unittest
import shutil

from pathlib import Path
from click.testing import CliRunner

from matatika_utils.create_pipelines_files import create_pipelines_files

SCHEDULE_COMMAND_OUTPUT = {
    "schedules": {
        "job": [
            {
                "name": "123",
                "interval": "@daily",
                "cron_interval": "0 0 * * *",
                "env": {},
                "job": {
                    "name": "testjob",
                    "tasks": ["tap-spotify target-postgres dbt:run"],
                },
            },
            {
                "name": "newschedule",
                "interval": "0 0 0 * * 0",
                "cron_interval": "0 0 0 * * 0",
                "env": {},
                "job": {
                    "name": "testjob5",
                    "tasks": [
                        "tap-spotify target-postgres dbt:run dbt:"
                        + "snapshot tap-spotify target-postgres dbt:run"
                    ],
                },
            },
        ],
        "elt": [
            {
                "name": "testtwo",
                "extractor": "tap-spotify",
                "loader": "target-postgres",
                "transform": "skip",
                "interval": "@daily",
                "start_date": "2022-07-19",
                "env": {},
                "cron_interval": "0 0 * * *",
                "last_successful_run_ended_at": None,
                "elt_args": [
                    "tap-spotify",
                    "target-postgres",
                    "--transform=skip",
                    "--state-id=testtwo",
                ],
            }
        ],
    }
}


class TestCreatePipelinesFiles(unittest.TestCase):
    """Unittest class for matatika-utils create_pipelines_files"""

    def setUp(self):
        """matatika-utils create_pipelines_files test setup"""
        self.package_dir = str(Path(__file__).parent.parent.absolute())
        self.test_files_path = self.package_dir + "/pipelines"

        self.runner = CliRunner()

    def tearDown(self) -> None:
        """matatika-utils create_pipelines_files test tear down"""
        shutil.rmtree(Path(self.test_files_path))

    def test_create_pipelines_files(self):
        """Test create_pipelines_files function"""
        create_pipelines_files(self.package_dir, SCHEDULE_COMMAND_OUTPUT)
        pipeline_file_path = Path(self.test_files_path).joinpath("123.yml")
        self.assertTrue(pipeline_file_path.is_file())
        pipeline_file_path = Path(self.test_files_path).joinpath("newschedule.yml")
        self.assertTrue(pipeline_file_path.is_file())
