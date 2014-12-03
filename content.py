#layout
meta = {
        'author': 'drew verlee',
        'description' : 'Online Art Gallery',
        'keywords' : 'Art, Gallery, Flowers, Abstract, Stick',
        'viewport' : 'width=device-width, initial-scale=1.0, minimum-scale=1.0'
        }

internal_urls = ['home', 'gallery', 'about','purchase', 'tour', 'reviews']
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
drew_heading = "Amazing facts about drew"
about_drew='''Artistic mastermind drew Verlee was born in Michigan. Raised and
taught by wolves. His style has been hailed as revolutionary. A renowned time traveler
drew had the ability to study under many famous artists.'''

drew_facts = [
    'The flue gets drew shots',
    'Drew is the reason why Waldo is hiding',
    'Death once had a near-drew experience',
    'Drew makes onions cry'
    ]

# purchase
purchase_art = images + 'Flowers_1.jpg'
purchase_table = {
        'thead' : ['size', 'cost'],
        'tbody' : {'small': '$1,000', 'medium': '$3,000', 'large': '$6,000'}
        }
purchase_info="""Art is created on demand. As such prices will very greatly based on
the size, scope and complexity of the piece. Keep in mind a well drawn stick figure
can take months if not years to complete. Keeping that in mind, the table below
outlines roughly what you can expect as far as cost"""
email_form_heading="Send me an email with your order!"

# tour page
tour_art = images + 'Flowers_4.jpg'
tour_info="Here are some dates and locations where you can come see how amazing I am"
tour_table = {'Detroit': '4/7/2015', 'Croatia': '4/25/2015', 'Iceland': '5/20/2015'}

#reviews page
review_art = images + 'Abstract_4.jpg'
review_1 = """at first hulk think hulk should smash art. as hulk raise giant arms,
hulk suddenly overcome with emotion. hulk think, hulk shouldn't smash such
preety thing. hulk cry and star at drews art and think about place in world.
5/5 wouldn't smash - hulk"""
review_2 = """ He was an old man who fished alone in a skiff in the Gulf Stream
and he had gone eighty-four days now without taking a fish. In the first forty
days a boy had been with him. But after forty days without a fish the boy's
parents had told him that the old man was now definitely and finally salao,
which is the worst form of unlucky, and the boy had gone at their orders in
another boat which caught three good fish the first week. It made the boy sad
to see the old man come in each day with his skiff empty and he always went
down to help him carry either the coiled lines or the gaff and harpoon and the
sail that was furled around the mast. The sail was patched with flour sacks
and, furled, it looked like the flag of permanent defeat. -someone """
review_3 = """ Drews art touched me deeply. I mean look at it. Really look at it.
Something like this comes around once in a lifetime. I would buy all of his art.
In fact, don't even make him draw anything. Just give him all your money. 
Get up, right now, walk down to the bank and take out a huge Fing loan. Then
send that money to drew with no string attached - Not Drew"""
text_reviews = [review_1.upper(), review_2, review_3]


#TODO better way, read file
stick_art = [images + 'Stick_' + str(x) + '.jpg' for x in range(1,5)]
flowers_art = [images + 'Flowers_' + str(x) + '.jpg' for x in range(1,5)]
abstract_art = [images + 'Abstract_' + str(x) + '.jpg' for x in range(1,5)]
animated_art = ['abstract', 'ball', 'boom', 'heart', 'line']
animated_art = [images + x + '.gif' for x in animated_art]


gallery_art = {
        'stick': stick_art,
        'abstract': abstract_art,
        'flower': flowers_art,
        'animated': animated_art,
        }
