from flask import Flask, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuration for Google OAuth
GOOGLE_CLIENT_ID = 'your_google_client_id'
GOOGLE_CLIENT_SECRET = 'your_google_client_secret'
GOOGLE_REDIRECT_URI = 'http://localhost:5000/google/callback'

# Configuration for Facebook OAuth
FACEBOOK_CLIENT_ID = 'your_facebook_client_id'
FACEBOOK_CLIENT_SECRET = 'your_facebook_client_secret'
FACEBOOK_REDIRECT_URI = 'http://localhost:5000/facebook/callback'

oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    refresh_token_params=None,
    redirect_uri=GOOGLE_REDIRECT_URI,
    client_kwargs={'scope': 'openid profile email'},
)

facebook = oauth.register(
    name='facebook',
    client_id=FACEBOOK_CLIENT_ID,
    client_secret=FACEBOOK_CLIENT_SECRET,
    authorize_url='https://www.facebook.com/dialog/oauth',
    authorize_params=None,
    access_token_url='https://graph.facebook.com/oauth/access_token',
    access_token_params=None,
    refresh_token_url=None,
    refresh_token_params=None,
    redirect_uri=FACEBOOK_REDIRECT_URI,
    client_kwargs={'scope': 'email'},
)

@app.route('/')
def index():
    return 'Welcome! Please <a href="/login">login</a> with Google or Facebook.'

@app.route('/login')
def login():
    redirect_uri = url_for('login', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/google/callback')
def google_callback():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)
    # Handle user info (e.g., save to database, set session)
    return 'Google login successful!'

@app.route('/facebook/callback')
def facebook_callback():
    token = facebook.authorize_access_token()
    resp = facebook.get('me?fields=id,email')
    user_info = resp.json()
    # Handle user info (e.g., save to database, set session)
    return 'Facebook login successful!'

if __name__ == '__main__':
    app.run(debug=True)
