from flask import Flask, redirect, url_for, request, render_template
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import random 
import os
import json
import datetime
import time
import sys
import glob
import subprocess
import socket


app = Flask(__name__)

@app.route('/testeok')
def testeok():
    return "Deu boa irmão!!!!"

@app.route('/howisurday')
def todo_twitt():
    now = datetime.datetime.now()
    return render_template('HowIsUrDay.html', items=now)

if __name__ == "__main__":
    app.run(host=socket.gethostbyname(socket.gethostname()), threaded=True, ssl_context='adhoc')
