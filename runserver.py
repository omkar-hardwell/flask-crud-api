"""Application entry point"""
from src.api import app


if __name__ == "__main__":
    app.run(port=5000, debug=True)
