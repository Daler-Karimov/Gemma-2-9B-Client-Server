@echo off
echo Running ...

cd /d "%~dp0"

start /B python app.py

echo It is worked, dont touch any fucking button!
pause > nul

taskkill /F /IM python.exe /T

echo Turn off.