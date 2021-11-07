from flask import Flask, request, Response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    user = request.args.get('user')
    password = request.args.get('password')
    if ((user == 'aday') and (password == '1234')):
        return Response(
            "OK",
            status=200,
        )
    else:
        return Response(
            "KO",
            status=401,
        )

if __name__ == '__main__':
     app.run(port='5000')
