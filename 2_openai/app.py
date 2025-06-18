# app.py — Hugging Face Space entry point

from deep_research.deep_research import launch_ui  # 匯入 UI 构建函式

# Hugging Face Spaces 會尋找 demo/app/iface 這樣的變數作為啟動點
ui = launch_ui()
ui.launch(inbrowser=True)
