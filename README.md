# Analisador de Documentos com IA

Script em Python para análise de documentos PDF com uso da API da OpenAI.

O Desafio propõe uma ideia parecida de RAG, pois usa um documento para responder perguntas.

O programa recebe um arquivo PDF e uma pergunta em linguagem natural, envia o documento para a API da OpenAI e retorna uma resposta estruturada em JSON, contendo uma resposta em Markdown, o nome do PDF recebido e 3 perguntas de acompanhamento.

## Funcionalidades

- Recebe um arquivo PDF local como entrada
- Recebe uma pergunta do usuário em linguagem natural
- Envia o PDF e a pergunta para a API da OpenAI
- Retorna a resposta em JSON na estrutura pedida
- Gera resposta no campo `text` usando Markdown
- Retorna o nome do PDF utilizado `source`
- Retorna exatamente 3 perguntas de acompanhamento

## Formato da resposta

A resposta final segue obrigatoriamente o formato:

```json
{
  "type": "text",
  "text": "<resposta em Markdown>",
  "source": "<nome do documento ou N/A>",
  "suggestions": [
    "<pergunta 1>",
    "<pergunta 2>",
    "<pergunta 3>"
  ]
}
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/marioccomp/active-bi-ai-document-analyzer.git
cd active-bi-ai-document-analyzer
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
OPENAI_KEY=sua_chave_da_openai
OPENAI_MODEL=gpt-5.4-mini
```

## Como executar

O script recebe dois argumentos:

1. O caminho do arquivo PDF
2. A pergunta do usuário

Formato:

```bash
python main.py caminho/do/arquivo.pdf "sua pergunta"
```

Exemplo:

```bash
python main.py ./relatorio.pdf "Quais são os principais pontos do documento?"
```

A resposta será exibida no terminal em formato JSON.

## Modelo escolhido

O modelo utilizado no projeto é o `gpt-5.4-mini`.

Escolhi esse modelo porque é um bom equilíbrio entre qualidade, custo e velocidade. Como o desafio envolve análise de documentos PDF, interpretação de perguntas em linguagem natural e geração de uma resposta estruturada em JSON, o modelo atende bem aos requisitos.

Além disso, o modelo pode ser alterado pela variável `OPENAI_MODEL` no arquivo `.env`.

## Estimativa de custo

A estimativa pode ser calculada da seguinte forma:

```text
custo total = (tokens de entrada / 1_000_000 × 0.75) + (tokens de saída / 1_000_000 × 4.50)

O custo eu calculei do gpt-5.4-mini no modo Standard, mostro a seguir:

- Input: US$ 0.75 por 1 milhão de tokens
- Cached input: US$ 0.075 por 1 milhão de tokens
- Output: US$ 4.50 por 1 milhão de tokens 

```


