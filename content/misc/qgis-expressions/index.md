---
date: '2026-08-03T15:55:49+02:00'
draft: false
title: 'Expressions and variables in QGIS'
description: 'This article discusses the basics of expressions and variables in QGIS'
thumbnail: 'fractional-resize.avif'
---

QGIS is a data-focused program. This means that the data forms, layers,
geometries, and bitmaps it can process all can contain a lot of data. This
differs from other potential mapping software such as Inkscape, Photoshop, or
Adobe Illustrator where geometries and pixels don't contain any more information
than what they represent visually: what you see is what you get.

In QGIS a line layer representing rivers may contain a lot more information
than what just meets the eye. This layer stores information in a attribute table
where each row represent a geometry/feature and each column represents a piece
of information about said geometry.

*Example of a attribute table for a populated places layer with two geometries and two columns*
|name|population|
|---|---|
|Cairo|9801536
|Asyut|501033

Expressions and variables are what elevate QGIS above other mapping software.
These tools allows us to do a ton of cool stuff through geoprocessing
algorithms, geometry generators, and styling settings. 


## Expressions

*If you want to follow along this part and use
the same data I'm using, you may find it
[here](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-populated-places/).
It is the populated places point layer from Natural Earth.*


[Expressions](https://docs.qgis.org/3.44/en/docs/user_manual/expressions/expression.html)
can be used in virtually every input field in QGIS. Input fields are every field
where you are asked to enter information about fonts, stroke weight, colors,
etc.

If you want to get started with expressions you need to familiarize yourself
with the expression builder. Navigate to any field you want to control with a
expression and click the 'Data defined override' icon always situated to the
right of the field, navigate down to the 'Expression > Edit...' button.

{{< image
    src="open-expression-builder.avif"
    caption="Click here to open the expression builder"
    alt="Guide to find the expression builder button. It is located under a menu to the right of the input field"
    class="img-centered"
>}}

A new window will pop up with a few sections in it. In the far left you will
find a text editor. This is the part where expressions are written.

Immediately to the right is a section filled with items and dropdown menus, this
is the function selector. Its use is entirely optional as its only purpose is to
list available functions, variables, and fields.

The white window to the far right shows some information about the currently
selected item in the function selector. Below the text editor there's a row of
commonly used operators. Beneth that is the 'Feature Preview' field. This field
shows the result of the current expression for a given feature, this is useful
as a sanity check while we're writting our expression. The preview is currently
blank as we have not written any expression yet, I've changed the feature to be
previewed to 'Cairo'.

 {{< image
    src="expression-builder.avif"
    caption="The expression builder"
    alt="The expression builder"
    class="img-centered"
>}}

Enter this line of code into the text field:

```
"POP_MAX"
```

We've just called for the `"POP_MAX"` value field. All this does is return the
value inside this field for every feature in the layer. The preview now says
`11893000`, since this is the population of Cairo according to this dataset. It
is important to keep in mind that every feature is evaluated on its own. If you
change the city to be previewed to Asyut the value will change to `420585`.

If we press 'ok' and close the expression builder now your view will likely
go blank with a single color. This is because you've just set the size of each
point in mm to equal its population, and twelve million is a very large number.
Lets instead make this our expression and click 'ok':

```
"POP_MAX" / 1000000
```

{{< image
    src="linear-resize.avif"
    caption="Place icons with linear sizes"
    alt="The expression builder"
    class="img-centered"
>}}

Now the place icon sizes have a more reasonable size, at least the places with
the largest of populations. Very small locations are rendered almost invisible.
This is because the difference in population between the largest places and the
smallest ones are so large and the size of the icons have a linear relationship
to the population number.

This is where expressions really shine because they allow us to calculate more
appropiate relations between the underlying data and the results we want. Try
replacing our previous expression with this one, also, feel free to switch
between some previewed values to see how the expression affects that feature:

```
(POP_MAX/10)^ 0.2
```

{{< image
    src="fractional-resize.avif"
    caption="Place icons with fractional power scaling"
    alt="Place icons with fractional power scaling"
    class="img-centered"
>}}

You may want to play around with the exponent to get the perfect results
depending on your data and map scale.

You can apply the same principle in virtually any field in QGIS. We can
make label sizes vary by population, we can make river width vary by size or
significance,


{{< image
    src="tapered-rivers.avif"
    caption="Rivers with widths based on river size"
    alt="Rivers with widths based on river size"
    class="img-centered"
>}}

## Variables

QGIS has two main types of variables, global and project. Global variables
store information about the current version, the current logged-in user, and
locale information. Project variables contain information that pertain to the
project, such as the projection, creation time, and the project unit (meters
usually meters or degrees.)

You can find information about both types of variables by navigatin to
'Project > Propertie (ctrl + shift + p) > Variables'. Global variables can not
be directly modified or appended, but you can write your own project variables.

This is useful for changing all the values you set in a project from a single
place instead of going into the symbology panel of each layer or menu everytime
you want to try a new look.

### Some project variables I like to set
* `stroke-weight`: A float representing the stroke weight I use on rivers,
coasts, roads and everything I want to have the same stroke weight. You can also
use multiple variables to define several different stroke weights (thin, normal,
bold).
* `serif` and `sans-serif`: Strings containing the names of the primary fonts
of the project.

This is how you set a value of any field to a project variable:

{{< image
    src="setting-variables.avif"
    caption="Setting the value of a field to a variable"
    alt="Setting the value of a field to a variabe: 'Data override > Variable > your-variable'"
    class="img-centered"
>}}

If you now inspect the expression editor you'll see that it has been set to
`@serif`, `@` creates a link to the variable name.

### Color variables

While you can use set the value of project variables to color hex values
and use them in color fields, there is a much simpler solution. In the same
'Project Properties' we created our variables in theres a separate tab
named 'Colors'. Here you can create named colors unique to your project with
the same useful features of project variables.

These are however assigned in a slightly different place than project variables.
Create and label your color, then navigate to a color fied and press the
small arrow in the right of the color preview, you'll find your color under
the 'Project Colors' header. As with normal variables, edits to these color
variables will effect all fields that have been linked to that variable.
