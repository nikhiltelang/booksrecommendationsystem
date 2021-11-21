from flask import Flask, request, render_template
from flask import Response

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return Response('index.html')

@app.route("/predict", methods=['GET','POST'])
def predictRouteClient():
    try:
        pass
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)
    return Response("Prediction Is working")

@app.route("/train", methods=['GET','POST'])
def trainRouteClient():
    try:
        pass
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)
    return Response("Working Successfully")
if __name__ == "__main__":
    app.run()
