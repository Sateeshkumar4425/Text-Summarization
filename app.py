<<<<<<< HEAD

import torch
import gradio as gr
from transformers import pipeline

# use of pipeline as a high-level helper
# model_path = "../Models/models--sshleifer--distilbart-cnn-12-6"

=======
import os
import gradio as gr
from transformers import pipeline

>>>>>>> 7d776450fcd713b4df7e26ee28e7820f418a51ba
text_summary = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    device=-1
)

def summarize(text):
    if not text.strip():
        return "Please enter some text to summarize."

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
    title="GenAI Project: Text Summarization using DistilBART",
    description="This application summarizes long text using the DistilBART model from Hugging Face."
)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.getenv("PORT", 7860)),
    share=False
)
