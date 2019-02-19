# -*- mode: python -*-
# -*- coding: utf-8 -*-

block_cipher = None


a = Analysis(['.\\ScaffGen.py'],
             pathex=['dist\\win\\spec'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ScaffGen',
          debug=False,
          strip=False,
          upx=True,
          console=True, 
          icon='D:\\Repos\\ScaffGen\\Icons\\scaff64.ico' )
