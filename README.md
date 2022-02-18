# VendorsRestApi
A little project to design an application who registrate a vendor and products catalogues in django.

## Description:

For this example I chose to implement the solution using django with the django-rest-framework. It's all very clean, no setups and infinite configs, with few lines and less than 6 hours of hard work, voialá, we have an api that is scalable, easy to maintain, with understandable code and very easy to test too. Well, this comes with some drawbacks, it's true, and maybe the performance makes things a little less attractive, but it's still functional and I only had to spend 1/3 of the time it would take to build a new REST API from scratch.

This project was developed in a Raspaberry Pi 4 with 4 GB RAM and Running Raspbian GNU/Linux 10 (buster)(my learning programming machine); My IDE setup is quite simple just the basics (VS Code, with some python intellisense and black for prettier code format ).

### Dependencies:

|Package             | Version  |
|--------------------| ---------|
| Django             | 3.2.7    |
| django-filter      |  2.4.0   |
| django-grappelli   |  2.15.1  |
| django-localflavor |  3.1     |
| django-model-utils |  4.1.1   |
| djangorestframework|  3.12.4  |
| factory-boy        |  3.2.0   |
| psycopg2           |  2.9.1   |
| pytest             |  6.2.5   |
| pytest-cov         |  2.12.1  |
| pytest-django      |  4.4.0   |

_See the full requirements list on requirements.txt_

## How to Run (Installing, Setup, Test):

- Download this repository and create an virtual enviroment using any virtual enviroment management system that you prefer

- Install all dependecies with 'pipenv install' on your local repository folder like the example:

```bash
myuser@mydevice:~/my/local/folder $ pipenv install
```

- then if you don't receive any error just run server with the command bellow

```bash
(my-env) myuser@mydevice:~/my/local/folder $ ./manage.py runserver
```
_Make sure that you got the correct URL(probabily: 127.0.0.1:8000) from comand results and if you dont receive any error..._

# Congrats Now you have a restful api running !!

##

### For rest api front-end with the awesome django-rest-framework
- you should get access at http://127.0.0.1:8000 if there is no other server running on your device, but it is better to check the results of the 'runserver' command and make sure you have the correct url

### For admin-django front-end with the pretty grappelli theme
- http://127.0.0.1:8000/admin (once more, make sure that you have the correct url man)

### Postman (Collection and Workspace)

- For test API maybe you can use  [this](https://www.getpostman.com/collections/) quite simple collection.

- Or test directly from [this](https://app.getpostman.com/) workspace.

- But if you like do things on your way the [API Postman Collection](postman_collection.json) also is available on root folder of this project

## API documentation
You can found more detailed information about the api [here](https://documenter.getpostman.com/)

## Online Example
You can see how it's works on 