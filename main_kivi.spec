from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main_kivi.py'],
             pathex=['D:\\Repositories\\Desktop'],
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
			 
a.datas += [('Code\main_kivi.kv',
'D\\Repositories\\Desktop\main_kivi.kv',
'DATA')]
			 
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Warhammer Helper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='assets\\WH_logo.ico')
coll = COLLECT(exe, Tree('D:\\Repositories\\Desktop\\'), Tree('D:\\Repositories\\asset\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
			   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Warhammer Helper')
