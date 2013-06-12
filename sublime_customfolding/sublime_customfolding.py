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

# Finds the first open tag starting at the beginning of the view, and then
# recursively closes every custom fold region.

def fold_tag_all(view, opentag, closetag):
	p = 0
	while True:
		firstopen = view.find(opentag, p, sublime.LITERAL)

		# No folding, just return.
		if firstopen.empty():
			return

		p = firstopen.b

		# Ignore fold markers inside of strings. 
		if view.score_selector(firstopen.a, "string") > 0:
			print("Skipping over string fold")
			continue

		firstclose = find_matching_fold(view, opentag, closetag, firstopen.b)
		foldregion = sublime.Region(firstopen.b, firstclose.a)

		print("Folding region %s" % foldregion)

		view.fold(foldregion)


def fold_ALL_the_things(view):
	for tags in view.settings().get("customfolding_onload_tags", []):
		fold_tag_all(view, tags[0], tags[1])

# Handles folding tags on file load
class CustomfoldingEventListener(sublime_plugin.EventListener):
	def on_load(self, view):
		if view.settings().get("customfolding_onload_all", False):
			fold_ALL_the_things(view)

		defaultFolds = view.settings().get("customfolding_onload_tags", [])


		if len(view.settings().get("customfolding_onload_tags", [])) > 0:
			fold_ALL_the_things(view)


### Test Area

### VERY_LONG_AND_ANNOYING_FOLD_TAG_START

## Some unrelated content.

# {{{ fold 1

# {{{ fold 1.1

# {{{ fold 1.1.1
	
# }}} endfold 1.1.1

# }}} endfold 1.1

# }}} endfold 1

# {{{ fold 2

# }}} endfold 2

# }}}

### VERY_LONG_AND_ANNOYING_FOLD_TAG_END
