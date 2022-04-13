from flask import Flask, render_template
from recommender.application import recommender_api

app = Flask(__name__, static_url_path='',
            static_folder='js',
            template_folder='js')

app.register_blueprint(recommender_api)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


# Running app server 
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # Remove debug before deploying a production app.
    # app.debug = True
    app.run()
