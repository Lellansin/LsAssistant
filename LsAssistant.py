import sublime, sublime_plugin
import os, urllib2;


class LsOpenCmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		cwd = os.getcwd();
		path = self.view.file_name();
		platform = sublime.platform();

		if path is None:
			sublime.message_dialog("There is no path to open, please save the file first!");		
		
		if(platform == 'windows'):
			settings = sublime.load_settings('LsAssistant.sublime-settings')
			compiler_path = settings.get('compiler_path')
			path = path[0:path.rfind('\\')];
			command = path[0:2] + ' && ' + 'cd "' + path + '" && start ' + compiler_path + ' '
			os.system(command)
		elif(platform == 'linux'):
			path = path[0:path.rfind('/')];
			command = 'cd ' + path + ' && gnome-terminal'
			os.system(command)
		else:
			sublime.error_message('Sorry, this plugin doestn\'t support your system now. :(')


class LsAssistant(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.message_dialog("Lellansin's assistant")
		# self.view.insert(edit, 0, "Hello, World!")

def getFile(name):
	github = 'https://github.com/Lellansin/LsAssistant/raw/master/'
	content = urllib2.urlopen(github + name.replace(' ', '%20')).read()
	sublime.message_dialog(content)
	return content

class LsUpdate(sublime_plugin.WindowCommand):
	def run(self):
		getFile("Version.json")
		# pf='Package Control.sublime-package';
		
		# packages_path = sublime.packages_path() + '\\LsAssistant\\';
		# obj = { 
		# 	"version" : 0.1,
		# 	"files"  : ["Default (Linux).sublime-keymap","Default (OSX).sublime-keymap","Default (Windows).sublime-keymap","LsAssistant.py","LsAssistant.pyc","LsAssistant.sublime-settings","Main.sublime-menu"],
		# }
		# 
		# txt = eval(content)
		# # open(os.path.join(packages_path, obj["files"][0]), 'w').write(content)
		# print txt
#		sublime.message_dialog(getFile("Version.json"))
		

# class EventListener(sublime_plugin.EventListener):
    # def on_load(self, view):
        # sublime.message_dialog("it's on_load!")
