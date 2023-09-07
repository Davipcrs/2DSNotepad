pip install -r requirements.txt
pip install pyinstaller
pyinstaller -w --distpath ./dist/windows main.py --add-data './style/dark/darktheme.qss;themes' --add-data './LICENSE;license'