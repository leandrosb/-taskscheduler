from flask import Flask
from apis import Api

app = Flask(__name__)

api.init_app(app)

app.run(debug=True)
