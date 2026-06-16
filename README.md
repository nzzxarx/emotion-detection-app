# Emotion Detection Application

A Python-based web application that analyzes textual data to detect emotions using the IBM Watson NLP library and Flask framework.

## Project Description
This application takes a string input from the user and analyzes it to determine the scores of five key emotions: **Anger**, **Disgust**, **Fear**, **Joy**, and **Sadness**. It also identifies the **Dominant Emotion** based on the highest score.

## Features
- Integrates with Watson NLP EmotionPredict API.
- Built with Flask backend.
- Full error handling for blank inputs (Status Code 400).
- 10/10 PyLint compliance for static code analysis.
- Unit tested using Python's `unittest` library.

## Project Structure
```text
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── server.py
├── test_emotion_detection.py
└── README.md
