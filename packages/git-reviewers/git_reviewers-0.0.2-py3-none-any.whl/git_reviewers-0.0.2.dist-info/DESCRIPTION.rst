git-reviewers
=============

|Codeship Status for albertyw/git-reviewers| |Dependency Status| |Code
Climate| |Test Coverage|

Tool to suggest code reviewers for your code depending on your diff

Development
-----------

.. code:: bash

    pip install -r requirements-test.txt
    coverage run setup.py test
    coverage report
    flake8

Publishing
----------

.. code:: bash

    sudo apt-get install pandoc
    pip install twine pypandoc
    python setup.py sdist bdist_wheel
    twine upload dist/*

.. |Codeship Status for albertyw/git-reviewers| image:: https://app.codeship.com/projects/17913cd0-3524-0135-2853-7e1f21584d06/status?branch=master
   :target: https://app.codeship.com/projects/227040
.. |Dependency Status| image:: https://gemnasium.com/badges/github.com/albertyw/git-reviewers.svg
   :target: https://gemnasium.com/github.com/albertyw/git-reviewers
.. |Code Climate| image:: https://codeclimate.com/github/albertyw/git-reviewers/badges/gpa.svg
   :target: https://codeclimate.com/github/albertyw/git-reviewers
.. |Test Coverage| image:: https://codeclimate.com/github/albertyw/git-reviewers/badges/coverage.svg
   :target: https://codeclimate.com/github/albertyw/git-reviewers/coverage


