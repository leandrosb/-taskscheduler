import os
from flask import Flask
from waitress import serve

app = Flask(__name__)


def main():
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port,
          threads=int(os.getenv("APP_THREADS", "1")))


if __name__ == '__main__':
    main()
