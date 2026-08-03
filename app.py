import os
import gradio as gr
from transformers import pipeline

text_summary = pipeline(
    "summarization",
    model=model_path,
    tokenizer=model_path,
    device=-1
)

def summarize(text):
    result = text_summary(
        text,
        max_length=130,
        min_length=30,
        do_sample=False
    )
    return result[0]["summary_text"]

demo = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(lines=10, label="Input Text"),
    outputs=gr.Textbox(label="Summary"),
    title="GenAI_Project: Text Summarization using DistilBART",
    description="This applications helps to summarize text using DistilBART"
)

demo.launch()

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.getenv("PORT", 7860))
)
