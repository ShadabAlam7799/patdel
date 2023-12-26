from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        title_length = len(title)
        return render_template('result.html', title=title, title_length=title_length)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
