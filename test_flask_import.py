# test_flask_import.py
try:
    from flask import Flask
    print("Flask is installed and can be imported")
except ImportError as e:
    print("Error importing Flask:", e)
