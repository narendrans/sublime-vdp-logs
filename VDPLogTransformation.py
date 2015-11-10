# Sublime plugin. Last edited by Naren 2015-11-10

import sublime, sublime_plugin, re, webbrowser, http.server, socketserver

# Applies regular expression transformation
class VdpLogDateTimeTransformCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		reg = sublime.Region(0, self.view.size())
		text = self.view.substr(reg)
		self.view.replace(edit, reg, transformTimeStamp(text))
		self.view.set_status("DateTimeTransform", "Date time transformations applied.")

# Searches a selected text on search.denodo.com
class searchDenodoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		x = ""
		for region in view.sel():
			x+=view.substr(region)
		webbrowser.open_new_tab("https://search.denodo.com/results?filter=" + x)

# Searches a selected text on Google
class searchGoogleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		x = ""
		for region in view.sel():
			x+=view.substr(region)
		webbrowser.open_new_tab("https://encrypted.google.com/search?q=" + x)

# TODO: Serve a file over http. Useful for quickly sharing a file (especially log) over LAN.
# 		Change the way it's done as a sublime text bug makes sublime unresponsive.
class serverCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		Handler = http.server.SimpleHTTPRequestHandler
		httpd = socketserver.TCPServer(("", 88), Handler)
		print("serving at port", 88)
		httpd.serve_forever()

# Edit the second parameter of re.sub as per your needs
def transformTimeStamp(data):
	data = re.sub(r'(2015)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d\d)', r'\1-\2-\3 \4:\5:\6.\7', data)  
	return data
