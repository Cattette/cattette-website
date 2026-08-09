---
date: '2026-08-06T22:28:31+02:00'
draft: false
title: 'Qgis point labelling'
description: 'Article on labelling points in QGIS, covering manual labelling and some quality of life-hacks'
thumbnail: 'label-chaos.avif'
---

## On automatic labelling

I've yet to find a good automatic labelling engine in any software. A automatic
labelling engine is a program which automatially arranges labels according to
a set of rules. These rules typically include biases against overlap with other
labels, intersection into certain geometries, or automatic label sizing and
letter spacing. You'll find labelling engines not only in GIS software but also
in games such as the grand strategy titles of Paradox Interactive or even Rimworld.
But in the case of games, these often have very primitive labelling engines only
cappable of displaying a certain type of label on pre-rendered or currated geometries.

When making a complex map with a lot of features and labelled properties
the QGIS labelling algorithm is just unable to keep up. It is often unable
to find the most optimal location to place their labels and if features
are packed too tight it might just give up and not display your label. You
can try this out yourself by loading up the [Natural Earth populated places
layer](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-populated-places/),
activating labels, and zooming out.

## Manual labelling

This method of labelling is perhaps more accurately described as semi-manual
labeling. In software such as Photoshop and Inkscape the user is, after
all, expected to manually create text boxes and type out all place names
one-after-one. Never so in QGIS where labelling data already probably exists to
be tapped into by the label symbology.

When working with point labelling in QGIS I like to disable most features of the
labelling engine which you can do in two simple steps:
1. Navigate to the symbology layer of the point feature you're
working with and enable labels like normal. Now enter the 'Placement' tab, it is
the one next to the rightmost one in the labelling menu. Go to the bottom of this panel
and disable 'Features act as obstacles' setting.
2. Next, go to the rightmost tab called 'Rendering'
and change the 'Overlapping labels' drop-down-menu setting to 'Allow Overlaps without Penalty'.

This will disable most features of the labelling engine on this particular layer. You'll want to
repeat this process on other layers or labels if need be.

{{< image
    src="label-chaos.avif"
    caption="Labels after disabling the labelling engine"
    alt="Labels after disabling the labelling engine. The engines do not respect each others personal space and overlap without penalty"
    class="img-centered"
>}}

Now without the labelling engine your labels will overlap each other and other
features without any rhyme or reason. We can now start to manually adjusting the
positioning of the labels. If you have not done any manual labeling before you
may need to enable the labeling toolbar, you'll find it at the 'View' dropdown
menu, > 'Toolbars' > 'Label Toolbar'. A new set of tools will now appear on the
toolbar. You can hover over these tools to learn more about them and most of
them have pretty self-explanatory names.

The most important tool for us is the 'Move a label' tool. Click it, *make sure
your layer is in edit mode*, and click any label in your layer. A prompt asking
about key joining will appear and it will most likely already be set to `fid`,
`id`, or something similar, click 'OK'. What just happened is that the project
just created a auxiliary storage table. This is a form of virtual table attached
to the project and linked to your layer through the `fid`. So if feature
`Madrid` has the `fid` of `21`, the auxiliary table is able to pair the data it
stores for that `fid`.

What does this auxiliary storage table contain? It now contains two fields for
the x- and y-coordinate for the label of the feature, your point and label now
have coordinates independent of each other. If you continue using the 'Move a
label' tool you can now move labels, wherever you place them, information about
the labels new coordinate gets automatically added to the auxiliary table.

Remember that the auxiliary table is tied to the project and not the layer. This
means that if you open the layer in another project the label coordinate data
will not follow it. There are ways of exporting the auxiliary data but I will
not cover that here.

{{< image
    src="label-order.avif"
    caption="Labels ordered with manual labelling"
    alt="Labels ordered with manual labelling to ensure readability and accessibility"
    class="img-centered"
>}}

## Making labels follow the graticule automatically

{{< image
    src="curved-labels.avif"
    caption="Labels automatically following the graticule"
    alt="Labels arranged with a expression to always point towards the projected north. They appear to follow the graticule lines."
    class="img-centered"
>}}

You may have noticed that there is a tool to rotate the labels right
next to the move tool. You may be tempted to use it to make the labels
follow the latitudal graticule lines, but this process can be automated.
For this to work you need to make sure that your layer has the [same
projection](https://docs.qgis.org/3.44/en/docs/training_manual/processing/crs.html#crss-reprojecting)
as the one you want to work in. The standard automatic on-the-fly reprojection
will make this not work.

Navigate to your layers label panel and go to the placement tab. Scroll down to the 'Rotation'
option and change the dropdown option to 'Radians'. Click the little 'Data-defined override' context
menu and click 'edit...'. Paste this into the expression builder:

```
coalesce(
  "auxiliary_storage_labeling_labelrotation",
  coalesce(
      azimuth(
      make_point(
        "auxiliary_storage_labeling_positionx",
        "auxiliary_storage_labeling_positiony"
      ),
      make_point( [north pole x-coordinate], [north pole y-coordinate])
    )
  )
)
```

This code basically makes it so that if you don't explicitly define the label
rotation with the rotation tool, the label will automatically orient towards
the north pole. You'll need to input the cartesian coordinates for the north
pole in your projection for this to work. You can get them by finding the rought
location of the north pole on your map and clicking 'Copy Coordinate' > 'Map
CRS'

