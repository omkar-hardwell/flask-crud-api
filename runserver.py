"""Application entry point"""
from flask import Flask
from src import api


if __name__ == "__main__":
    api.app.run(port=5000, debug=True)
