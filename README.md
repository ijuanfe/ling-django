# Learning Django: the purpose of this repository is to learn the basics of Django (:

The following steps need to be taken to deploy this app:

  - apt install python3-venv
  - python3 -m venv env/
  - source env/bin/activate
    - Test env with command: which python or which pip
  - pip install -r requirements.txt
    - Test Django: python -m django --version or python -> import django -> print(django.get_version())
  - Run Django server: python mysite/manage.py runserver
