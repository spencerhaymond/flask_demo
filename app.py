from flask import Flask, render_template, request
from jokes import jokes_dict


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/jokes', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        joke_type = request.form.get('category')
        joke = get_jokes_by_category(joke_type)
        print(joke)
        test = jokes_dict[joke_type]
        print(test)
        return render_template('joke_output.html', joke = joke)
    return render_template('main.html')



def get_jokes_by_category(category):
    return jokes_dict.get(category)