#!/usr/bin/env python3
"""basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


config = Config()
app.config.from_object(config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """function to get a user from mock db

    Returns:
    user dictionary or
    None if the ID cannot be found or if login_as was not passed
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]
    return None


@app.before_request
def before_request() -> None:
    """
    use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """determine the best match languagr with our supported languages"""
    # Check for 'locale' argument in URL query string
    locale = request.args.get('locale')
    if locale in config.LANGUAGES:
        return locale
    if g.user and g.user.get("locale") in config.LANGUAGES:
        return g.user["locale"]
    return request.accept_languages.best_match(config.LANGUAGES)


@babel.timezone_selector
def get_timezone() -> str:
    """Determine the best match time zone with our supported time zones."""
    # Check for 'timezone' argument in URL query string
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check if user is logged in and has a preferred timezone
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def home() -> str:
    """returns a simple index page"""
    home_title = _("home_title")
    home_header = _("home_header")
    current_locale = get_locale()

    if g.user:
        message = _("logged_in_as", username=g.user["name"])
    else:
        message = _("not_logged_in")
    return render_template('6-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           current_locale=current_locale,
                           message=message)


if __name__ == '__main__':
    """run the app"""
    app.run(debug=True)
