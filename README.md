---
title: Hand-Digit-Recognizer
emoji: ✍️
colorFrom: black
colorTo: gray
sdk: fastapi
app_file: main.py
pinned: true
license: mit
tags:
  - computer-vision
  - handwritten-digit
  - numpy
  - fastapi
  - render
  - vercel
  - digit-classifier
---

[![Deployed on Render](https://img.shields.io/badge/Backend-Render-blue?logo=render&style=flat-square)](https://digitrecognizer.onrender.com)
[![Frontend on Vercel](https://img.shields.io/badge/Frontend-Vercel-black?logo=vercel&style=flat-square)](https://hand-digit-recognizer.vercel.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![GitHub last commit](https://img.shields.io/github/last-commit/McKlay/DigitRecognizerWebApp)
![GitHub Repo stars](https://img.shields.io/github/stars/McKlay/DigitRecognizerWebApp?style=social)
![GitHub forks](https://img.shields.io/github/forks/McKlay/DigitRecognizerWebApp?style=social)
![MIT License](https://img.shields.io/github/license/McKlay/DigitRecognizerWebApp)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=McKlay.DigitRecognizerWebApp)

---

# ✍️ Hand Digit Recognizer

A real-time digit recognizer powered by a neural network built **entirely from scratch** using **NumPy**, combined with a modern **ReactJS** canvas interface and a **FastAPI** backend.

> Draw any digit from 0 to 9 — our ANN will try to guess it.

---

## 🌐 Live Demo

- **Backend (Render):** [`https://digitrecognizer.onrender.com`](https://digitrecognizer.onrender.com)  
- **Frontend (Vercel):** [`https://hand-digit-recognizer.vercel.app`](https://hand-digit-recognizer.vercel.app)

---

## Tech Stack

- **Neural Network**: Custom architecture built from scratch using NumPy
- **API**: FastAPI for backend digit inference
- **Frontend**: ReactJS + Canvas + Axios
- **Hosting**: 
  - Backend: **Render**
  - Frontend: **Vercel**

---

## Features

- Custom ANN (no frameworks — just NumPy!)
- Canvas UI to draw digits directly in the browser
- Live prediction on image upload via API
- Fully deployed using free-tier services
- CORS-handled for seamless Vercel↔Render integration
- Health check endpoint for deployment stability

---

## How to Use

1. Visit the live frontend [here](https://hand-digit-recognizer.vercel.app)
2. Draw a digit (0–9) in the box
3. Click `Predict`
4. The prediction will appear below the canvas

---

## Local Setup

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd ../frontend
npm install
npm start
````

---

## Project Structure

```bash
DigitRecognizerWebApp/
├── backend/
│   ├── main.py              # FastAPI backend logic
│   ├── model_weights.npz    # Saved ANN weights
│   ├── models/              # ANN layers and loss functions
│   ├── utils/               # Image preprocessing & model loader
│   └── requirements.txt
│
├── frontend/
│   ├── src/                 # React canvas logic and UI
│   ├── public/
│   └── package.json
│
├── Dockerfile               # Backend Docker setup (Render)
└── README.md
```

---

## API Endpoints

| Route       | Method | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| `/predict/` | POST   | Accepts image file and returns predicted digit |
| `/`         | GET    | Root route – basic live check                  |
| `/healthz`  | GET    | Health monitor for Render                      |

---

## 👨‍💻 Author

Built with ❤️ by [Clay Mark Sarte](https://github.com/McKlay)  
Custom AI + Modern Web + Cloud Deployment

---

## License

This project is licensed under the **MIT License**.

---
