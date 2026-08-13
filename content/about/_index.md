+++
date = '2026-07-29T17:59:16+02:00'
draft = false
title = 'About'
+++

## This site

This website serves as my personal weblog, where I share my artwork and other things that
interest me. It replaces my previous presence on Reddit, Twitter and DeviantArt, as I have grown
increasingly cynical about the direction and overall state of those (and many other!) platforms
over the years.

I started building this website with no web development experience. I first wrote everything as
individual HTML files, but that quickly became tedious. I then tried automating the process
with Bash scripts, [Pandoc](https://pandoc.org/), and Python, only to find those solutions growing
just as cumbersome.

Eventually I settled on [Hugo](https://gohugo.io/), an open-source static site generator.
A static site generator produces static HTML files from markdown files, HTML templates,
and data files. This makes them ideal for small sites such as blogs or documentation sites which
only need to update their information once in a while and less suitable for social networks or
large storefronts. You can find the Git repo for this entire project
[here](https://github.com/Cattette/cattette-website).

This website uses no JavaScript, no cookies, and no trackers. It does, however, use HTML5.
I've gathered that this is a grave sin according some Indieweb purists out there but
I cannot be bothered to pore over documentation and compatibility tables to see if a given
semantic is supported by the final Netscape release. Besides, I think some semantics here
and there are neat.

### Fonts

This website does not force your browser to download a font because I consider that rude. 
I'm instead using the [web safe](https://www.w3schools.com/cssref/css_websafe_fonts.php)
font of Garamond. Georgia or it's open source cousin [Gelasio](https://github.com/sorkintype/Gelasio)
are used if you do not have Garamond, and your default serif font takes over if all else fails.

I do not follow [the view](https://seirdy.one/posts/2020/11/23/website-best-practices/#about-fonts)
that developer-set fonts and font sizes are, as a rule, inappropriate. Thought out typography is generally
far too sensetive for default system fonts to just be slotted in.

This website also overrides the default font sizes because whoever came up with
the idea that h1 should be over twice as big as the default body text should...
well, whoever they are they're probably not around anymore. Furthermore,
the default web body text has simply not kept up with modern screens, and so we're
changing that as well.

[Iosevka](https://github.com/be5invis/iosevka) is the preferred monospace font.

### Image formats

Its been 30 years since PNG and JPEG started to (mostly) replace
the TIFF and GIF brothers. Since then we've made great leaps
in compression algorithms but these efforts have mostly borne fruit
in the realm of online video delivery.

Despite the advent of many new image formats, many optimized for the
web, adoption of these formats have been very slow. [^1]

WebP is developed by Google, who also have a
direct hand in developing the majority of the competing image
formats for some reason. It is fairly popular these days but
even this format is starting to become outdated as other
formats have made further advancements since it's already been
15 years since its release in 2010.

HEIF, or HEIC probably doesn't qualify as a web format because
of the fact that many browsers simply don't support them. In spite of this
the format has been adopted by Apple as the default output format
for all their phone cameras.

JPEG-XL and AVIF are the current frontrunners in
the low-intensity format war and the question of
which one is the superior new image format feels
inconsequential. Both of them are generations
ahead at both lossless and lossy compression
compared the formats they seek to replace so we should
probably just get on with it.

I don't grasp enough about the technical differences between
these two formats but I do know that AVIF has more support
on web browser so I have picked it as the format of choice
for this website.

### Image hygiene

Good image practice, what I like to call 'image
hygiene', is the art of composing your web images
in a way that compliments image format technology.
For better or worse virtually all non-text
and non-video information conveyed through the
internet are done by images made out of individual
pixels.

I may dream of a web world where vector graphics
ended up being used more where they make sense but
we don't live in that reality.

I don't use more colors than necessary, I,
don't make the images larger than necessary,
I don't make them more complex than necessary.
These considerations complements color indexing,
resolution and general compression algorithms to
the extent that I would argue that this is more
impactful than any image format choice.

This is the typical [Magick](https://imagemagick.org/)
command I use to optimize graphics I have prepared:

`convert in.png -colors 2 -format avif out.avif`

You would think that screenshots of software should be an
easy thing to optimize since they only have a relatively
small amount of flat colors in them. And this would be
true were it not for shadows and font hinting. I circumvent
these obstacles by temporarily switching to a bitmap font
whenever possible and disabling shadows. If the font can't
be switched we can manually index our screenshot with
GIMP using a custom palette. This custom palette needs
to be created manually by picking all main colors of the
screenshot + adding a few extra colors sampled from font
subpixels.



<!-- footnotes -->

[^1]: This is not strictly true for all websites. Just as many fancy
sites will disguise videos as GIFs many sites will disguise their WebPs
as JPEGs or PNGs.




<!-- ## my interests -->

<!-- ### history -->

<!-- These days history is a peripheral interest of mine. It used to be my favourite subject in school -->
<!-- but as time has passed so has my strong fascination with the past. These days I only passively -->
<!-- consume history through media, mainly YouTube videos. Some of my favourite creators include: -->
<!-- [The Histocrat](https://www.youtube.com/@TheHistocrat/videos), -->
<!-- [Fredda](https://www.youtube.com/@FreddaYT), -->
<!-- [Rosencreutz](https://www.youtube.com/@Rosencreutzzz), and -->
<!-- [Smarthistory](https://www.youtube.com/@smarthistory-art-history), -->

<!-- ### geography -->

<!-- Geography is my chief interest as of late. My love for the subject inspired my career-choice, -->
<!-- other hobbies, and lifestyle. Geography has something for everybode. Love math? Look up geodesy, -->
<!-- love engineering? Geo-engineering. Love the outdoors? Surveying. Love nature? Geology. --> 

<!-- ### photography -->

<!-- ### computers and software -->

<!-- ### music -->

<!-- ### video games -->
