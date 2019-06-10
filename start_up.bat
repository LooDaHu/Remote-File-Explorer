@echo off
set root=%~dp0
set venvdir=venv\Scripts
cd /d %root%%venvdir%
call activate.bat
cd %root%
python app.py





