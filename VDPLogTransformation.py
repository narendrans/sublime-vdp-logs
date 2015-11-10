# Sublime plugin. Last edited by Naren 2015-11-10

import sublime, sublime_plugin, re

class VdpLogDateTimeTransformCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		reg = sublime.Region(0, self.view.size())
		text = self.view.substr(reg)
		self.view.replace(edit, reg, transformTimeStamp(text))
		self.view.set_status("DateTimeTransform", "Date time transformations applied.")
		self.view.set_syntax_file('VDPLog.tmLanguage')

def transformTimeStamp(data):
	data = re.sub(r'(2015)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d\d)', r'\1-\2-\3 \4:\5:\6.\7', data)  
	return data
