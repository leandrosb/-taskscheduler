from flask import Flask
from apis import api

app = Flask
api.init_app(app)

app.run(debug=True)
