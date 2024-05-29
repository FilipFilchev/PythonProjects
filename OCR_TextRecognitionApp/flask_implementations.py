#TESSERACT
"""#brew install tesseract
#pip install flask opencv-python pytesseract numpy


from flask import Flask, render_template, request
import cv2
import numpy as np
import pytesseract

app = Flask(__name__)

# Configure path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

#pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No selected file')
    
    # Read image
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply OCR
    text = pytesseract.image_to_string(gray, lang='eng')
    
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)


# TESSERACT WONT INSTALL for some reason"""
#GOOGLE VISION

"""
#pip install google-cloud-vision

from flask import Flask, render_template, request
from google.cloud import vision
import io

app = Flask(__name__)

# Create a client for the Google Cloud Vision API
client = vision.ImageAnnotatorClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No selected file')
    
    # Read image
    content = file.read()
    
    # Use Google Cloud Vision API for text extraction
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    # Extract text
    extracted_text = ''
    for text in texts:
        extracted_text += text.description + '\n'
    
    return render_template('index.html', text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)


"""
"""
#TensorFlow Object Detection API
from flask import Flask, render_template, request
import numpy as np
import os
from imutils.contours import sort_contours
import numpy as np
import argparse
import imutils
import cv2
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("OCR_Resnet.h5")
print("model is loaded")

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        filename = file.filename
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
        test_image = tf.keras.preprocessing.image.load_img(file_path)
        src = cv2.imread(file_path)
        print(src)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 30, 150)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sort_contours(cnts, method="left-to-right")[0]
        chars = []
        for c in cnts:
            # compute the bounding box of the contour
            (x, y, w, h) = cv2.boundingRect(c)
            # filter out bounding boxes, ensuring they are neither too small
            # nor too large
            if (w >= 5 and w <= 150) and (h >= 15 and h <= 120):
                # extract the character and threshold it to make the character
                # appear as *white* (foreground) on a *black* background, then
                # grab the width and height of the thresholded image
                roi = gray[y:y + h, x:x + w]
                thresh = cv2.threshold(roi, 0, 255,
                                       cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
                (tH, tW) = thresh.shape
                # if the width is greater than the height, resize along the
                # width dimension
                if tW > tH:
                    thresh = imutils.resize(thresh, width=32)
                # otherwise, resize along the height
                else:
                    thresh = imutils.resize(thresh, height=32)
                # re-grab the image dimensions (now that its been resized)
                # and then determine how much we need to pad the width and
                # height such that our image will be 32x32
                (tH, tW) = thresh.shape
                dX = int(max(0, 32 - tW) / 2.0)
                dY = int(max(0, 32 - tH) / 2.0)
                # pad the image and force 32x32 dimensions
                padded = cv2.copyMakeBorder(thresh, top=dY, bottom=dY,
                                            left=dX, right=dX, borderType=cv2.BORDER_CONSTANT,
                                            value=(0, 0, 0))
                padded = cv2.resize(padded, (32, 32))
                # prepare the padded image for classification via our
                # handwriting OCR model
                padded = padded.astype("float32") / 255.0
                padded = np.expand_dims(padded, axis=-1)
                # update our list of characters that will be OCR'd
                chars.append((padded, (x, y, w, h)))
        boxes = [b[1] for b in chars]
        chars = np.array([c[0] for c in chars], dtype="float32")
        # OCR the characters using our handwriting recognition model
        preds = model.predict(chars)
        # define the list of label names
        labelNames = "0123456789"
        labelNames += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        labelNames = [l for l in labelNames]

        output = ""
        for (pred, (x, y, w, h)) in zip(preds, boxes):
            i = np.argmax(pred)
            prob = pred[i]
            label = labelNames[i]
            output += label

        print("output",output)

        return render_template('sec.html', pred_output=output, user_image=file_path)

if __name__ == "__main__":
    app.run(threaded=False)"""
    
    
# import cv2
# #or with google-cloud-vision

# import easyocr
# import matplotlib.pyplot as plt
# import numpy as np



# # read image
# image_path = 'image.png'

# img = cv2.imread(image_path)

# # instance text detector
# reader = easyocr.Reader(['en'], gpu=False)

# # detect text on image
# text_ = reader.readtext(img)

# threshold = 0.25
# # draw bbox and text
# for t_, t in enumerate(text_):
#     print(t)

#     bbox, text, score = t

#     if score > threshold:
#         cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
#         cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()


#source venv/bin/activate

"""data:
Matplotlib is building the font cache; this may take a moment.
Using CPU. Note: This module is much faster with a GPU.
([[20, 18], [266, 18], [266, 66], [20, 66]], 'Ivan Ivanov', 0.9893577445949406)
([[23, 63], [75, 63], [75, 75], [23, 75]], 'For & start', 0.569582619643103)
([[107, 63], [165, 63], [165, 75], [107, 75]], 'ran ofart -', 0.7590258906640875)
([[174, 66], [196, 66], [196, 72], [174, 72]], 'us', 0.5712489261204313)
([[197, 63], [247, 63], [247, 75], [197, 75]], 'cian for J9', 0.4291845322335402)
([[24, 78], [138, 78], [138, 86], [24, 86]], 'rememcer participating', 0.2950869561675086)
([[139, 75], [201, 75], [201, 89], [139, 89]], 'in TV shows', 0.8357837855573321)
([[207, 75], [263, 75], [263, 89], [207, 89]], 'Eurovision;', 0.8857425664883629)
([[267, 75], [315, 75], [315, 89], [267, 89]], 'Golemite', 0.9758419318911099)
([[23, 89], [67, 89], [67, 103], [23, 103]], 'nadejdi"', 0.539809106221305)
([[81, 89], [161, 89], [161, 101], [81, 101]], 'Nova and shows', 0.6578596962690901)
([[177, 89], [205, 89], [205, 101], [177, 101]], 'BNT', 0.9997452811141291)
([[209, 89], [317, 89], [317, 101], [209, 101]], 'have participated and', 0.9815201983805392)
([[24, 104], [134, 104], [134, 112], [24, 112]], 'won Manxinternationa', 0.5457247148649338)
([[138, 104], [196, 104], [196, 112], [138, 112]], 'and nationa', 0.9969752634273912)
([[202, 104], [310, 104], [310, 112], [202, 112]], 'comderitions Vith MISt', 0.162093002062231)
([[23, 115], [217, 115], [217, 127], [23, 127]], 'prize and Grand Prix But apart from art', 0.807785585317762)
([[241, 115], [299, 115], [299, 129], [241, 129]], 'developing', 0.9401110380720452)
([[23, 129], [91, 129], [91, 141], [23, 141]], 'all directions:', 0.7119863549301918)
([[95, 129], [169, 129], [169, 141], [95, 141]], 'play sports and', 0.8891260348983956)
([[202, 130], [258, 130], [258, 138], [202, 138]], 'Drotessiona', 0.7617817598134959)
([[264, 130], [308, 130], [308, 138], [264, 138]], 'sv/immer', 0.29213256823081785)
([[43, 141], [91, 141], [91, 155], [43, 155]], 'lifeguard', 0.9796186521496251)
([[97, 139], [245, 139], [245, 155], [97, 155]], 'develcp iveosites, ML projects', 0.6113975851530729)
([[250, 142], [312, 142], [312, 150], [250, 150]], 'oclinestores', 0.2774046596778573)
([[43, 155], [131, 155], [131, 169], [43, 169]], 'tracing platfcrms;', 0.5682574315751218)
([[137, 155], [271, 155], [271, 167], [137, 167]], 'advertise my Dusinesseson', 0.6664885958969594)
([[23, 167], [195, 167], [195, 181], [23, 181]], 'sccial media; Instagram; Facebook', 0.7869463742539758)
([[265, 167], [319, 167], [319, 179], [265, 179]], 'all possible', 0.7167048390911115)
([[23, 179], [261, 179], [261, 195], [23, 195]], 'ways ofthe Zist century | deal with prcgramming', 0.5231686902835588)
([[265, 181], [321, 181], [321, 195], [265, 195]], 'encrypticn', 0.9987556526141949)
([[23, 195], [131, 195], [131, 209], [23, 209]], 'ano cryptocurrencics', 0.7686979642770775)
([[137, 195], [277, 195], [277, 207], [137, 207]], 'am communicative ana have', 0.43390206129099373)
([[22, 205], [293, 205], [293, 221], [22, 221]], 'experience with people from ell over the werld (through', 0.6392395295036012)
([[23, 218], [259, 218], [259, 234], [23, 234]], 'work) I have lived in Germany for scie tlmne and', 0.29930929987143273)
([[265, 219], [293, 219], [293, 233], [265, 233]], 'have', 0.9998962879180908)
([[23, 233], [201, 233], [201, 247], [23, 247]], 'certilicate fer proliclency In Gerian.', 0.41923437628378446)
([[208, 234], [310, 234], [310, 242], [208, 242]], 'canworkniphitJing', 0.07911733435654594)
([[24, 248], [46, 248], [46, 256], [24, 256]], 'nave', 0.781401515007019)
([[50, 248], [102, 248], [102, 256], [50, 256]], 'exderience', 0.47806146717844167)
([[116, 248], [138, 248], [138, 256], [116, 256]], 'tal', 0.3130374329009456)
([[137, 245], [175, 245], [175, 259], [137, 259]], 'field as', 0.6098227279791824)
([[183, 247], [249, 247], [249, 259], [183, 259]], 'leader- (Jguin', 0.3449103892824581)
([[255, 247], [315, 247], [315, 259], [255, 259]], 'Inrough my', 0.49342748414491755)
([[23, 259], [53, 259], [53, 273], [23, 273]], 'work)', 0.9994148271108847)
([[23, 287], [161, 287], [161, 305], [23, 305]], 'Employment History', 0.998952452834306)
([[341, 289], [391, 289], [391, 303], [341, 303]], 'Details', 0.9999360185747748)
([[24, 306], [74, 306], [74, 314], [24, 314]], 'Enterliner', 0.06259217955709694)
([[78, 306], [136, 306], [136, 314], [78, 314]], 'ADreamTeatn', 0.02030544640545002)
([[140, 306], [200, 306], [200, 314], [140, 314]], 'Enterlinmeni', 0.09383800820304204)
([[206, 308], [236, 308], [236, 314], [206, 314]], 'b +NX', 0.013608571108804823)
([[364, 306], [394, 306], [394, 314], [364, 314]], 'Hulanre', 0.20013818186651736)
([[24, 318], [60, 318], [60, 326], [24, 326]], 'JURE Zols', 0.29514107966577013)
([[66, 318], [112, 318], [112, 326], [66, 326]], 'Rvqustzol?', 0.1035091508728691)
([[340, 316], [390, 316], [390, 324], [340, 324]], '0k7/7770?', 0.10435504123033076)
([[384, 326], [458, 326], [458, 334], [384, 334]], 'vAlcha Donallen', 0.051336460875101526)
([[24, 340], [56, 340], [56, 348], [24, 348]], 'Pollstar', 0.530994348402605)
([[86, 340], [120, 340], [120, 348], [86, 348]], 'Julgari;', 0.33600645743290064)
([[136, 340], [168, 340], [168, 348], [136, 348]], '1Crion', 0.01099683096191544)
([[172, 340], [228, 340], [228, 348], [172, 348]], 'sunny Bcach', 0.5276075785066092)
([[24, 350], [56, 350], [56, 358], [24, 358]], 'JULYzole', 0.5508197688315049)
([[64, 350], [122, 350], [122, 358], [64, 358]], 'SEFTEYBER 20 IB', 0.61894280676005)
([[341, 355], [379, 355], [379, 369], [341, 369]], 'Links', 0.9999654004316152)
([[24, 372], [102, 372], [102, 380], [24, 380]], 'Customter Support', 0.4836303442147842)
([[116, 372], [164, 372], [164, 380], [116, 380]], 'Sutel Vafha', 0.36081382740576984)
([[342, 374], [378, 374], [378, 380], [342, 380]], '-ceboos', 0.026975896038334477)
([[340, 386], [374, 386], [374, 392], [340, 392]], 'lrec-', 0.12759357438485486)
([[24, 404], [96, 404], [96, 412], [24, 412]], 'Content Analysis', 0.5428163302589181)
([[104, 404], [188, 404], [188, 412], [104, 412]], 'at /elus Internationa', 0.23891218057983227)
([[194, 404], [216, 404], [216, 412], [194, 412]], 'Sona', 0.9764181971549988)
([[341, 411], [379, 411], [379, 425], [341, 425]], 'Skills', 0.9976639549489479)
([[342, 430], [380, 430], [380, 438], [342, 438]], "Comcute'", 0.19214688301399335)
([[388, 432], [412, 432], [412, 438], [388, 438]], 'KteT', 0.03330408036708832)
([[24, 436], [64, 436], [64, 444], [24, 444]], 'OAgoftw', 0.333516665278871)
([[77, 435], [137, 435], [137, 447], [77, 447]], 'test engincer', 0.7451384836425136)
([[146, 436], [198, 436], [198, 444], [146, 444]], 'Bosch Sofiz', 0.358103978717331)
([[342, 448], [386, 448], [386, 456], [342, 456]], 'Oroanizatio', 0.7309240839235335)
([[342, 466], [374, 466], [374, 474], [342, 474]], 'Sortware', 0.2208719845715806)
([[380, 468], [404, 468], [404, 476], [380, 476]], 'estng', 0.6277210961020974)
([[23, 475], [95, 475], [95, 489], [23, 489]], 'Education', 0.9999660648010068)
([[24, 494], [72, 494], [72, 502], [24, 502]], 'Geman C', 0.7917888975882673)
([[77, 491], [101, 491], [101, 505], [77, 505]], 'DSD', 0.9974849891794447)
([[107, 493], [299, 493], [299, 505], [107, 505]], 'at Geo Milev Language Hiah School; Dobrich', 0.5484418431055021)
([[56, 506], [82, 506], [82, 512], [56, 512]], 'Ekz0l', 0.03921345365322773)
([[88, 504], [122, 504], [122, 512], [88, 512]], 'AAY 2021', 0.158832298990717)
([[341, 503], [371, 503], [371, 515], [341, 515]], 'Aten', 0.2052796483039856)
([[340, 522], [384, 522], [384, 530], [340, 530]], "ATML'CSS", 0.3378152492638688)
([[24, 526], [82, 526], [82, 534], [24, 534]], 'Mechatronics', 0.7370850725962305)
([[94, 526], [278, 526], [278, 534], [94, 534]], 'Technical Univenity FDIBA Karlsruhe/Soha', 0.24879596799032597)
([[340, 540], [380, 540], [380, 548], [340, 548]], 'JavaScilpt', 0.20275657249762127)
([[24, 548], [72, 548], [72, 556], [24, 556]], 'Sull stuzvirz', 0.2112614476593378)
([[342, 560], [364, 560], [364, 566], [342, 566]], '7etan', 0.008261129699242987)
([[23, 583], [107, 583], [107, 599], [23, 599]], 'Intornships', 0.6608544526065875)
([[247.4187618062809, 61.18626652879327], [273.9587981127084, 64.71591167030863], [271.5812381937191, 76.81373347120673], [245.0412018872916, 73.28408832969137]], 'long', 0.318443238735199)
"""


from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import easyocr
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    
    image_stream = file.read()
    npimg = np.fromstring(image_stream, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(img)
    
    output_image = img.copy()
    for (bbox, text, prob) in results:
        if prob >= 0.25:
            top_left = tuple([int(val) for val in bbox[0]])
            bottom_right = tuple([int(val) for val in bbox[2]])
            cv2.rectangle(output_image, top_left, bottom_right, (0, 255, 0), 5)
            cv2.putText(output_image, text, (top_left[0], top_left[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    
    is_success, buffer = cv2.imencode(".jpg", output_image)
    io_buf = BytesIO(buffer)
    base64_string = base64.b64encode(io_buf.getvalue()).decode('utf-8')
    
    return render_template('index.html', uploaded_image=base64_string, extracted_text=' '.join([text for _, text, _ in results]))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
