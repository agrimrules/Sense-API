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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
