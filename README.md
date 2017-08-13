# Item Catalog
This project is implementing Python Flask framework to build a web app for performing CRUD operations on items of a catalog as required for Project 4 of FSND program

## Requirements

- Download Vagrant and VirtualBox and install them
- Download [Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm/raw/master/vagrant/Vagrantfile)
- Download Git bash for Windows (yes only if Windows) and install
- Clone or Download this repo then extract from zip
- JSON file of your Google developers credentials, here's how to get one:
1. Go to https://console.developers.google.com/project and login with Google.
2. Create a new project
3. Name the project whatever you like
4. Click `Create credentials` and choose `OAuth Client ID` then go to `Configure consent screen` and enter product name.
5. After that select `Web App` option.
6. Type app name and enter http://localhost:8080 in both Restrictions input fields and in `Authorized redirect URIs` field, enter http://localhost:8080/oauth/google.
7. In credentials tab, download JSON of your Cliend ID
9. Save it into the root director of this project.
10. Rename the JSON file "client_secrets.json"
11. In main.html replace the value of `data-clientid` with your Client ID from the web app.
## Setting up VM
- Move the 'Vagrantfile' to downloaded directory
- Open 'Terminal' or 'Git bash for Windows' after going to downlaoded directory
- run `vagrant up` (This can take time if running for the first time)
- run `vagrant ssh`
## Creating Database
  Follwing commands create a database model for Catalog anf fill it up:
```sh
$ python database_setup.py
$ python insert_games.py
```
## Usage
Run the Item Catalog server by typing this:
```sh
$ python project.py
```
## Attribution
Database setup structure from https://github.com/udacity/ud330/tree/master/Lesson4/step2
