# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
from PyInstaller.utils.hooks import get_package_paths
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT, BUNDLE, TOC

data_altair = (
    (Path(get_package_paths("altair")[1]) / "vegalite/v4/schema/vega-lite-schema.json").as_posix(),
    "./altair/vegalite/v4/schema/"
)
data_streamlit = (
    (Path(get_package_paths("streamlit")[1]) / "static").as_posix(),
    "./streamlit/static"
)

block_cipher = None


a = Analysis(
    ["./run.py"],
    pathex=["."],
    binaries=[],
    datas=[
        data_altair,
        data_streamlit,
        ("./app", "./app")
    ],
    hiddenimports=[
        "streamlit"
    ],
    hookspath=["./hooks"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="Streamkit",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name="Streamkit.app",
    icon=None,
    bundle_identifier=None,
)
