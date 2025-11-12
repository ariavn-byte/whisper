#!/usr/bin/env python3
"""
Farsi Transcriber - Main Entry Point

A PyQt6-based desktop application for transcribing Farsi audio and video files.
"""

import sys
from PyQt6.QtWidgets import QApplication


def main():
    """Main entry point for the application"""
    app = QApplication(sys.argv)

    # TODO: Import and create main window
    # from ui.main_window import MainWindow
    # window = MainWindow()
    # window.show()

    print("Farsi Transcriber App initialized (setup phase)")
    print("✓ PyQt6 environment ready")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
