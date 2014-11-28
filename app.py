from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from flask.ext.heroku import Heroku
from jinja2 import Environment as Env
from hamlish_jinja import HamlishTagExtension, HamlishExtension


app = Flask(__name__)
heroku = Heroku(app)
app.debug = True


# add haml
app.jinja_env.add_extension(HamlishTagExtension)
app.jinja_env.add_extension(HamlishExtension)
app.jinja_env.hamlish_enable_div_shortcut = True

# compile assets
assets = Environment(app)
assets.url = app.static_url_path

css_bundle = Bundle('css/master.css.sass', filters='sass', output='all.css')
assets.register('css_all', css_bundle)

css_bundle = Bundle('css/flexbox-grid-5.0.0/css/flexboxgrid.min.css', output='flex.css')
assets.register('css_flex', css_bundle)

js_bundle = Bundle('js/test.js.coffee', filters='coffeescript', output='all.js')
assets.register('js_all', js_bundle)

#Should be in DB
meta = {
        'author': 'drew verlee',
        'description' : 'Online Art Gallery',
        'keywords' : 'Art, Gallery, Flowers, Abstarct',
        'viewport' : 'width=device-width, initial-scale=1.0, minimum-scale=1.0'
        }

internal_urls = ['index', 'abstract', 'flowers','purchase', 'tour', 'about']
copy_right = "NY, New York City 88516, Rich ave P0 234. &copy; 2014 DrewsArt.com ALL RIGHTS RESERVED."
logo = "DREW'S ART"

images = 'static/images/'

# TODO pre hooks
b = images + 'cover.png'
content = [b,b,b]
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html.haml',
            title="Home",
            meta=meta,
            logo=logo,
            internal_urls=internal_urls,
            copy_right=copy_right,
            content=content
            )


text='''Artistic mastermind drew Verlee was born in Michigan. Raised and
taught by wolves. His style has been hailed as revolutionary.'''
picture = images + 'drew.png'
art = images + 'cover.png'
external_links = { 'Bill', 'url'}
@app.route('/about')
def about():
    return render_template('about.html.haml',
            title="About",
            meta=meta,
            logo=logo,
            internal_urls=internal_urls,
            copy_right=copy_right,
            picture=picture,
            text=text,
            art=art,
            external_links=external_links
            )

purchase_info = "info about purchasing art. " * 20
art = images + 'cover.png'
table = {'small': '150', 'large': '200'}
@app.route('/purchase')
def purchase():
    return render_template('purchase.html.haml',
            title="purchase",
            meta=meta,
            logo=logo,
            internal_urls=internal_urls,
            purchase_info=purchase_info,
            copy_right=copy_right,
            art=art,
            table=table
            )

if __name__ == '__main__':
    app.run()
