from functools import wraps
from flask import Blueprint, current_app, redirect, render_template, request, session

bp_gui = Blueprint('gui', __name__, url_prefix='/gui')



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
        # Validate the username and password
        # If valid, generate a token
        # Store the token in session or secure cookie
        session['token'] = 'generated_token'
        # Redirect to a protected page
        return redirect('/gui/protected')
    else:
        return render_template('login.html')

@bp_gui.route('/protected')
@token_required
def protected():
    # Protected route accessible only with a valid token
    return 'Protected Content'





@bp_gui.route('/')
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
    #return f"Template folder path: {template_folder_path}"

    return render_template('test.html')

