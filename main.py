from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'dasopdfjlskfjdss'

@app.route('')
def main_page():
    return render_template('')


if __name__ == '__main__':
    app.run()
