from ollama import chat
from ollama import ChatResponse


def anamnese_ai_analysis(ocr_text):
    response: ChatResponse = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": "Analise o seguinte paciente e gere um relatório simples com achados, possíveis diagnósticos e sugestões finais, pronto para PDF: "
                + str(ocr_text),
            },
        ],
    )
    return response.message.content
