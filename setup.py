from pathlib import Path
from setuptools import find_packages, setup

about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / 'requirements'
PACKAGE_DIR = ROOT_DIR / 'lending'
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


def list_reqs(fname="requirements.txt"):
    with open(REQUIREMENTS_DIR / fname) as fd:
        return fd.read().splitlines()


setup(
    version=about["__version__"],
    packages=find_packages(exclude=("tests",)),
    package_data={"lending": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)