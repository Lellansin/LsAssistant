@echo off

if not exist "%1\bin\gcc.exe" goto epicfail1
if not exist "%~dp0set_distro_paths.bat" goto epicfail2
cmd /k ""%~dp0set_distro_paths.bat" %1 && title LsAssistant"
goto :eof

:epicfail1
chcp 936
set X_ERR1=ERROR: 啊哦，出状况了：
set X_ERR2=       1. %1/bin/gcc.exe 文件未找到, 请确保您设置的 compiler_path 是正确的。请到 Tools - 编程助手 -【功能】默认设置，中设置编译器目录 (compiler_path)，如果要关闭只需修改 file_ext 即可
set X_ERR3=       2. 请不要移动 LsAssistant 插件目录下 的 bat 文件 %~nx0
cmd /t:4f /k "echo %X_ERR1% && echo %X_ERR2% && echo %X_ERR3% && title ERROR"
goto :eof

:epicfail2
chcp 936
set X_ERR1=ERROR: LsAssistant插件下的 bat 文件 set_distro_paths.bat 丢失.
set X_ERR2=       请不要移动或删除该文件。丢失可到 Lellansin 的 Github 上重新下载
cmd /t:4f /k "echo %X_ERR1% && echo %X_ERR2% && title ERROR"
goto :eof
