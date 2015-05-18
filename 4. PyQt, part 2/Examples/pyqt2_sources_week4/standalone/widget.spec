# -*- mode: python -*-
import os
name = 'widget.exe'
a = Analysis(['widget.py'],
             pathex=[os.path.dirname(__file__)],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)

a.binaries += [('imageformats/qjpeg4.dll',
                       'C:/Python27/Lib/site-packages/PySide/plugins/imageformats/qjpeg4.dll', 
                       'BINARY')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=name,
          debug=False,
          strip=None,
          upx=True,
          icon='icon.ico')
