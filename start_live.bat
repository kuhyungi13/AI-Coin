@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo Installing packages (first time takes a few minutes)...
py -m pip install --quiet -r requirements.txt -r requirements-live.txt
echo Starting. Your browser will open http://localhost:8501 in a few seconds.
echo Close this window to stop.
start "" cmd /c "timeout /t 8 > nul & start http://localhost:8501"
py -m streamlit run live_paper.py --server.headless true --server.port 8501 --browser.gatherUsageStats false
pause
