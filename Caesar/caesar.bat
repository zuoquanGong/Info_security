@echo %date:~0,4%��%date:~5,2%��%date:~8,2%��%time:~0,8%
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
@echo ԭ�Ĵ���clrtext.txt�����Ĵ���out.txt���������ı�����recover.txt