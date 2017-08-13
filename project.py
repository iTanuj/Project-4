from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash, make_response
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Game, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Games Catalog Application"

credentials = {}
token_info = {}

# Connect to Database and create database session
engine = create_engine('sqlite:///gamescatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# JSON endpoints
@app.route('/category/JSON/')
def cateJSON():
    categories = session.query(Category).order_by(asc(Category.name))
    return jsonify(categories=[category.serialize for category in categories])


@app.route('/category/<int:category_id>/games/JSON/')
def gameJSON(category_id):
    items = session.query(Game).filter_by(category_id=category_id)
    return jsonify(items=[item.serialize for item in items])


@app.route('/category/<int:category_id>/games/<int:game_id>/JSON')
def menuItemJSON(category_id, game_id):
    game = session.query(Game).filter_by(id=game_id).one()
    return jsonify(Game=game.serialize)


# Homepage
@app.route('/')
@app.route('/category')
def showCategories():
    if login_session.get('state') is None:
        login_session['state'] = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for x in xrange(32))
    categories = session.query(Category).order_by(asc(Category.name))
    recents = session.query(Game).order_by(desc(Game.id)).limit(10)
    return render_template(
        "categories.html",
        categories=categories, recents=recents, STATE=login_session['state'],
        user_id=login_session.get('user_id'))


# Show games of a category
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/games/')
def showGames(category_id):
    if login_session['state'] is None:
        login_session['state'] = ''.join(
            random.choice(string.ascii_uppercase+string.digits)
            for x in xrange(32))
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Game).filter_by(category_id=category_id).all()
    return render_template(
        'cateGames.html', items=items, category=category,
        categories=categories, user_id=login_session.get('user_id'),
        STATE=login_session['state'])


# Show a game of a category
@app.route('/category/<int:category_id>/games/<int:game_id>/')
def showGame(category_id, game_id):
    if login_session['state'] is None:
        login_session['state'] = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for x in xrange(32))
    categories = session.query(Category).order_by(asc(Category.name))
    game = session.query(Game).filter_by(id=game_id).one()
    return render_template(
        'game.html', categories=categories,
        STATE=login_session['state'], item=game,
        user_id=login_session.get('user_id'))


# Create a new game
@app.route('/category/<int:category_id>/games/new/', methods=['GET', 'POST'])
def newGame(category_id):
    if 'username' not in login_session:
        return redirect('/category')
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = Game(
            name=request.form['name'],
            description=request.form['description'], category_id=category_id,
            user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showGames', category_id=category_id))
    else:
        return render_template(
            'newGame.html', category=category, STATE=login_session['state'])


# Edit a game
@app.route('/category/<int:category_id>/games/<int:game_id>/edit',
           methods=['GET', 'POST'])
def editGame(category_id, game_id):
    if 'username' not in login_session:
        return redirect('/category')
    editedItem = session.query(Game).filter_by(id=game_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash('Game Successfully Edited')
        return redirect(url_for('showGame', category_id=category_id,
                        STATE=login_session['state'], item=editedItem))
    else:
        return render_template(
            'editGame.html', category_id=category_id, item=editedItem,
            STATE=login_session['state'])


# Delete a game
@app.route('/category/<int:category_id>/games/<int:game_id>/delete',
           methods=['GET', 'POST'])
def deleteGame(category_id, game_id):
    if 'username' not in login_session:
        return redirect('/category')
    category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(Game).filter_by(id=game_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Game Successfully Deleted')
        return redirect(url_for('showGames', category_id=category_id))
    else:
        return render_template(
            'deleteGame.html', category_id=category_id, item=itemToDelete,
            STATE=login_session['state'])


# Signing in begins
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
                'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['email'] = data['email']

    # See if a user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    response = make_response(json.dumps('User successfully connected.'), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# Logging out - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result.get('status') == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['user_id']

        return redirect('/category')
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
