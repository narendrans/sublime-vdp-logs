import sublime, sublime_plugin, re


class VdpLogDateTimeTransformCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		reg = sublime.Region(0, self.view.size())
		text = self.view.substr(reg)
		self.view.replace(edit, reg, transformTimeStamp(text))
		self.view.set_status("DateTimeTransform", "Date time transformations applied.")
# 2015-10-19 16:10:12.194
# 2015-10-21 14:09:25 995

def transformTimeStamp(data):
	data = re.sub(r'(2015)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d\d)', r'\1-\2-\3 \4:\5:\6.\7', data)  
	return data