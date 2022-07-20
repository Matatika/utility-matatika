"""CLI 'pipelines' command"""
import json
import logging
import os
import subprocess

from pathlib import Path
from matatika_utils.create_pipelines_files import create_pipelines_files
from .root import mutils

logger = logging.getLogger(__name__)


@mutils.command(
    "pipelines",
    short_help="Generate Matatika pipeline.yml files from your Meltano project's schedules",
)
def pipelines():
    """Generate Matatika pipeline.yml files"""
    project_root = os.getenv("MELTANO_PROJECT_ROOT", os.getcwd())

    meltano_bin = ".meltano/run/bin"

    if not Path(project_root).joinpath(meltano_bin).exists():
        logger.warning(
            "A symlink to the 'meltano' executable could not be found at '%s'.",
            meltano_bin,
        )

    result = subprocess.run(
        [meltano_bin, "schedule", "list", "--format=json"],
        cwd=project_root,
        stdout=subprocess.PIPE,
        universal_newlines=True,
        check=True,
    )
    schedules = json.loads(result.stdout)

    create_pipelines_files(project_root, schedules)
