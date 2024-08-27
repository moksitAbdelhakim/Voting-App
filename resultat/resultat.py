from flask import Flask, render_template
from redis import Redis
import os
import json

app = Flask(__name__)

#Premier endPoint
@app.route("/")
def resultat():
    #connecter a redis utilisant nom de service:
    db = Redis(host="redis", port=6379, db=0)
    if db.get(os.environ.get('EQUIPE_A', 'FC Barcelone')) is None:
        fcb_vote = 0
    else :
        fcb_vote = db.get(os.environ.get('EQUIPE_A', 'FC Barcelone'))

    if db.get(os.environ.get('EQUIPE_A', 'Real Madrid')) is None:
        real_vote = 0
    else :
        real_vote = db.get(os.environ.get('EQUIPE_A', 'Real Madrid'))

    if db.get(os.environ.get('EQUIPE_A', 'Liverpool')) is None:
        livre_vote = 0
    else :
        livre_vote = db.get(os.environ.get('EQUIPE_A', 'Liverpool'))
    if db.get(os.environ.get('EQUIPE_A', 'Manchester United')) is None:
        manchester_vote = 0
    else :
        manchester_vote = db.get(os.environ.get('EQUIPE_A', 'Manchester United'))

    votes = {
    'FC Barcelone': int(fcb_vote),
    'Real Madrid': int(real_vote),
    'Liverpool': int(livre_vote),
    'Manchester United': int(manchester_vote)
    }
    totale_votes = sum(votes.values()) 
    
    #liste pour stocker les pourcentages :
    for choix, vote in votes.items():
        votes[choix] = round(vote/totale_votes*100)
    return render_template("resultat.html", votes=votes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)