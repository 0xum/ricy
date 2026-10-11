#!/usr/bin/env python3
"""Initialize only Dolphin with local Qt helper and visual sheet."""
from pathlib import Path
import os,sys
root=Path.home()/'.local/share/ricy-dolphin'
old=os.environ.get('QT_PLUGIN_PATH','')
os.environ['QT_PLUGIN_PATH']=str(root/'plugins')+(os.pathsep+old if old else '')
arguments = sys.argv[1:]
# GUI launches must not reuse an older process with an older mapped helper.
# Keep the FileManager1 daemon route and explicit window requests intact.
if '--daemon' not in arguments and '--new-window' not in arguments:
    arguments = ['--new-window', *arguments]
os.execv('/usr/bin/dolphin',['dolphin','-plugin','ricydolphinui','-stylesheet',str(root/'dolphin.qss'),*arguments])
