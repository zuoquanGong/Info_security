@echo %date:~0,4%年%date:~5,2%月%date:~8,2%日%time:~0,8%
@echo **********************
@echo;
@Debug\caesar.exe %1 1 
@echo;
@echo **********************
@echo;
@Debug\caesar.exe %1 0 out.txt recover.txt
@echo;
@echo **********************
@echo;
@echo 原文存于clrtext.txt，密文存于out.txt，解码后的文本存于recover.txt