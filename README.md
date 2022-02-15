# FoodAtHome
Food@Home is a Progressive Web Application that manages the services of a food delivery.
The project was realized for the Web Technologies exam at the University of Naples Parthenope.

## Components
The web app was implemented using the following technologies: 
- **Client** side: HTML, CSS, JavaScript
- **Server** side: Python, Flask, MongoDB

## Create a virtual environment
```
python3 -m venv venv 
. venv/bin/activate
```

## Packages to install
Inside the virtual environment folder, it is necessary to install Flask and the packages listed in *[Requirements](requirements.txt)*, using the following command:
```
pip install Flask
pip install -r requirements.txt
```

## Execute
To execute the **Food@Home** PWA, it is necessary to run the following commands in the terminal:
```
export FLASK_APP=main.py
flask run -h 0.0.0.0 -p 5000
python main.py
```
