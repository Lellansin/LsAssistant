import sublime
import sublime_plugin
import os
import os.path
from shutil import copy


class LsOpenCmdCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):
        cwd = os.getcwd()
        path = self.view.file_name()
        platform = sublime.platform()
        exec_type = args.get('type')

        if exec_type == 'test_gcc_version':
            path = 'C:\\'

        if not path:
            echo("没有办法打开当前路径的控制台, 请先确保你的文件已保存!")
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

    if compiler_path and checkFileType(run_file, ext):
        command += compiler_path + ' '
        if not exec_type:
            if settings.get('auto_compile_run') == 'default':
                print('prepare auto run')
                autoRun(
                    getAutoRunPath(bat_dir, 'run_gcc_auto.bat') + '\n' + run_file)
        elif (exec_type == 'test_gcc_version'):
            print('prepare auto run')
            autoRun(getAutoRunPath(bat_dir, 'test_gcc_version.bat'))
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
    auto_bat = bat_dir + '\\' + bat_name
    auto_bat_tmp = tmp_dir + '\\' + bat_name

    if not os.path.exists(auto_bat_tmp):
        copy(auto_bat, tmp_dir)
    return auto_bat_tmp


def checkFileType(path, ext):
    return (ext == path[path.rfind('.'):])


def autoRun(command):
    tmp_dir = os.getenv('temp')
    fp = open(tmp_dir + '/auto.txt', 'w')
    print('auto command:' + command)
    fp.write(command);
    fp.close()
