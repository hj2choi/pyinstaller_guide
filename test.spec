# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['project/test.py'],
             pathex=['./'],
             binaries=[],
             datas=[("./project/Inner/child_dir_text.txt","./Inner")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='test',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='test')

import shutil
shutil.copyfile("./parent_dir_text.txt", "{0}/parent_dir_text.txt".format(DISTPATH))
