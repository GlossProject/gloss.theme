from setuptools import setup, find_packages
import os

version = '0.8.2'

setup(name='gloss.theme',
      version=version,
      description="gloss.theme",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='theme,gloss',
      author='David Bain',
      author_email='david@alteroo.com',
      url='https://github.com/glossproject/gloss.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gloss'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
