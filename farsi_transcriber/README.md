# Farsi Transcriber

A desktop application for transcribing Farsi audio and video files using OpenAI's Whisper model.

## Features

- 🎙️ Transcribe audio files (MP3, WAV, M4A, FLAC, OGG, etc.)
- 🎬 Extract audio from video files (MP4, MKV, MOV, WebM, AVI, etc.)
- 🇮🇷 High-accuracy Farsi transcription
- ⏱️ Word-level timestamps
- 📤 Export to multiple formats (TXT, SRT, JSON)
- 💻 Clean PyQt6-based GUI

## System Requirements

- Python 3.8+
- ffmpeg (for audio/video processing)
- 8GB+ RAM recommended (for high-accuracy model)

### Install ffmpeg

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

**Windows (Chocolatey):**
```bash
choco install ffmpeg
```

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## Usage

### GUI Application
```bash
python main.py
```

Then:
1. Click "Select File" to choose an audio or video file
2. Click "Transcribe" and wait for processing
3. View results with timestamps
4. Export to your preferred format

### Command Line (Coming Soon)
```bash
python -m farsi_transcriber --input audio.mp3 --output transcription.srt
```

## Model Information

This application uses OpenAI's Whisper model optimized for Farsi:
- **Model**: medium or large (configurable)
- **Accuracy**: Optimized for Persian language
- **Processing**: Local processing (no cloud required)

## Project Structure

```
farsi_transcriber/
├── ui/               # PyQt6 UI components
├── models/           # Whisper model management
├── utils/            # Utility functions
├── main.py           # Application entry point
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Development

### Running Tests
```bash
pytest tests/
```

### Code Style
```bash
black .
flake8 .
isort .
```

## License

MIT License - See LICENSE file for details

## Contributing

This is a personal project, but feel free to fork and modify for your needs!
