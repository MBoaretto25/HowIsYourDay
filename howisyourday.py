import random 
import os
import json
import datetime
import time
import sys
import glob
import subprocess
from flask import Flask, redirect, url_for, request, render_template
from flask import Blueprint, flash, g, redirect, render_template, request, url_for


app = Flask(__name__)

@app.route('/testeok')
def testeok():
    return "Deu boa irmão!!!!"

@app.route('/howisurday')
def todo_twitt():
    now = datetime.datetime.now()
    return render_template('HowIsUrDay.html', items=now)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=port)
