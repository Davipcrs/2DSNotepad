pip install -r requirements.txt
pip install pyinstaller
pyinstaller -w --distpath ./dist/linux main.py --add-data './style/dark/darktheme.qss:themes' --add-data './LICENSE:license'

#-w windowned
#--add-data local to themes (relative or full paths)
