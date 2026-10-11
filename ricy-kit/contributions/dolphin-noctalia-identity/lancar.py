#!/usr/bin/env python3
"""Inicializa somente Dolphin com o helper Qt local e a folha visual."""
from pathlib import Path
import os,sys
root=Path.home()/'.local/share/ricy-dolphin'
old=os.environ.get('QT_PLUGIN_PATH','')
os.environ['QT_PLUGIN_PATH']=str(root/'plugins')+(os.pathsep+old if old else '')
os.execv('/usr/bin/dolphin',['dolphin','-plugin','ricydolphinui','-stylesheet',str(root/'dolphin.qss'),*sys.argv[1:]])
