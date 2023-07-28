import sys
import os
from setuptools import setup, find_packages

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

version = "0.0.1"

setup(name="PyBlox",
      version=version,
      description="A Python MVC web framework.",
      long_description="""A Python web framework""",
      classifiers=["Environment :: Web Environment"],
      keywords="python sqlalchemy angularjs framework responsive bootstrap admin",
      author="Noel Morgan",
      author_email="noel@vwci.com",
      url="http://www.pyblox.org",
      license="MIT",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "PasteScript==3.3.0",
          "PasteDeploy==3.0.1",
      ],
      dependency_links=[
          "git+git@github.com:regularex/paste.git#egg=paste"
      ]      
      setup_requires=["PasteScript==3.3.0],
      entry_points="""
      [paste.paster_create_template]
      PyBlox = pyblox.tmplt:PyBloxTemplate
      """
      )

