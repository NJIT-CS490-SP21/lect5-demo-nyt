from flask import Flask, render_template
import os
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    print('Updated printline')
    random_number = random.randint(1, 4)
    tv_shows = ['Mandalorian', 'Queens Gambit', 'Avatar', 'Korra', 'The Office']
    return render_template(
        "index.html",
        num = random_number,
        my_show = tv_shows[random_number]
    )
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)