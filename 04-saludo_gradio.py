import gradio as gr

def saludo(nombre):
    return "Hola " + nombre + ", ¿Como estas???? "


demo = gr.Interface(
    fn=saludo, 
    inputs = "text",    #Ingresar nombre
    outputs = "text"
)

demo.launch()
#El Server apunta a http://localhost:7860