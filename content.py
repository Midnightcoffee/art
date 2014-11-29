#layout
meta = {
        'author': 'drew verlee',
        'description' : 'Online Art Gallery',
        'keywords' : 'Art, Gallery, Flowers, Abstarct',
        'viewport' : 'width=device-width, initial-scale=1.0, minimum-scale=1.0'
        }

internal_urls = ['home', 'abstract', 'flowers','purchase', 'tour', 'about']
copy_right = "NY, New York City 88516, Rich ave P0 234. &copy; 2014 "
logo = "DREW'S ART"

#global
images = 'static/images/'
alt = 'art piece'

#cover
cover_art = ['Abstract_4.jpg', 'Flowers_2.jpg', 'Stick_1.jpg']
cover_art = [images + a for a in cover_art]
external_links = {
        'Michael Whelan' : 'www.michaelwhelan.com/',
        'pablo picasso'  : 'http://en.wikipedia.org/wiki/Pablo_Picasso',
        'Lenonardo da vinci' : 'http://en.wikipedia.org/wiki/Leonardo_da_Vinci',
        'Vincent van Gogh' : 'http://en.wikipedia.org/wiki/Vincent_van_Gogh',
        'Andy Warhol' : 'http://en.wikipedia.org/wiki/Andy_Warhol'
        }

email_hyper_link= 'drew.Verlee@gmail.com'

#about
picture_of_drew = images + 'drew.jpg'
about_art = images + 'Stick_3.jpg'
# purchase
purchase_art = images + 'Flowers_1.jpg'
purchase_table = {'small': '150', 'large': '200'}
purchase_info="Prices vary by something something something..."
