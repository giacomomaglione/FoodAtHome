# FoodAtHome
Food@Home is a Progressive Web Application that manages the services of a food delivery.
The project was realized for the Web Technologies exam at the University of Naples Parthenope.

## Components
The web app was implemented using the following technologies: 
- **Client** side: HTML, CSS, JavaScript
- **Server** side: Python, Flask, MongoDB

## Create virtual environment
```
python3 -m venv venv 
. venv/bin/activate
```

## Plugins to install
After downloading the project from GitHub, it is necessary to open the terminal and install all the plugin listed in *[Requirements](requirements.txt)*, using the following command:
```
pip install -r requirements.txt
```

## Execute
To execute the **Food@Home** PWA, it is necessary to run the following command in the terminal:
```
(venv)$ pip install Flask
export FLASK_APP=main.py
flask run -h 0.0.0.0 -p 5000
```

```
python main.py
```
