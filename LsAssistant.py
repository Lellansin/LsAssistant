import sublime, sublime_plugin
import os, urllib2
import json
import thread, time


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


class LsAssistant(sublime_plugin.WindowCommand):
	def run(self):
		# sublime.status_message("string")
		# self.view.set_status('mode', 'hello world')
		self.window.run_command("hide_panel", {"cancel": "true"})
		# self.window.run_command("show_panel", {"panel": "console", "toggle": "true"})
		# sublime.log_input(1)
		# sublime.message_dialog("Lellansin's assistant")
		# self.view.insert(edit, 0, "Hello, World!")


def getFile(name):
	github = 'https://github.com/Lellansin/LsAssistant/raw/master/'
	print("Downloading " + github + name)
	content = urllib2.urlopen(github + name.replace(' ', '%20')).read()
	return content

class LsUpdate(sublime_plugin.WindowCommand):
	def run(self):
		print('\n\n\n\n\n\n\n\n\n\n')
		self.window.run_command("show_panel", {"panel": "console"})
		sublime.message_dialog("update thread has created, it make take 30 sec.")
		thread.start_new(update, ())

def update():
	packages_path = sublime.packages_path() + '\\LsAssistant\\';
	os.makedirs(packages_path) if not os.path.exists(packages_path) else None;
	string = getFile("Version.json")
	content = json.loads(string);
	# length = len(content['files'])
	for files in content['files']:
		print("File name : " + files)
		content = getFile(files)
		open(os.path.join(packages_path, files), 'wb').write(content)
		print("Complete!")
	sublime.message_dialog("Update ok!")
	# sublime.active_window().run_command("hide_panel", {"cancel": "true"})
	# sublime.message_dialog(str(content['version']));
		

# class EventListener(sublime_plugin.EventListener):
    # def on_load(self, view):
        # sublime.message_dialog("it's on_load!")
