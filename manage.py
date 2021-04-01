import os

from apps import create_app

env = os.environ.get("APP_ENV", "development")
app = create_app(env)

if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=8000)
