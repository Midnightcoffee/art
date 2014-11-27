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


internal_urls = ['index', 'stick', 'abstract', 'flowers', 'custom', 'tour', 'about']
footer = "NY, New York City 88516, Rich ave P0 234. &copy; 2014 DrewsArt.com ALL RIGHTS RESERVED."
logo = "Drew'sArt"

#ahhh
# b = "static/images/Cover_"
# cover_art = [0,1,2]
# cover_art = [b + str(x) + ".jpg" for x in cover_art]
b = 'static/images/cover.png'
content = [b,b,b]


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    # TODO pre hooks
    return render_template('index.html.haml',
            title="Home",
            logo=logo,
            internal_urls=internal_urls,
            footer=footer,
            content=content
            )

if __name__ == '__main__':
    app.run()
