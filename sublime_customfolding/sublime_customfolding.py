# sublime_customfolding.py
# A simple plugin for folding arbitrarily defined sections of code
# in Sublime Text.
#
# Author: Ray Russell Reese III <russ@zerotech.net>
#         diametric@freenode
#
#

import sublime, sublime_plugin

# Assuming pos begins after an open tag, find the proper closing tag.
def find_matching_fold(view, tagopen, tagclose, pos, nest = 0):
	# Look for the next open and close tags that aren't in a string. 
	opos, cpos = pos, pos
	while True:
		nextopen = view.find(tagopen, opos, sublime.LITERAL)
		if view.score_selector(nextopen.a, "string") == 0:
			break
		else:
			opos = nextopen.b

	while True:
		nextclose = view.find(tagclose, cpos, sublime.LITERAL)
		if view.score_selector(nextclose.a, "string") == 0:
			break
		else:
			cpos = nextclose.b

	# No more matching close tags, just fold it all up.
	if nextclose.empty():
		return sublime.Region(view.size(), view.size())

	# Found another open tag before we found the matching close tag
	if not nextopen.empty() and nextopen.b < nextclose.b:
		nest = nest + 1
		return find_matching_fold(view, tagopen, tagclose, nextopen.b, nest)
	# Found a close tag
	else:
		# Unroll it
		if nest > 0:
			nest = nest - 1
			return find_matching_fold(view, tagopen, tagclose, nextclose.b, nest)
		# Match
		else:
			return nextclose

def find_nearest_open(view):
	pass


# Fold everything below the supplied position. 
def fold_tag_below(view, opentag, closetag, pos):
	p = pos
	while True:
		firstopen = view.find(opentag, p, sublime.LITERAL)

		# No folding, just return.
		if firstopen.empty():
			return

		p = firstopen.b

		# Ignore fold markers inside of strings. 
		if view.score_selector(firstopen.a, "string") > 0:
			continue

		firstclose = find_matching_fold(view, opentag, closetag, firstopen.b)
		foldregion = sublime.Region(view.line(firstopen).b, view.line(firstclose).b)

		view.fold(foldregion)


# Fold the current region where the cursor is.
def fold_below(view):
	cur = view.sel()[0].begin()
	for tags in view.settings().get("customfolding_tags"):
		fold_tag_below(view, tags[0], tags[1], cur)


# Folds all the configured tags (not including onload tags)
def fold_ALL_the_things(view):
	for tags in view.settings().get("customfolding_tags", []):
		if tags[0] != "" and tags[1] != "":
			fold_tag_below(view, tags[0], tags[1], 0)

# Fold everything command. 
class CustomfoldingFoldAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		fold_ALL_the_things(self.view)

class CustomfoldingFoldBelowCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		fold_below(self.view)

# Handles folding tags on file load
class CustomfoldingEventListener(sublime_plugin.EventListener):
	def on_load(self, view):
		if view.settings().get("customfolding_onload_all", False):
			for tags in view.settings().get("customfolding_onload_tags", []):
				if tags[0] != "" and tags[1] != "":
					fold_tag_below(view, tags[0], tags[1], 0)

		defaultFolds = view.settings().get("customfolding_onload_tags", [])

		if len(view.settings().get("customfolding_onload_tags", [])) > 0:
			fold_ALL_the_things(view)



### Test Area
### ----------------------------------------------------------------------------

### VERY_LONG_AND_ANNOYING_FOLD_TAG_START

## Some unrelated content.

# {{{ fold 1

# {{{ fold 1.1

# {{{ fold 1.1.1
	
asdfasdfadfadfadfadsf


# }}} endfold 1.1.1

# }}} endfold 1.1

# }}} endfold 1

# {{{ fold 2

# }}} endfold 2

# }}}

### VERY_LONG_AND_ANNOYING_FOLD_TAG_END
