# Restaurant Management

Company needs internal service for its’ employees which helps them to make a decision
on lunch place.

Clone the repository using git clone command.
```bash
  git clone {repository}
```
## Setup using Docker
- Install docker from [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/) and [https://docs.docker.com/engine/install/linux-postinstall/](https://docs.docker.com/engine/install/linux-postinstall/).Below are the commands for Ubuntu 20.04.4 LTS.
```bash
  sudo apt install docker.io
  sudo snap install docker
```
- Check the docker version
```bash
  docker --version
```
- Navigate to the project folder (put your project path)
```bash
  cd /home/projects/{project_name}
```
- Build project using docker
```bash
  docker-compose build
```
- Run project using docker
```bash
  docker-compose up
```
## Setup Using Python

### Database

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

### Installation

Installation requires Python 3.8 or above

* Create the virtual environment
```bash
  python3 -m venv {env_name}
```
* Activate the environment
```bash
  source {env_name}/bin/activate
```
* Navigate to project folder (put your project path)
```bash
  cd /home/projects/{project_name}
```
* Install all dependencies from requirements.txt
```bash
  pip install -r requirements.txt
```
* Create the tables in database
```bash
  python3 manage.py migrate
```
* Run the server
```bash
  python3 manage.py runserver
```
## Features

- Authentication
- Creation, Deletion and List of restaurant
- Addition and List of Items
- Addition, Listing, Updation and deletion of menu for restaurant
- Creation and List of employee
- Getting current day menu
- Voting for restaurant menu (Old version api accepted one menu, New one accepts top three menus with respective points (1 to 3))
- Getting results for current day

## Enhancement

- Create analysis report based on the data
- Rating restaurant menu on scale of 1 to 10