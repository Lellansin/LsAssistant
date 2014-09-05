@echo off && setlocal enabledelayedexpansion

for /f %%i in (%~dp0bbc.txt) do ( 
	set "args=!args!%%i "
)
!args!