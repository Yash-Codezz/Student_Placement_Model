#!/bin/sh
uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run Frontend/app.py --server.port=8501 --server.address=0.0.0.0
