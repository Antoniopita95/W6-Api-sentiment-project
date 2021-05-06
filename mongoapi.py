from flask import Flask, request
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
#import tools.postdata as pos




app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

@app.route("/quotes")
def quotes_():
   """
   Function to see all the quotes
   """
    quotes = get.quotes()
    return jsonify(quotes)


@app.route("/quotes/<char>")
"""
Function that let you find all the quotes from a certain character
"""
def quotes_char(char):
    quotes = get.dialogue(char)
    return jsonify(quotes)

@app.route("/quotes/<scene>")
"""
Function that let you find all the quotes from a certain character
"""
def quotes_scene(scene):
    quotes = get.scene_(scene)
    return jsonify(quotes)


"""
@app.route("/dialog/<char>")
def dialog_(char):
    quotes = get.dialog(char)
    return jsonify(quotes)

@app.route("/quotes_movie/<movie>") 
def quotes_movie(movie):
    quotes = get.quotes_movie(movie)
    return jsonify(quotes)

    
@app.route("/movies")
def movies():
    quotes = get.movies()
    return jsonify(quotes)
 @app.route()

 """








app.run(debug=True)
























