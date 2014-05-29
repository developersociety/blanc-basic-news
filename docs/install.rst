============
Installation
============

Requirements
============

Before installing blanc-basic-news, you'll need a copy of Django__ 1.7,
and blanc-basic-assets__ installed.

.. __: http://www.djangoproject.com/
.. __: https://github.com/blancltd/blanc-basic-assets


Installing blanc-basic-news
===========================

The fastest way of installing is to use pip__.

.. __: http://www.pip-installer.org/

Simply type::

    pip install blanc-basic-news

Manual installation
-------------------

Alternative you manually install by downloading the latest version from the
`blanc-basic-news page on the Python Package Index`__.

.. __: http://pypi.python.org/pypi/blanc-basic-news/

Download the package, unpack it and run the ``setup.py`` installation
script::

    python setup.py install


Configuring your project
========================

Edit your Django project's settings module, ensure that the required
dependencies are installed and configured, then add ``blanc_basic_news`` to
``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'blanc_basic_assets',
        ...
        'blanc_basic_news',
    )

Also in the settings file you should edit the title for RSS feeds::

    NEWS_TITLE = "My Site"

Once this is done, run ``python manage.py migrate`` to update your database.

Edit your Django project's URL config file, and add the URL pattern for news::

    urlpatterns = patterns('',
        ...

        # News
        url(r'^news/', include('blanc_basic_news.urls', namespace='blanc_basic_news')),
    )

Then your project will be ready to use the news package.
