# 🔧 Step 1: Create a Project Folder and Environment
# Open PowerShell / CMD:

# bash
# Copy code
# mkdir ML_Project
# cd ML_Project
# python -m venv venv
# Activate the environment:

# bash
# Copy code
# .\venv\Scripts\activate
# ✅ You should see: (venv) in the terminal line.

# 🔧 Step 2: Upgrade pip
# bash
# Copy code
# pip install --upgrade pip setuptools wheel
# 📦 Step 3: Install All Required Libraries
# bash
# Copy code
# pip install tensorflow
# pip install django
# pip install numpy pandas matplotlib seaborn scikit-learn jupyter
# All of these will be installed in this virtual environment only — clean and safe.

# 🔧 Step 4: Verify Installations
# Create a test file check_setup.py:

# python
# Copy code
# import tensorflow as tf
# import django
# import pandas as pd
# import numpy as np

# print("TensorFlow:", tf.__version__)
# print("Django:", django.get_version())
# print("Pandas:", pd.__version__)
# print("NumPy:", np.__version__)
# Run:

# bash
# Copy code
# python check_setup.py
# 🧠 Step 5: Save Your Setup (Optional but Recommended)
# bash
# Copy code
# pip freeze > requirements.txt
# You can now reuse this requirements.txt in future projects:

# bash
# Copy code
# pip install -r requirements.txt
# 🖥️ Step 6: Use in VS Code
# Open VS Code

# Go to: File → Open Folder → Select ML_Project

# Press Ctrl+Shift+P → Select: Python: Select Interpreter

# Choose the one from:

# bash
# Copy code
# ./venv/Scripts/python.exe
# Now you're using your clean Python 3.10 environment in VS Code.

# 🏁 Done! You're ready to build with:
# Machine Learning libraries ✅

# Django web apps ✅

# Deep Learning (TensorFlow) ✅

# Jupyter notebooks ✅

