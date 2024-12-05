@echo off
git clone https://github.com/Arturo218/MaestroDeTareas.git
cd MaestroDeTareas
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
python app.py