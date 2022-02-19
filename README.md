# VendorsRestApi
A little project to design an API who consultin organizations from Github API, calcule their score based on public repositories and public members and registrate this informations on database.

## Description:

This project was developed in a Philco Notebook Model: with 3 GB RAM and Running Windows 7 32bit's; My IDE setup is quite simple just the basics (VS Code, with some python intellisense and black for prettier code format ).

### Dependencies:

|Package             | Version  |
|--------------------| ---------|
| django             |  3.1.1   |
| django-filter      |  2.4.0   |
| djangorestframework|  3.12.4  |
| django-filter      |  *       |
| requests           |  2.25.1  |
| pipenv             |  *       |




_See the full requirements list on Pipfile_

## How to Run (Installing, Setup, Test):

- Download this repository and create an virtual enviroment using pipenv

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
- you should get access at http://127.0.0.1:8000/api if there is no other server running on your device, but it is better to check the results of the 'runserver' command and make sure you have the correct url


### Postman (Collection and Workspace)

- For test API maybe you can use  [this](https://www.getpostman.com/collections/) quite simple collection.

- Or test directly from [this](https://app.getpostman.com/) workspace.

- But if you like do things on your way the [API Postman Collection](postman_collection.json) also is available on root folder of this project

## API documentation
You can found more detailed information about the api [here](https://documenter.getpostman.com/)

## Online Example
You can see how it's works on 