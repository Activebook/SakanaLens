"""
This is a setup.py script generated by py2applet

Usage:
    pyinstaller --name="SakanaLens" --windowed --icon=app.icns --add-data="images:images" --add-data="api.json5:." sakana.py

    codesign --force --options runtime --sign - --entitlements entitlements.plist dist/SakanaLens.app

    # Don't use py2app, the app it made cannot be codesigned
    # Use pyinstaller instead
    pip install setuptools==70.3.0

    rm -rf build dist
    python setup.py py2app

    codesign --force --deep --sign - dist/SakanaLens.app
    # First, remove the signature from the problematic library
    codesign --remove-signature dist/SakanaLens.app
    codesign --force --deep  --no-strict --sign - --entitlements entitlements.plist dist/SakanaLens.app
    codesign -vvv dist/SakanaLens.app

    <key>NSInputMonitoringUsageDescription</key>
	<string>This app needs to monitor keyboard input to detect shortcuts.</string>
	<key>NSAppleEventsUsageDescription</key>
	<string>This app needs to control other applications.</string>
	<key>NSScreenCaptureUsageDescription</key>
	<string>This app needs to capture screenshots.</string>
	<key>NSAccessibilityUsageDescription</key>
	<string>This app needs accessibility access to monitor keyboard shortcuts.</string>

    open -a dist/SakanaLens.app
"""

from setuptools import setup

APP = ['sakana.py']
DATA_FILES = [('images', ['images/info_mark.png', 'images/question_mark.png'])]  # Include specific image files
OPTIONS = {
    'argv_emulation': False,
    #'packages': ['rubicon-objc'],  # Include the 'rubicon' package
    'excludes': ['rubicon', 'lzma'],  # Include the 'rubicon' package
    'iconfile': 'app.icns',  # Optional: path to your app icon
    'plist': {
        'CFBundleName': 'SakanaLens',  # Your app name
        'CFBundleDisplayName': 'Sakana Lens 日本語の自動翻訳ツール',
        'CFBundleShortVersionString': '2.0.0',  # Version
        'NSHumanReadableCopyright': 'Copyright © 2025 Charles Liu. All rights reserved.'
        
        #'NSRequiresAquaSystemAppearance': False,
        #'CFBundleGetInfoString': "Monitoring App",
        #'CFBundleIdentifier': "com.activebook.sakanalens",
        #'CFBundleVersion': "2.0.0",
        #'CFBundleShortVersionString': "2.0.0",
        # Required usage descriptions
        #'NSInputMonitoringUsageDescription': 'This app needs to monitor keyboard input to detect shortcuts.',
        #'NSAppleEventsUsageDescription': 'This app needs to control other applications.',
        #'NSScreenCaptureUsageDescription': 'This app needs to capture screenshots.',
        #'NSAccessibilityUsageDescription': 'This app needs accessibility access to monitor keyboard shortcuts.'
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)