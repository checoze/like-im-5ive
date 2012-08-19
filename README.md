like-lm-5ive
============

[![Build Status](https://secure.travis-ci.org/checoze/like-im-5ive.png?branch=develop)](http://travis-ci.org/checoze/like-im-5ive)

About
-----

Like I'm 5ive is an application that provides simple, laymen's explanations for everything. Search for and provide short explanations about
people, places, concepts, youtube videos, news articles, or any URL or thing. 


Core Features
--------

Create Entries

Create Explanations for those entires

Vote on Explanations

Comments (coming soon)

Registration

Extra Features
--------

Responsive Styles-- completely mobile friendly!

Tests-- Selenium tested, Unit Coming soon (hey, it WAS a dash)

Help Docs

APIs-- GET for now, POST soon

TravisCI Integration



To get up and running::

    pip install conf/requirements.txt

If you want to us Hadrian, map fab to conf/fab.py or pass in conf/fab.py as your fabfile.  Then::

    fab run_local

Otherwise just run the usual::

    python manage.py runserver --settings=settings.local