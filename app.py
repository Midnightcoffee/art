from flask import Flask, render_template, request
from flask.ext.assets import Environment, Bundle
from flask.ext.heroku import Heroku
from flask.ext.triangle import Triangle
from jinja2 import Environment as Env
from hamlish_jinja import HamlishTagExtension, HamlishExtension
from content import *

#setup app

app = Flask(__name__, static_path='/static')
Triangle(app)
heroku = Heroku(app)
app.debug = True


# add haml
app.jinja_env.add_extension(HamlishTagExtension)
app.jinja_env.add_extension(HamlishExtension)
app.jinja_env.hamlish_enable_div_shortcut = True

# compile assets
assets = Environment(app)
assets.url = app.static_url_path
# css

#TODO: this isn't how to use assets, investigate when time
css_bundle = Bundle('css/master.css.sass', filters='sass', output='all.css')
assets.register('css_all', css_bundle)

slick_css = 'slick-1.3.15/slick/slick.css'
css_bundle = Bundle(slick_css, output='slick.css')
assets.register('slick_css', css_bundle)

js_bundle = Bundle('js/test.js.coffee', filters='coffeescript', output='all.js')
assets.register('js_all', js_bundle)

jquery = 'js/jquery-1.11.1.min.js'
js_bundle = Bundle(jquery, output='jquery.js')
assets.register('jquery_all', js_bundle)

jquery_migrate = 'js/jquery-migrate-1.2.1.min.js'
js_bundle = Bundle(jquery_migrate, output='jquery_migrate.js')
assets.register('jquery_migrate_all', js_bundle)

slick = 'slick-1.3.15/slick/slick.min.js'
js_bundle = Bundle(slick, output='slick.js')
assets.register('slick_all', js_bundle)

angular = 'angular.min.js'
js_bundle = Bundle(angular, output='angular.js')
assets.register('angular_all', js_bundle)

# # javascript



# ============ views ==================
# global views

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


# normal views
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html.haml',
            title="Home",
            cover_art=cover_art,
            alt=alt
            )


@app.route('/about')
def about():
    return render_template('about.html.haml',
            title="About",
            alt=alt,
            picture_of_drew=picture_of_drew,
            about_drew=about_drew,
            external_links=external_links,
            about_art=about_art,
            drew_facts=drew_facts,
            )


@app.route('/purchase')
def purchase():
    return render_template('purchase.html.haml',
            title="Purchase",
            alt=alt,
            purchase_info=purchase_info,
            purchase_art=purchase_art,
            purchase_table=purchase_table,
            email_form_heading=email_form_heading,
            )

@app.route('/tour')
def tour():
    return render_template('tour.html.haml',
            title="Tour",
            alt=alt,
            tour_info=tour_info,
            tour_art=tour_art,
            tour_table=tour_table
            )


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    art = gallery_art['stick']
    if request.method == 'POST':
        art = gallery_art.get(request.form.get('art_selection'))
    return render_template('gallery.html.haml',
            options=gallery_art.keys(),
            art=art)

if __name__ == '__main__':
    app.run()
