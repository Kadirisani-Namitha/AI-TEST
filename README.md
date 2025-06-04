# AI Pipeline Assignment – FastAPI

This project implements a mock AI pipeline using FastAPI. It simulates the process of:

- Interpreting a text prompt
- Generating a mock image (text-to-image)
- Generating a mock 3D model (image-to-3D)
- Storing prompt history in memory

## 🔧 Features

- FastAPI backend with `/process` POST endpoint
- Mocked responses (no paid API used)
- CORS enabled for frontend integration
- Prompt memory stored in a Python list

## 📦 How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
