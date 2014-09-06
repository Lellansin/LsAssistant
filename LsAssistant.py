import sublime, sublime_plugin
import os, os.path
from shutil import copy

TEMP_AUTO_RUN_BAT_NAME = 'LsAuto.bat'
TEST_GCC_VERSION_PATH  = 'test_gcc_version.bat'
RUN_GCC_AUTO = 'run_gcc_auto.bat'
GCC_INIT_BAT = 'open_distro_window.bat'

class LsOpenCmdCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):
        cwd = os.getcwd()
        path = self.view.file_name()
        platform = sublime.platform()
        exec_type = args.get('type')
        auto_flag = args.get('auto_run')

        if exec_type == 'test_gcc_version':
            path = 'C:\\'

        if not path:
            echo("无法打开当前路径的控制台, 请先确保你的文件已保存")
            return

        # path = getChineseCFile(path);

        if(platform == 'windows'):
            compiler_exec = getCompilerExec(exec_type, path, auto_flag)
            path = getCurPath(path, platform)
            command = path[0:2] + ' && ' + 'cd "' + \
                path + '" && start "" ' + compiler_exec + ' '
            print(command)
            os.system(command)
        elif(platform == 'linux'):
            path = getCurPath(path, platform)
            command = 'cd ' + path + ' && gnome-terminal'
            os.system(command)
        else:
            echo('Sorry, 目前插件不支持你的系统 Orz')

class LsAssistant(sublime_plugin.WindowCommand):

    def run(self, **args):
        pass
        # sublime.status_message("string")
        # self.view.set_status('mode', 'hello world')
        # self.window.run_command("hide_panel", {"cancel": "true"})
        # self.window.run_command("show_panel", {"panel": "console", "toggle": "true"})
        # sublime.log_input(1)

def echo(str):
    sublime.message_dialog('冰森编程助手:\n' + str)

def getCompilerExec(exec_type, run_file, auto_flag):
    bat_dir = os.path.dirname(__file__) + '\\bat'
    open_bat = '"' + bat_dir + '\\' + GCC_INIT_BAT + '"'
    command = open_bat + ' '

    settings = sublime.load_settings('LsAssistant.sublime-settings')
    compiler_path = settings.get('compiler_path')
    ext = settings.get('file_ext')
    auto_switch = settings.get('auto_compile_run')
    command += compiler_path + ' '

    if (exec_type == 'test_gcc_version'):
        print('prepare run test')
        tempRun(TEMP_AUTO_RUN_BAT_NAME, getAutoRunPath(bat_dir, TEST_GCC_VERSION_PATH))
        return command

    if compiler_path and checkFileType(run_file, ext):
        print('auto_flag', auto_flag)
        if not exec_type and auto_flag and auto_switch:
            custom_run = settings.get('custom_run')
            bat_to_run = custom_run
            if not bat_to_run:
                custom_run = getAutoRunPath(bat_dir, RUN_GCC_AUTO)
            print('prepare auto run')
            tempRun(TEMP_AUTO_RUN_BAT_NAME, custom_run + ' ' + run_file)
        else:
            tempRun(TEMP_AUTO_RUN_BAT_NAME, '')
        return command
    else:
        return 'cmd'

def getCurPath(path, platform):
    if(platform == 'windows'):
        return path[0:path.rfind('\\') + 1]
    elif(platform == 'linux'):
        return path[0:path.rfind('/')]

def getAutoRunPath(bat_dir, bat_name):
    tmp_dir = os.getenv('temp')
    auto_bat = '"' + bat_dir + '\\' + bat_name + '"'
    return auto_bat

def checkFileType(path, ext):
    end = path[path.rfind('.'):]
    return (ext == end or (ext + 'tmp') == end)

def tempRun(file_name, command):
    tmp_dir = os.getenv('temp')
    fp = open(tmp_dir + '/' + file_name, 'w')
    print('auto command:' + command)
    fp.write('@echo off\n');
    fp.write(command);
    fp.close()

def getChineseCFile(path):
    settings = sublime.load_settings('LsAssistant.sublime-settings')
    ext = settings.get('file_ext')
    encoding = settings.get('file_encoding')
    if encoding == 'utf8':
        return path
    if not checkFileType(path, ext):
        return path
    text = open(path).read()
    tmp_file = path[:path.rfind('.')] + ".tmp" + path[path.rfind('.'):]
    f = open(tmp_file, 'w')
    print('----------------------------------')
    print(text.encode('utf8'))
    print('----------------------------------')
    s = text.encode('utf8').decode(encoding)
    f.write(s)
    f.close()
    return tmp_file

# todo 生成一个 gbk 缓存文件，编译这个缓存文件