from flask import  Flask, jsonify, request, session, url_for, redirect
from . import cliente, rider, negozio
from flask_login import UserMixin
import pymongo


