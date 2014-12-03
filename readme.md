Webapp for 3750
==================
I have built websites before. But the design was always an after thought. Thus,
designing the website was a new experience for me.

Extra - Please read
========================
Where is the mobile.css and print.css? - I didn't make a mobile.css and print.css 
because i thought it better to simply include the small changes i needed inside
the master.css page like so...

.logo
  ... some styles  
  @include responsive(small-screens) # checks to see if were 'mobile'
    font-size: 2em
    text-align: center
  @media print # if were printing change the size of the font..
    font-size: 1em

Validation - some errors concerning external libraries that i couldn't resolve

Styling and design
==========================
I wanted a darker theme to bring an elegance to my design.  Thats why i use
mainly black and grey. I also wanted the site to be responsive, which i talk about below.

Things I struggled with:

=======================
Responsive design
=================
it's hard to build a site that does well on multiple 
screen sizes. I read two books on responsive web design and several posts 
online on the topic. The conclusion was while you can get far with media
queries, fluid designs, etc.. the future is something like flexbox by mozzila.

I would use flexbox on a real project, given the right requirements, but
in this case I just used max-widths, ems, and percentages along with a limited
media query to do the project.

ids vs class
=================
I understand their use but its not obvious to me when 
to use one vs another at the start.

i didn't overcome this problem.


css structure
=======================
sometimes a hierarchy isn't important, should i just 
push things to the left or layer things?

.nav

.link

VS

.nav
  .link

I end ended up layering in most cases


DRY css
=======================
I feel like with some slight tweeks i could have half the code.
But a lot of code shared code doesn't have an obvious parent. TODO

sass helps but i'm sure with more experience i'll get better at this


nameing stuff
=======================
naming variables is always hard. I think better names 
comes with better understanding of what your doing and keeping things 
dry. Example gallery_select, probably should just be 'select' under
gallery...





