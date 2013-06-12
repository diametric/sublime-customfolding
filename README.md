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

To define the tags to fold on.

`"customfolding_tags": [ ["tag1open", "tag1close"], ["tag2open", "tag2close"], ... ]`

To define the tags to fold on file open.  These can be a subset, or independent
of the defined defined customfolding_tags setting.  If these are independent 
they will only be folded on file open, you will be unable to fold them later.

`"customfolding_onload_tags": [ ["tag1open", "tag1close"], ["tag2open", "tag2close"], ... ]`

Alternatively, you can set this to True in order to fold all your defined flags. 

`"customfolding_onload_all": True`
