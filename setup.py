"""
This is a setup.py script generated by py2applet

Usage:
    pip install setuptools==70.3.0

    rm -rf build dist
    python setup.py py2app
    open -a dist/SakanaLens.app
"""

from setuptools import setup

APP = ['sakana.py']
DATA_FILES = [('images', ['images/info_mark.png', 'images/question_mark.png'])]  # Include specific image files
OPTIONS = {
    'argv_emulation': False,
    #'packages': ['rubicon-objc'],  # Include the 'rubicon' package
    'excludes': ['rubicon'],  # Include the 'rubicon' package
    'iconfile': 'app.icns',  # Optional: path to your app icon
    'plist': {
        'CFBundleName': 'SakanaLens',  # Your app name
        'CFBundleShortVersionString': '2.0.0',  # Version
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)