import os
from setuptools import setup, find_packages

# Read the long description from the README.
thisdir = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(thisdir, "README"))
kwds = {"long_description": f.read()}
f.close()

setup(name="PyDyn",
      version="0.1",
      description="Dynamic analysis of electric power systems",
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      url="http://pypi.python.org/pypi/PyDyn",
      license="Apache",
      packages=find_packages(),
      zip_safe=True,
      **kwds)
