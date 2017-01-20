from flask import Flask, request, jsonify
from sense_hat import SenseHat
__author__ = 'agrimasthana'

sense = SenseHat()
app = Flask(__name__)


@app.route("/setpixels", methods=['POST'])
def setpixels():
    _pixels = request.json['pxls']
    try:
        sense.clear()
        sense.set_pixels(_pixels)
    except Exception as error:
        return error
    return jsonify({'status': 'done'})


@app.route("/setpixel", methods=['POST'])
def setpixel():
    _pixel = request.json['pxls']
    try:
        sense.clear()
        sense.set_pixels([_pixel]*64)
    except Exception as error:
        return error
    return jsonify({'status': 'done'})


@app.route("/clear", methods=['GET'])
def setpixel():
    try:
        sense.clear()
    except Exception as error:
        return error
    return jsonify({'status': 'done'})\

@app.route("/getpixel", methods=['GET'])
def getpixel():
    reqpxl = request.args.get('coords')
    try:
       respxl = sense.get_pixel(reqpxl[0], reqpxl[1])
    except Exception as error:
        return error
    return jsonify({'pixel': respxl})


@app.route("/humidity", methods=['GET'])
def gethumidity():
    try:
       humidity = sense.get_humidity();
    except Exception as error:
        return error
    return jsonify({'humidity': humidity})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
