# Sublime Text Custom Folding Plugin

This plugin allows you to define arbitrary folding start and end tags. Just drop the sublime_customfolding directory
into your Packages directory. 

### Caveats 

Sublime Text's built in folding mechanism works off of indentation.  By default, indendtations will cause a region to
be defined, as well as adding special folding mechanisms to the UI such as a arrow to collapse the fold, and a vertical
line to define the fold region.   Unfortunately, these mechanisms are not exposed in the plugin API and therefore any
folding plugins, including this one, are unable to create the UI elements to collapse a fold. 

However, arbitrary folds can be defined, and collapsed on hotkey/menu selection which will result in the proper UI
elements being rendered to expand a fold. 

### Configuration

<<<<<<< HEAD
=======
To define the tags to fold on.

>>>>>>> 8e1b87448624a138f2ef7b6a04738e0e9f1a790d
`"customfolding_tags": [ ["tag1open", "tag1close"], ["tag2open", "tag2close"], ... ]`

To define the tags to fold on file open.  These can be a subset, or independent
of the defined defined customfolding_tags setting.  If these are independent 
they will only be folded on file open, you will be unable to fold them later.

<<<<<<< HEAD
`"customfolding_onload_tags": [ ["tag1open", "tag1close"], ["tag2open", "tag2close"], ... ]`
=======
`"customfolding_onload_tags": [ ["tag1open", "tag1close"], ["tag2open", "tag2close"], ... ]`

Alternatively, you can set this to true in order to fold all your defined flags. 

`"customfolding_onload_all": true`

### Examples

Before Folding:

![Before Fold](http://antidiametric.com/customfolding/customfold-before.png)

After Folding:

![After Fold](http://antidiametric.com/customfolding/customfold-after.png)
>>>>>>> 8e1b87448624a138f2ef7b6a04738e0e9f1a790d
