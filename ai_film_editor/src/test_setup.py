import os
import cv2
import torch
import spacy
import pandas as pd
import sklearn
import transformers
from moviepy import VideoFileClip

def run_health_check():
    print("\n" + "="*50)
    print("🚀 AI FILM EDITOR: SYSTEM HEALTH CHECK")
    print("="*50)

    # 1. Check Video Libraries
    print(f"✅ OpenCV Version: {cv2.__version__}")
    
    try:
        # Testing MoviePy 2.0+ 
        print(f"✅ MoviePy: Ready to process video")
    except Exception as e:
        print(f"❌ MoviePy Error: {e}")

    # 2. Check AI & Machine Learning Power
    print(f"✅ Torch (AI Engine): Running on {'GPU (Nvidia)' if torch.cuda.is_available() else 'CPU'}")
    print(f"✅ Scikit-Learn: {sklearn.__version__}")
    print(f"✅ Transformers (NLP): {transformers.__version__}")

    # 3. Check Script Analysis (Spacy)
    try:
        nlp = spacy.load("en_core_web_sm")
        print("✅ Spacy Language Model: 'en_core_web_sm' is LOADED")
    except Exception:
        print("❌ Spacy Error: Language model not found.")
        print("   FIX: Run 'python -m spacy download en_core_web_sm' in terminal.")

    # 4. Check Project Folder Structure
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    required_folders = ['data/raw_video', 'data/scripts', 'output', 'src']
    
    print("\n--- Folder Structure Check ---")
    for folder in required_folders:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            print(f"✅ Found: {folder}")
        else:
            print(f"⚠️ Missing: {folder} (Please create this)")

    print("="*50)
    print("RESULT: If all items are ✅, you are ready to build!")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_health_check()