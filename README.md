# Fake Motivation Quote Detector

This project is a simple Machine Learning application that classifies motivational quotes as **real** or **fake / generic** using Natural Language Processing (NLP).

## Problem Statement
Motivational quotes are widely shared online, but many of them are repetitive, low-quality, or AI-generated.
The goal of this project is to automatically detect such fake or generic quotes using machine learning.

## Dataset
The dataset contains motivational quotes labeled as:
- real
- fake

The data is manually curated for learning purposes and stored in CSV format.

## Approach
- Text preprocessing
- TF-IDF vectorization
- Logistic Regression classifier
- Train-test split for evaluation

## Project Structure
fake-motivation-quote-detector/
├── README.md
├── train_model.py
└── data/
    ├── README.md
    └── quotes.csv

## Results
The model is trained using Logistic Regression and evaluated using accuracy score.

## Future Improvements
- Increase dataset size
- Try advanced NLP models
- Add a web interface for predictions

## Author
Adhisha


