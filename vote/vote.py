from flask import Flask, render_template, request
import os
import redis

# A list of teams that users can vote for
equipe_a = os.environ.get('EQUIPE_A', 'FC Barcelone')
equipe_b = os.environ.get('EQUIPE_B', 'Real Madrid')
equipe_c = os.environ.get('EQUIPE_C', 'Liverpool')
equipe_d = os.environ.get('EQUIPE_D', 'Manchester United')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        # Code to store the vote in Redis goes here
        r = redis.Redis(host='redis', port=6379, db=0)
        choix = request.form["vote"]
        nbr_votes = r.get(choix)
        if nbr_votes is None:
            r.set(choix, 1)
        else:
            r.set(choix, (int(nbr_votes) + 1))

        return render_template('vote.html', equipe_choisis=choix)
        
    else:
        return render_template("index.html",
            equipe_a=equipe_a,
            equipe_b=equipe_b,
            equipe_c=equipe_c,
            equipe_d=equipe_d)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

