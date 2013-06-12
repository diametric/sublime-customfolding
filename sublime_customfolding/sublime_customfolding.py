# sublime_customfolding.py
# A simple plugin for folding arbitrarily defined sections of code
# in Sublime Text.
#
# Author: Ray Russell Reese III <russ@zerotech.net>
#         diametric@freenode
#
#

## Here's some fun testing area.

# {{{ fold 1

# {{{ fold 1.1

# {{{ fold 1.1.1
	
# }}} endfold 1.1.1

# }}} endfold 1.1

# }}} endfold 1

# {{{ fold 2

# }}} endfold 2

import sublime, sublime_plugin

def find_matching_fold(view, tagopen, tagclose, pos, nest = 0):
	while True:
		nextopen = view.find(tagopen, pos, sublime.LITERAL)
		if view.score_selector(nextopen.a, "string") == 0:
			break
		else:
			pos = nextopen.b

	while True:
		nextclose = view.find(tagclose, pos, sublime.LITERAL)
		if view.score_selector(nextclose.a, "string") == 0:
			break
		else:
			pos = nextclose.b

	# No more matching close tags, just fold it all up.
	if nextclose.empty():
		return sublime.Region(view.size(), view.size())

	if not nextopen.empty() and nextopen.b < nextclose.b:
		nest = nest + 1
		return find_matching_fold(view, tagopen, tagclose, nextopen.b, nest)
	else:
		if nest > 0:
			nest = nest - 1
			return find_matching_fold(view, tagopen, tagclose, nextclose.b, nest)
		else:
			return nextclose

def fold_ALL_the_things(view):
	p = 0
	while True:
		firstopen = view.find("{{{", p, sublime.LITERAL)

		# No folding, just return.
		if firstopen.empty():
			return

		p = firstopen.b

		# Ignore fold markers inside of strings. 
		if view.score_selector(firstopen.a, "string") > 0:
			print("Skipping over string fold")
			continue

		firstclose = find_matching_fold(view, "{{{", "}}}", firstopen.b)
		foldregion = sublime.Region(firstopen.b, firstclose.a)

		print("Folding region %s" % foldregion)

		view.fold(foldregion)




