# event_management_system
Event management system - Django
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/nobitadore/event_management_system.git
$ cd project
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.7 -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:

Create database name : "event_management_system" and then we start to migrate

```sh
(env)$ cd event_management_system
(env)$ python3.7 manage.py migrate
(env)$ python3.7 manage.py makemigrations admin_portal
(env)$ python3.7 manage.py createsuperuser
```
Enter your desired username and press enter.

Username: admin
You will then be prompted for your desired email address:

Email address: admin@example.com
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.

```sh
(env)$ python3.7 manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
