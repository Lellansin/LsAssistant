@echo off
gcc -v && ( 
	color 2f && echo -----------------------  && echo  version test success! && echo -----------------------
) || (
	color 4f && echo ------------------------ && echo  version test failed!  && echo ------------------------
)