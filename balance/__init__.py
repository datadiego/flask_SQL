#Este archivo marca la carpeta balance
from flask import Flask

app = Flask(__name__) #name es balance por la carpeta
app.config.from_prefixed_env()

