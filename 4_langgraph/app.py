import gradio as gr
import atexit
from sidekick import Sidekick
import asyncio

# Global reference to the current Sidekick instance
sidekick_ref = {"value": None}

# --- 非同步初始化 Sidekick ---
async def app_setup():
    sidekick = Sidekick()
    await sidekick.setup()
    sidekick_ref["value"] = sidekick  # Register instance for cleanup
    print(f"✅ Sidekick setup completed, ID: [{sidekick.sidekick_id}]")
    return sidekick

# --- 處理使用者輸入 ---
async def process_message(sidekick, message, success_criteria, history):
    results = await sidekick.run_superstep(message, success_criteria, history)
    return results, sidekick

# --- 重設 Sidekick 實例 ---
async def reset():
    old = sidekick_ref.get("value")
    if old and hasattr(old, "free_resources"):
        try:
            print(f"\n♻️ Resetting: cleaning up previous Sidekick [{old.sidekick_id}]")
            await old.free_resources()
        except Exception as e:
            print(f"⚠️ Error during previous Sidekick cleanup: {e}")

    # 建立新 Sidekick 實例
    new_sidekick = Sidekick()
    await new_sidekick.setup()
    sidekick_ref["value"] = new_sidekick
    print(f"✅ Sidekick reset completed, ID: [{new_sidekick.sidekick_id}]")
    return "", "", None, new_sidekick

# ✅ --- 資源釋放 ---
def free_resources():
    try:
        sk = sidekick_ref["value"]
        print(f"\n♻️  Cleaning up Sidekick resources [{sk.sidekick_id}]")

        if sk and hasattr(sk, "free_resources"):
            # 同步調用 async 資源釋放
            asyncio.run(sk.free_resources())
            print("🧹 Sidekick resources have been cleaned up.")
    except Exception as e:
        print(f"⚠️ Exception during cleanup: {e}")

atexit.register(free_resources)

# --- Gradio UI 建構 ---
with gr.Blocks(title="Sidekick", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("## 🤖 Sidekick Personal Co-Worker")

    sidekick = gr.State(delete_callback=lambda sk: None)  # Not needed since atexit is used

    with gr.Row():
        chatbot = gr.Chatbot(label="Sidekick", height=300, type="messages")

    with gr.Group():
        with gr.Row():
            message = gr.Textbox(show_label=False, placeholder="Your request to the Sidekick")
        with gr.Row():
            success_criteria = gr.Textbox(show_label=False, placeholder="What are your success criteria?")

    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
        go_button = gr.Button("Go!", variant="primary")

    print("🚀 Application starting...")
    ui.load(app_setup, [], [sidekick])
    message.submit(process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick])
    success_criteria.submit(process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick])
    go_button.click(process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick])
    reset_button.click(reset, [], [message, success_criteria, chatbot, sidekick])

# 啟動 UI
ui.launch(inbrowser=True)
