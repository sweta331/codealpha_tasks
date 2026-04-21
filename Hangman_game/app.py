from flask import Flask, render_template, request, session, redirect, url_for
from game import start_game, process_guess

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def home():
    if "state" not in session:
        session["state"] = start_game()

    state = session["state"]

    display = " ".join([l if l in state["guessed"] else "_" for l in state["word"]])
    win = False
    lose = False

    if request.method == "POST":
        guess = request.form.get("letter")
        state, display, win, lose = process_guess(state, guess)
        session["state"] = state

    return render_template(
    "index.html",
    display=display,
    guessed=state["guessed"],
    wrong=state["wrong"],
    win=win,
    lose=lose,
    word=state["word"]
)

# ✅ FIXED RESET
@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("home"))   # 👈 important

if __name__ == "__main__":
    app.run(debug=True)