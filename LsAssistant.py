import sublime, sublime_plugin
import os;

class OpenCmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		cwd = os.getcwd();
		path = self.view.file_name();
		platform = sublime.platform();

		if path is None:
			sublime.message_dialog("There is no path to open, please save the file first!");		
		
		if(platform == 'windows'):
			settings = sublime.load_settings('LsAssistant.sublime-settings')
			compiler_path = settings.get('gcc_path')
			# get file directory
			path = path[0:path.rfind('\\')];
			# cd directory and start a cmd
			command = path[0:2] + ' && ' + 'cd "' + path + '" && start ' + compiler_path + ' '
			# sublime.message_dialog(command)
			os.system(command)
		elif(platform == 'linux'):
			# get file directory
			path = path[0:path.rfind('/')];
			# cd directory and start a terminal
			command = 'cd ' + path + ' && gnome-terminal'
			os.system(command)
		else:
			sublime.error_message('Sorry, this plugin doestn\'t support your system now. :(')

class LsAssistant(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.message_dialog("Lellansin's assistant")
		# self.view.insert(edit, 0, "Hello, World!")

# class EventListener(sublime_plugin.EventListener):
    # def on_load(self, view):
        # sublime.message_dialog("it's on_load!")
