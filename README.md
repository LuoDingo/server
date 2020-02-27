# LuoDingo

LuoDingo is an language learning chat application


## Project Requirements
* python3
* sqlite 3.28.0

## Setup
 1. git clone this repo
 1. cd into the app
 1. init python virtual environment (i use virtualenv)
 1. activate virtual environment
 1. run `pip install -r requirements.txt`
 1. setup database
    * open the python interpreter with command `python`
    * `from web import db, create_app`
    * `db.create_all(app=create_app())`
 1. run `python chat.py`
 1. access app from `localhost:5000` in web browser