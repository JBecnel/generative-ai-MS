from flask import Flask, request
from markupsafe import escape
import os

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    """
    Greet the user with a name passed as a query parameter.
    Defaults to 'World' if no name is provided.
    Escapes input to prevent injection or XSS.
    """
    name = escape(request.args.get('name', 'World'))
    return f'Hello, {name}!'

if __name__ == '__main__':
    # Enable debug mode only if FLASK_DEBUG=true is set in the environment
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
