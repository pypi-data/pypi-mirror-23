########
Sebureem
########

.. image:: https://framagit.org/erwhann-rouge/sebureem/badges/master/build.svg
   :target: https://framagit.org/erwhann-rouge/sebureem/commits/master)

.. image:: https://framagit.org/erwhann-rouge/sebureem/badges/master/coverage.svg
   :target: https://framagit.org/erwhann-rouge/sebureem/commits/master)

.. image:: https://img.shields.io/pypi/v/sebureem.svg 
   :target: https://pypi.python.org/pypi/sebureem/

.. image:: https://img.shields.io/pypi/l/sebureem.svg 

Sebureem is a small comment server written in Python 3 with the Flask
microframework and the Peewee ORM.
Comments are storred using the SQLite database.

Sebureem aim to be:

* Easy to integrate
* Easy to deploy and configure

Sebureem is the Kotava word for "comments" or "group of comments".

**Important : Sebureem is still in very early stage. It might not be secure and
a lot of rough edges are to be expected.**

Installation
============

First run::

    pip install sebureem

Create database::

    sebureem database --init

Then run your sebureem instance with::

    sebureem serve

… or you can specify host and port::

    sebureem serve 0.0.0.0 8000

Usage
=====

Just add an iframe containing the following code in your page::

    <iframe src="http://<server_url:port>/comments/<topic>" >
        <p>Your browser doesn't support iframes. Comments can't be loaded.</p>
    </iframe>

where server_url and port are the address of your instance and topic is the name
of the discussion thread you want to add to your webpage.

If the thread doesn't exist in the database it will be created with the first
comment.

Roadmap
=======

Planned features:

* Angular/Ember/Aurelia web_app
* Avatar support (Python Cat Avatar Generator ?)
* Instance federation
* Admin page

Contributions
=============

Contributions are warmly welcome. See `CONTRIBUTING.rst`__.

Sebureem development occurs 
`here <https://framagit.org/Erwhann-Rouge/sebureem>`_ on the Framasoft's Gitlab
instance.

Others repositories (I'm thinking of Github here) are mainly for replication.

License
=======

Sebureem is licensed both under the BSD License and the Cecill-B License.



