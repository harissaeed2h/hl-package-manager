import readline

def autocomplete(allOptions):
	def completer(text, state):
		viableOptions = [option for option in allOptions if option.startswith(text)]
		if state < len(viableOptions):
			return viableOptions[state]
		else:
			return None
	readline.parse_and_bind("tab: complete")
	readline.set_completer(completer)