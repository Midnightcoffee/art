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

css_bundle = Bundle('css/home.css.sass', filters='sass', output='all.css')
assets.register('css_all', css_bundle)

js_bundle = Bundle('js/test.js.coffee', filters='coffeescript', output='all.js')
assets.register('js_all', js_bundle)



@app.route('/')
def hello_word():
    return render_template('index.html.haml',
            title="Home",
            banner="DrewsArt")



if __name__ == '__main__':
    app.run()
