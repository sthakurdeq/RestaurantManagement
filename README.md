
# Restaurant Management

Company needs internal service for its’ employees which helps them to make a decision
on lunch place.

## Database

Database used for Restaurant Management is postgresql.
- Install the postgresql. Below are the commands for Ubuntu
```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
```
- Start the postgresql service
```bash
  sudo systemctl start postgresql.service
```

## Installation

Installation requires Python 3.8 or above

* Clone the repository using git clone command
```bash
  git clone git@github.com:sthakurdeq/restaurantManagement.git
```
* Create the virtual environment
```bash
  python3 -m venv {env_name}
```
* Activate the environment
```bash
  source {env_name}/bin/activate
```
* Go to the project folder (put your own path)
```bash
  cd /home/projects/{project_name}
```
* Install all dependencies from requirements.txt
```bash
  pip install -r requirements.txt
```
* Migrate the tables
```bash
  python3 manage.py migrate
```
* Run the server
```bash
  python3 manage.py runserver
```
## Features

- Authentication
- Creating restaurant
- Uploading menu for restaurant (Menu for each day)
- Creating employee
- Getting current day menu
- Voting for restaurant menu (Old version api accepted one menu, New one accepts top three menus with respective points (1 to 3))
- Getting results for current day

## Docker
## Enhancement

- Create analysis report based on the data