a=InputBox("ÇëÊäÈëÃÜÔ¿")
dim objShell
set objShell=wscript.createObject("wscript.shell")
objShell.run "caesar.bat "+a+" > temp.txt",0

Set fso  = CreateObject("Scripting.FileSystemObject")
Set file = fso.OpenTextFile("temp.txt", 1)
text = file.ReadAll
file.Close
MsgBox text,0,"result"