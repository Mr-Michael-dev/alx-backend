#!/usr/bin/env python3
"""basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


config = Config()
app.config.from_object(config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match languagr with our supported languages"""
    return request.accept_languages.best_match(config.LANGUAGES)


@app.route('/')
def home() -> str:
    """returns a simple index page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
