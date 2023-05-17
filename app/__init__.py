"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi80trhp8u7g2egong0-a",
        database="himanshi",
        user="root",
        password="2UwM3XzXVoiXQRXd6EEZz6ATgWJAneiJ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
