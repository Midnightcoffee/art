from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from flask.ext.heroku import Heroku
from jinja2 import Environment as Env
from hamlish_jinja import HamlishTagExtension, HamlishExtension
from content import *


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



@app.template_global()
def head():
    return render_template('head.html.haml',
            meta=meta,
            )

@app.template_global()
def header():
    return render_template('header.html.haml',
            logo=logo,
            internal_urls=internal_urls,
            )

@app.template_global()
def footer():
    return render_template('footer.html.haml',
            internal_urls=internal_urls,
            copy_right=copy_right,
            email_hyper_link=email_hyper_link
            )

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html.haml',
            title="Home",
            cover_art=cover_art,
            alt=alt
            )

about_drew='''Artistic mastermind drew Verlee was born in Michigan. Raised and
taught by wolves. His style has been hailed as revolutionary. A renowned time traveler
drew had the ability to study under many famous artists'''



@app.route('/about')
def about():
    return render_template('about.html.haml',
            title="About",
            alt=alt,
            picture_of_drew=picture_of_drew,
            about_drew=about_drew,
            external_links=external_links,
            about_art=about_art,
            )


@app.route('/purchase')
def purchase():
    return render_template('purchase.html.haml',
            title="Purchase",
            alt=alt,
            purchase_info=purchase_info,
            copy_right=copy_right,
            purchase_art=purchase_art,
            purchase_table=purchase_table
            )

if __name__ == '__main__':
    app.run()
