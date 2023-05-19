import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "you are a chemistry professor."},
#{"role": "system", "content": "You are a helpful and kind AI Assistant."},

]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Academic Bot",
             description="Ask anything you want",
             theme="compact").launch(share=True)