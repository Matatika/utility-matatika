from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="matatika-utils",
    version="0.1.0",
    description="A Meltano utility plugin for creating Matatika artifacts to run the Matatika orchestrator.",
    author="DanielPDWalker",
    url="https://www.matatika.com/",
    entry_points="""
        [console_scripts]
        matatika-utils=matatika_utils.cli.commands.root:mutils
    """,
    license="MIT",
    install_requires=required,
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
