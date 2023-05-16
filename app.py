from flask import Flask, render_template
from flask import request
import urllib.request, json

# Define app name
app = Flask(__name__)

# Data Structure
fruit_list = []
records = []

# Create a route for the project
@app.route('/', methods=["GET", "POST"])

# Define a funcion to be executed in route
def main():

    #fruit_list = ["Strawberry","Grapes","Apple","Papaya","Orange", "Pineaple", "Pear", "Melon"]

    if request.method == "POST":
        if request.form.get("fruit"):
            fruit_list.append(request.form.get("fruit"))
    return render_template("index.html", fruit_list=fruit_list)

# Create a route for another page
@app.route('/teacher_diary', methods=["GET", "POST"])
def teacher_diary():

    #grades_list = {"Leo":8.8, "Rick":8.8, "Arthur":8.9, "Matheus":9.0, "Maria":10.0}

    if request.method == "POST":
        if request.form.get("student") and request.form.get("grade"):
            records.append({"student": request.form.get("student"), "grade": request.form.get("grade")})
    return render_template("about.html", records=records)

# Create a route for movies section
@app.route('/movies/<property>')
def movies(property):

    if property == 'popular':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=16aa2bb14b8cd9f4b85571e3b9e0517f"
    elif property == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=16aa2bb14b8cd9f4b85571e3b9e0517f"
    elif property == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=16aa2bb14b8cd9f4b85571e3b9e0517f"
    elif property == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=16aa2bb14b8cd9f4b85571e3b9e0517f"
    elif property == 'tom_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=16aa2bb14b8cd9f4b85571e3b9e0517f"

    # Open URL
    response = urllib.request.urlopen(url)

    # Read data from response
    data = response.read()

    # Converts to json format
    jsondata = json.loads(data)

    return render_template("movies.html", movies=jsondata['results'])

if __name__ =="__main__":
    app.run(debug=True)

# http://127.0.0.1:5000
# "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=16aa2bb14b8cd9f4b85571e3b9e0517f"
# 
# 
# 
# 