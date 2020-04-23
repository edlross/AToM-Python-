# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['atomTech.py'],
             pathex=['/Users/edward.ross/Documents/Documents - Edward’s MacBook Pro/GitHub/491/atomTech/appWithPort'],
             binaries=[],
             datas=[],
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
          name='atomTech',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='atomTech')
app = BUNDLE(coll,
             name='atomTech.app',
             icon=None,
             bundle_identifier=None)
