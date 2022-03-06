from flask import Flask, jsonify, request
import csv

allmovies=[]
with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]

likedmovies=[]
nonlikedmovies=[]
didnotwatch=[]

app=Flask(__name__)
@app.route("/get-movie")
def getmovie():
    return jsonify({
        "data": allmovies[0],
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def likedmovie():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    likedmovies.append(movie)
    return jsonify({
        "status": "success"
    }),201

@app.route("/nonliked-movie", methods=["POST"])
def nonlikedmovie():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    nonlikedmovies.append(movie)
    return jsonify({
        "status": "success"
    }),201

@app.route("/didnotwatch", methods=["POST"])
def didnotwatch():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    didnotwatch.append(movie)
    return jsonify({
        "status": "success"
    }),201

if __name__=="__main__":
    app.run()