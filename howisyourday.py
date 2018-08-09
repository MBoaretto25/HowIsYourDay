from flask import Flask, redirect, request, render_template, url_for
import numpy as np
import datetime
import time
import socket
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static','images_from_peoples')

g_imgCounter = 0
faceNet = cv2.dnn.readNetFromCaffe("cnn-models/deploy.prototxt",
                                    "cnn-models/res10_300x300_ssd_iter_140000.caffemodel")

@app.route('/howisurday')
def todo_twitt():
    now = datetime.datetime.now()
    return render_template('HowIsUrDay.html', items=now)

@app.route('/detected_face/<file>')
def detected_face(file):
    fileName = os.path.join(app.config['UPLOAD_FOLDER'], file)
    print(fileName)
    return render_template("detected_face.html", user_image = fileName)


@app.route('/howisurday_user_snap', methods = ['POST'])
def get_user_snap():
    global g_imgCounter, faceNet
    file = request.files['webcam']
    t = time.time()
    image = cv2.imdecode(np.fromstring(file.stream.read(),np.uint8), cv2.IMREAD_UNCHANGED)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
    faceNet.setInput(blob)
    detections = faceNet.forward()
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]
    
        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
    
            # draw the bounding box of the face along with the associated
            # probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY),
                (0, 0, 255), 2)
            cv2.putText(image, text, (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    g_imgCounter+=1
    fileName = "static/images_from_peoples/{}.jpg".format(g_imgCounter)
    cv2.imwrite(fileName,image)
    print("process time:", time.time()-t)
    
    return redirect(url_for('detected_face',file=os.path.basename(fileName)))

if __name__ == "__main__":
    app.debug = True
    app.run(host=socket.gethostbyname(socket.gethostname()), threaded=True, ssl_context='adhoc')
