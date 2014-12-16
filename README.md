PyBlox  0.1
================

A full-featured MVC python web framework utilizing Python, SQLAlchemy, JQuery, Bootstrap, LESS, and other great software.

PyBlox is part of the python package index and can be installed to your environment easily without needing to clone from this repo using PIP or easy_install. If you wish to contribute, fork or clone. Installation has been verified in Linux, OSX, and even Windows.

From your favorite OS, grab a shell and issue the following commands:

easy_install pyblox

paster create -t PyBlox MySuperCoolApp

cd MySuperCoolApp

python setup.py develop

paster serve --reload ./development.ini

If you want PostgreSQL support, then add psycopg2 to your module dependencies and use the usual connection string syntax in the development.ini. 

That's it! Now browse to http://127.0.0.1:8080/ 