from functools import wraps
from flask import Blueprint, current_app, redirect, render_template, request, session
import jwt
import requests
import base64
from flask import session


bp_gui = Blueprint('gui', __name__, url_prefix='/gui')

def base64_encode_credentials(username, password):
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encoded_credentials

def token_required(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        # Check if token is present and valid
        if 'token' in session:
            # Token validation logic here
            # If token is valid, execute the decorated function
            return func(*args, **kwargs)
        else:
            # Redirect to login page if token is not present or invalid
            return redirect('/gui/login')
    return decorated_func



@bp_gui.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        encoded_credentials = base64_encode_credentials(username, password)
        headers = {'Authorization': f'Basic {encoded_credentials}'}
        url = "http://127.0.0.1:1337/api/v1/authenticate"

        payload = ""
        response = requests.request("GET", url, data=payload, headers=headers)
        if response.status_code == 200:
                response_data = response.json()
                if 'token' in response_data:
                    # Authentication successful, token received
                    token = response_data['token']
                    session['token'] = token
                    return redirect('/gui')
                else:
                    # Unexpected response format
                    return {'error': response.text}
        else:
            return {'error': response.text}

        # Redirect to a protected page
        
    else:
        return render_template('login.html')




@bp_gui.route('/protected')
@token_required
def clients():
    token = session.get('token')
    # Protected route accessible only with a valid token
    return render_template('index.html', name=token)





@bp_gui.route('/')
@token_required
def gui_index():
    return render_template('index.html')




# @bp_gui.route('/login')
# del 

@bp_gui.route('/test')
def test():
    template_loader = current_app.jinja_loader
    if isinstance(template_loader, dict):
        # When using a package loader, extract the search path
        template_folder_path = template_loader['__main__']._searchpath[0]
    else:
        # When using a FileSystemLoader, extract the root path
        template_folder_path = template_loader.searchpath[0]
    return f"Template folder path: {template_folder_path}"

    return render_template('test.html')

def authenticate(username, password):
    url = 'http://localhost:1337/api/v1/authenticate'  # Update the URL with your API's authentication endpoint
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        token = response.json().get('token')
        print(token)
        # Token received, perform further actions
        return token
    else:
        # Authentication failed, handle the error
        return None
    

def is_valid_token(token, secret_key):
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.InvalidTokenError:
        return False