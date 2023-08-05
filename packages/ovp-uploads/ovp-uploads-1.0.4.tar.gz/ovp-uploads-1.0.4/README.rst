==========
OVP Uploads
==========

.. image:: https://img.shields.io/codeship/468bb4d0-7850-0134-a43d-7aa8687239c4/master.svg?style=flat-square
.. image:: https://img.shields.io/codecov/c/github/OpenVolunteeringPlatform/django-ovp-uploads.svg?style=flat-square
  :target: https://codecov.io/gh/OpenVolunteeringPlatform/django-ovp-uploads/
.. image:: https://img.shields.io/pypi/v/ovp-uploads.svg?style=flat-square
  :target: https://pypi.python.org/pypi/ovp-uploads/

This module implements core upload functionality.

Getting Started
---------------
Requirements
""""""""""""""
This module uses pillow. Don't forget installing your `libjpeg` and your `zlib` through your distribution package manager.

Installing
""""""""""""""
1. Install django-ovp-uploads::

    pip install ovp-uploads

2. Add it to `INSTALLED_APPS` on `settings.py`

3. Include urls to your url_patterns

4. Setup your file storage backend on settings::

    DJANGO_DEFAULT_STORAGE = '...'


Forking
""""""""""""""
If you have your own OVP installation and want to fork this module
to implement custom features while still merging changes from upstream,
take a look at `django-git-submodules <https://github.com/leonardoarroyo/django-git-submodules>`_.

Testing
---------------
To test this module

::

  python ovp_uploads/tests/runtests.py

Contributing
---------------
Please read `CONTRIBUTING.md <https://github.com/OpenVolunteeringPlatform/django-ovp-users/blob/master/CONTRIBUTING.md>`_ for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
---------------
We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/OpenVolunteeringPlatform/django-ovp-/tags>`_. 

License
---------------
This project is licensed under the GNU GPLv3 License see the `LICENSE.md <https://github.com/OpenVolunteeringPlatform/django-ovp-users/blob/master/LICENSE.md>`_ file for details
