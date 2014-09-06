@echo off

if not exist "%1\bin\gcc.exe" goto epicfail
if "%X_DISTRO%" == "nuwen" goto :eof
set X_DISTRO=nuwen
if exist "%1\git\cmd\git.exe" set PATH=%1\git\cmd;%PATH%
set PATH=%1\bin;%PATH%
cls
cmd /c "%temp%\LsAuto.bat"
goto :eof

:epicfail
color 4f
echo ERROR: You must run %~nx0 from the root of the LsAssistant\bat.
echo        Don't copy or move this batch file.
title ERROR
goto :eof