# NaT Django

## Project setup

* [Python 3.9.2](https://www.python.org/downloads/release/python-392/).
* [pip](https://pip.pypa.io/en/stable/installing/)
* [Virtuelenv](https://pypi.org/project/virtualenv/)


### Clone repo
```
git clone https://github.com/JollyGoal/nat_dj.git
cd nat_dj
```

### Setting up virtuelenv
```
virtualenv venv
```

#### Windows
```
venv\Scripts\activate
```

#### Linux
```
source venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run server
```
python manage.py runserver
```

The server will run with super user (login: admin | password: admin)

### Unnecessary configuration
In some cases try to run following commands

```
python manage.py makemigrations
python manage.py migrate
```

