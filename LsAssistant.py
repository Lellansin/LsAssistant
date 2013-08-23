import sublime, sublime_plugin
import os, urllib2
import json

import thread
import time


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
	print("Downloading " + github + name)
	content = urllib2.urlopen(github + name.replace(' ', '%20')).read()
	return content

class LsUpdate(sublime_plugin.WindowCommand):
	def run(self):
		# sublime.set_timeout(update, 100)
		thread.start_new(update, ())
		sublime.message_dialog("update thread has created, if it shows err : 'Error trying to parse file', it's just ok!")

def update():
	#packages_path = 'c:\\python\\test';
	packages_path = sublime.packages_path() + '\\LsAssistant\\test';
	os.makedirs(packages_path) if not os.path.exists(packages_path) else None;
	string = getFile("Version.json")
	content = json.loads(string);
	length = len(content['files'])
	# print "length is " + str(length)
	for files in content['files']:
		print("downloading : " + files)
		open(os.path.join(packages_path, files), 'wb').write(getFile(files))
		print("complete!")
	sublime.message_dialog("update ok!")
	# print type(content)
	# print content
	# sublime.message_dialog(str(content['version']));
	#open(os.path.join(packages_path, obj["files"][0]), 'w').write(content)
		

# class EventListener(sublime_plugin.EventListener):
    # def on_load(self, view):
        # sublime.message_dialog("it's on_load!")
