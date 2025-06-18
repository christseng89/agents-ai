import gradio as gr
from dotenv import load_dotenv
# from research_manager import ResearchManager
from deep_research.research_manager import ResearchManager

load_dotenv(override=True)

def launch_ui():
    async def run(query):
        async for chunk in ResearchManager().run(query):
            yield chunk

    with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
        gr.Markdown("# Deep Research")
        query_textbox = gr.Textbox(label="What topic would you like to research?")
        run_button = gr.Button("Run", variant="primary")
        report = gr.Markdown(label="Report")
        
        run_button.click(fn=run, inputs=query_textbox, outputs=report)
        query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)
    return ui

if __name__ == "__main__":
    ui = launch_ui()
    ui.launch(inbrowser=True)
