from flask import Flask, render_template
import random
from datetime import datetime

random_num = random.randint(1, 9)
print(random_num)

app = Flask(__name__)


@app.route("/")
def guess_num_image():
    c_year = datetime.now().year
    print(c_year)
    return render_template("index.html", current_year=c_year)


@app.route('/<int:post_id>')
def show_post(post_id):
    # show the with the given id, the id is an integer
    if post_id < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif post_id > random_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
