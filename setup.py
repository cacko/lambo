from pathlib import Path
import semver
from setuptools.dist import Distribution as _Distribution
from setuptools import find_packages, setup

import sys

__name__ = "lambo"


def version():
    if len(sys.argv) > 1 and sys.argv[1] >= "bdist_wheel":
        init = Path(__file__).parent / "src" / __name__ / "version.py"
        _, v = init.read_text().split("=")
        cv = semver.VersionInfo.parse(v.strip().strip('"'))
        nv = f"{cv.bump_patch()}"
        init.write_text(f'__version__ = "{nv}"')
        return nv
    from lambo.version import __version__

    return __version__


class Distribution(_Distribution):
    def is_pure(self):
        return True

setup(
    name=__name__,
    version=version(),
    author="cacko",
    author_email="cacko@cacko.net",
    distclass=Distribution,
    url=f"http://pypi.cacko.net/simple/{__name__}/",
    description="whatever",
    install_requires=[
        "typer",
        "corelog",
        "python-hue-v2",
        "pydantic",
        "pydantic-settings"
    ],
    setup_requires=["wheel", "semver"],
    python_requires=">=3.11",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points="""
        [console_scripts]
        lambo=lambo.cli:start
    """,
)
