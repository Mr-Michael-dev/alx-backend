#!/usr/bin/env python3
"""this module contains a basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """a basic configuration class
    defines languages, default locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


config = Config()
app.config.from_object(config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match language with our supported languages

    returns:
    A string that best match the language
    """
    return request.accept_languages.best_match(config.LANGUAGES)


@app.route('/')
def home() -> str:
    """
    defines the application logic for the home route

    Returns:
    index page
    """
    home_title = _("home_title")
    home_header = _("home_header")
    current_locale = get_locale()
    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           current_locale=current_locale)


if __name__ == '__main__':
    """run the app"""
    app.run(debug=True)
