
# Setup new django project in **Linux/Mac**

## install venv
```
sudo apt install python3.12-venv
```

## if any error
```
sudo apt-get update
```
## Create venv
```
python3 -m venv venv 
```
## activate virtual environment
```
source venv/bin/activate
```
## Now install django
```
sudo apt install python3-django
```
or
```
pip install django
```
## Now create a new django project
```
django-admin startproject MyProject1
```
## goto the "MyProject1" directory
```
cd MyProject1
```
## Run the project in localhost
```
python3 manage.py runserver
```
## ***sudo*** is for permission
