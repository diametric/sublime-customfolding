# Sublime Text Custom Folding Plugin

This plugin allows you to define arbitrary folding start and end tags.

A simple plugin for defining artbitrary tags for folding.

#### Configuration

To define the tags to fold on.

`"customfolding_tags": [ 
   ["tag1open", "tag1close"],
   ["tag2open", "tag2close"],
   ...

]`

To define the tags to fold on file open.  These can be a subset, or independent
of the defined defined customfolding_tags setting.  If these are independent 
they will only be folded on file open, you will be unable to fold them later.

`"customfolding_onload_tags": [
   ["tag1open", "tag1close"],
   ["tag2open", "tag2close"],
   ...

]