@echo off

if not exist "%1\bin\gcc.exe" goto epicfail1
if not exist "%~dp0set_distro_paths.bat" goto epicfail2
cmd /k ""%~dp0set_distro_paths.bat" %1 && title LsAssistant"
goto :eof

:epicfail1
chcp 936
set X_ERR1=ERROR: ��Ŷ����״���ˣ�
set X_ERR2=       1. %1/bin/gcc.exe �ļ�δ�ҵ�, ��ȷ�������õ� compiler_path ����ȷ�ġ��뵽 Tools - ������� -�����ܡ�Ĭ�����ã������ñ�����Ŀ¼ (compiler_path)�����Ҫ�ر�ֻ���޸� file_ext ����
set X_ERR3=       2. �벻Ҫ�ƶ� LsAssistant ���Ŀ¼�� �� bat �ļ� %~nx0
cmd /t:4f /k "echo %X_ERR1% && echo %X_ERR2% && echo %X_ERR3% && title ERROR"
goto :eof

:epicfail2
chcp 936
set X_ERR1=ERROR: LsAssistant����µ� bat �ļ� set_distro_paths.bat ��ʧ.
set X_ERR2=       �벻Ҫ�ƶ���ɾ�����ļ�����ʧ�ɵ� Lellansin �� Github ����������
cmd /t:4f /k "echo %X_ERR1% && echo %X_ERR2% && title ERROR"
goto :eof
