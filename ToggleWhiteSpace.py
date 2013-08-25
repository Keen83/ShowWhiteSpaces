import sublime, sublime_plugin

class ToggleWhiteSpaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.settings().get("draw_white_space") != "all":
			print "Switch to All"
			self.view.settings().set("draw_white_space", "all")
		else :
			print "Switch to Selection"
			self.view.settings().set("draw_white_space", "selection")
