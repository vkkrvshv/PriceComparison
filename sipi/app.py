from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Основная функция веб-сервиса, отвечающая за рендер главной html-страницы

    :return: render_template('main.html')
    """
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
