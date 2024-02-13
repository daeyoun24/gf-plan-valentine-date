from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/yes')
def yes():
    return render_template('yes.html')


@app.route('/no/<int:image_index>')
def no(image_index):
    if 1 <= image_index <= 8:
        img_file = f'image{image_index}.jpg'
    else:
        img_file = 'image1.jpg'

    return render_template('no.html', image_file=img_file)


@app.route('/food', methods=['POST'])
def food():
    selected_date = request.form['date']

    return render_template('food.html', selected_date=selected_date)


@app.route('/end')
def end():
    food_id = request.args.get('food_id')
    date = request.args.get('date')

    return render_template('end.html', food_id=food_id, date=date)


if __name__ == '__main__':
    app.run(debug=True)
