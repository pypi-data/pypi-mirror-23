# -*- coding: utf-8 -*-


import os
import sys
from subprocess import Popen, PIPE
from setuptools import setup

import order


thisdir = os.path.dirname(os.path.abspath(__file__))

readme = os.path.join(thisdir, "README.md")
if os.path.isfile(readme) and "sdist" in sys.argv:
    cmd = "pandoc --from=markdown --to=rst " + readme
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception("pandoc conversion failed: " + err)
    long_description = out
else:
    long_description = ""

keywords = [
    "submission", "grid", "wlcg"
]

classifiers = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Information Technology",
    "Topic :: System :: Monitoring"
]

install_requires = []
with open(os.path.join(thisdir, "requirements.txt"), "r") as f:
    install_requires.extend(line.strip() for line in f.readlines() if line.strip())

setup(
    name             = order.__name__,
    version          = order.__version__,
    author           = order.__author__,
    author_email     = order.__email__,
    description      = order.__doc__.strip(),
    license          = order.__license__,
    url              = order.__contact__,
    keywords         = keywords,
    classifiers      = classifiers,
    long_description = long_description,
    install_requires = install_requires,
    zip_safe         = False,
    packages         = ["order"],
    package_data     = {"": ["LICENSE", "requirements.txt", "README.md"]}
)
