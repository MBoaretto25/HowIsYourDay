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

import numpy as np
import cv2



app = Flask(__name__)
g_imgCounter = 0

@app.route('/howisurday')
def todo_twitt():
    now = datetime.datetime.now()
    return render_template('HowIsUrDay.html', items=now)

@app.route('/howisurday_user_snap', methods = ['POST'])
def get_user_snap():
    global g_imgCounter
    file = request.files['webcam']
    image = cv2.imdecode(np.fromstring(file.stream.read(),np.uint8), cv2.IMREAD_UNCHANGED)
    cv2.imwrite("{}.jpg".format(g_imgCounter),image)
    g_imgCounter+=1

    return ""

if __name__ == "__main__":
    app.debug = True
    app.run(host=socket.gethostbyname(socket.gethostname()), threaded=True, ssl_context='adhoc')
