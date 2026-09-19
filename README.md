# MASA Transcribe Studio

Audio and video transcription desktop utility converting speech tracks into structured text

## Technical Architecture

The application is architected with modular separation of concerns adhering to modern clean code standards:

- **Component Layering**: Isolated view layouts, state managers, and service controllers.
- **Defensive Engineering**: Robust input sanitization and exception management.
- **Modern Design Standards**: High-contrast dark-mode interface styled for optimal usability and visual polish.

## Preview

![Application Interface](screenshots/app_interface.png)

## Features

- Video audio stream demuxing and WAV sample extraction pipeline.
- Speech recognition engine converting spoken passages into timestamps and transcripts.
- Export options for TXT and SRT subtitle formats.
- Interactive audio playback preview with synchronous transcript viewing.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter pillow requests
```

## Execution

Launch the application via Python:

```bash
python "transcribeapp.py"
```

## Project Structure

```
.
├── transcribeapp.py
├── screenshots/
│   └── app_interface.png
├── .gitignore
├── LICENSE             # MIT License
└── README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.
