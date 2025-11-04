from ollama import chat
from ollama import ChatResponse


def anamnese_ai_analysis(ocr_text):
    response: ChatResponse = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": "Interprete os seguintes dados do paciente e gere um relatório simples com achados, possíveis diagnósticos e sugestões finais em Português do Brasil (PTBR), dividido em Títulos, subtítulos e seções em formato MARKDOWN. (SEM # nos titulos): "
                + str(ocr_text),
            },
        ],
    )
    return response.message.content
