import sys
import json
import os
import base64
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY");
model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

client = OpenAI(api_key=api_key)

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": ["text"]
        },
        "text": {
            "type": "string",
        },
        "source": {
            "type": "string"
        },
        "suggestions": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["type", "text", "source", "suggestions"],
    "additionalProperties": False
}


def encode_pdf(pdf_path: Path) -> str:
    with open(pdf_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

def analyze_pdf(pdf_path: Path, pergunta: str) -> dict:
    base64_pdf = encode_pdf(pdf_path)

    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": """
                        Você é um analisador de documentos PDF.

                        Sua tarefa:
                        - Ler o PDF enviado
                        - Responder a pergunta do usuário
                        - Gerar uma resposta útil e objetiva
                        - O campo text deve conter Markdown válido com títulos, listas e destaques
                        - O campo source deve conter o nome do documento analisado
                        - O campo suggestions deve conter exatamente 3 perguntas de acompanhamento relevantes

                        Não invente informações. Se o documento não tiver dados suficientes, deixe isso claro no campo text
                    """
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "filename": pdf_path.name,
                        "file_data": f"data:application/pdf;base64,{base64_pdf}",
                    },
                    {
                        "type": "input_text",
                        "text": f"Pergunta do usuário: {pergunta}"
                    }
                ]
            }
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "response",
                "strict": True,
                "schema": RESPONSE_SCHEMA
            }
        }
    )

    return json.loads(response.output_text)

pdf_path = Path(sys.argv[1])
pergunta = sys.argv[2]

if not pdf_path.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

result = analyze_pdf(pdf_path, pergunta)



#  print(result["text"]) Aqui caso queira printar o markdown formatado

print(json.dumps(result, ensure_ascii=False, indent=2))

