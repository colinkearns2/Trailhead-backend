# TrailheadBackend

This repo will hold our Django database

## Architecture

Our group is interested in learning more about dev with Django, so we watched this tutorial to understand its architecture: [https://www.youtube.com/watch?v=nGIg40xs9e4&t=103s]([url](https://www.youtube.com/watch?v=nGIg40xs9e4&t=103s))

## Setup

We are using a virtual environment, to get that set up, we used these commands: 
` pip install virtualenv `
`python -m venv myenv`
Then to activate: 
`source myenv/bin/activate `
To install Django: 
`pip install django`
In order to initialize a Django project within this repo, run this command: 
` django-admin startproject trip_planner_backend`
Next, to set up a virtual environment for Python related dependencies and the djangorestframework, run this command: 
`pip install django djangorestframework`
Then to run the server use this command: 
`python manage.py runserver`

## Deployment

TODO: We will make a dependencies.txt file in which we will maintain all the dependecies this project requires so that we can run this script: 
`pip install -r dependencies.txt` instead of running all of those pesky individual commands. 

To get the server running: `python manage.py runserver`

To be able to test the database: `python manage.py makemigrations                                            
python manage.py migrate`

## Authors

Ari Rojas
Colin Kearns

## Acknowledgments


