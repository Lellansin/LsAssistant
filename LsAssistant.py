import sublime, sublime_plugin
import os, os.path
from shutil import copy

TEMP_AUTO_RUN_BAT_NAME = 'LsAuto.bat'
TEST_GCC_VERSION_PATH  = 'test_gcc_version.bat'
RUN_GCC_AUTO = 'run_gcc_auto.bat'

class LsOpenCmdCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):
        cwd = os.getcwd()
        path = self.view.file_name()
        platform = sublime.platform()
        exec_type = args.get('type')

        if exec_type == 'test_gcc_version':
            path = 'C:\\'

        if not path:
            echo("没有办法打开当前路径的控制台, 请先确保你的文件已保存")
            return

        if(platform == 'windows'):
            compiler_exec = getCompilerExec(exec_type, path)
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


def getCompilerExec(exec_type, run_file):
    bat_dir = os.path.dirname(__file__) + '\\bat'
    open_bat = '"' + bat_dir + '\\open_distro_window.bat' + '"'

    settings = sublime.load_settings('LsAssistant.sublime-settings')
    compiler_path = settings.get('compiler_path')
    ext = settings.get('file_ext')

    command = open_bat + ' '

    if compiler_path:
        command += compiler_path + ' '
        if not exec_type and checkFileType(run_file, ext):
            if settings.get('auto_compile_run') == 'true':
                custom_run = settings.get('custom_run')
                bat_to_run = custom_run
                if not bat_to_run:
                    custom_run = getAutoRunPath(bat_dir, RUN_GCC_AUTO)
                print('prepare auto run')
                autoRun(custom_run + ' ' + run_file)
            else:
                autoRun('')
        elif (exec_type == 'test_gcc_version'):
            print('prepare auto run')
            autoRun(getAutoRunPath(bat_dir, TEST_GCC_VERSION_PATH))
        else:
            autoRun('')
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
    return (ext == path[path.rfind('.'):])


def autoRun(command):
    tmp_dir = os.getenv('temp')
    fp = open(tmp_dir + '/' + TEMP_AUTO_RUN_BAT_NAME, 'w')
    print('auto command:' + command)
    fp.write('@echo off\n');
    fp.write(command);
    fp.close()
