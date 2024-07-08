from flask import Flask, render_template


application = Flask(__name__)


@application.route("/")
def hello():
   return render_template("base.html")


@application.route("/minecraft")
def minecraft():
   return render_template("minecraft.html")

if __name__ == "__main__":
   application.run(host='0.0.0.0')
