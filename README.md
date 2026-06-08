# AI Content Generator

A simple Flask-based AI content generator web app with title, description, language selection, and saved content history.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the environment:
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Windows CMD:
     ```cmd
     .\venv\Scripts\activate.bat
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your OpenAI API key:
   ```powershell
   $env:OPENAI_API_KEY = "your_openai_api_key_here"
   ```
5. Run the app:
   ```bash
   python app.py
   ```

## Usage

1. Open `http://127.0.0.1:5000` in your browser.
2. Enter a title, optional description, topic prompt, and select a language.
3. Click **Generate Content**.
4. Generated content is displayed and also saved automatically.

## Features

- Title and description inputs for every article
- Support for English and Bengali content generation
- Saved results history shown in the sidebar
- Saved data stored in `saved_results.json`

## Notes

- Replace `your_openai_api_key_here` with a valid OpenAI API key.
- Saved results are stored locally in `saved_results.json`.
