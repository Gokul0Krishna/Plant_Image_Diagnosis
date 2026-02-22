# 🌿 Intelligent Plant Disease Analysis Pipeline

A production-grade, modular computer vision pipeline for plant disease detection and environmental risk analysis.

This project implements a fully structured ML pipeline designed for scalability, maintainability, and real-world agricultural deployment scenarios.

---

## 🚀 Overview

This pipeline performs:

- 🌱 Plant disease detection from leaf images
- 📍 Elevation-based environmental context analysis
- 🌦 Weather-aware disease risk assessment
- 🧪 Automated treatment recommendations
- 📊 Structured multi-component output generation

The system is designed with separation of concerns, configuration-driven architecture, and modular extensibility.

---

## 🏗 Architecture

The pipeline follows a clean layered architecture:

Input Image Path
↓
Image Preprocessing
↓
Model Inference (YOLO / CNN)
↓
Disease Classification
↓
Environmental Data Integration
↓
Weather Risk Analysis
↓
Structured Report Output

Each stage is modular and independently testable.

---

## 🧠 Core Features

- ✔ Modular pipeline design
- ✔ Environment-based configuration (.env)
- ✔ Model abstraction layer
- ✔ Replaceable inference engine (YOLO / CNN)
- ✔ Clean separation between logic and I/O
- ✔ Production-ready structure
- ✔ Easily deployable to API or containerized environments

---

## 🛠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLO (if using .pt model)
- TensorFlow / Keras (if using .h5 model)
- NumPy
- python-dotenv

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/project-name.git
cd project-name

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt