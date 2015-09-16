PyBlox  0.1
================

A modern Python framework utilizing Python, SQLAlchemy, Angularjs, JQuery, Bootstrap, LESS, and other stuff we use regularly.

PyBlox is in the python package index and can be installed to your environment easily without needing to clone from this repo using PIP or easy_install. If you wish to contribute, fork or clone. Installation has been verified in Linux, OSX, and even Windows.

From your favorite OS, grab a shell and issue the following commands:

Use easy_install or pip (from a rhel `yum install python-setuptools`)

easy_install pyblox

paster create -t PyBlox MySuperCoolApp

cd MySuperCoolApp

python setup.py develop

paster setup-app ./development.ini

paster serve --reload ./development.ini

That's it! Now browse to http://127.0.0.1:8080/ 


If you want PostgreSQL support, just add psycopg2 to your module dependencies and use the usual connection string syntax in the development.ini. Stay tuned for the web site. We have some configuration options for various javascript toolkit support options coming. pg_config might fail, so you will have to get it in your $PATH before insalling psycopg2 e.g. (find /var/lib -name pg_config -exec ln -s {} /usr/bin \;) or your bashrc or shell profile evironment etc.


