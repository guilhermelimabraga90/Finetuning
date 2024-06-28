import openai
from openai import OpenAI

client = OpenAI(api_key = "")
response =  client.files.create(
  file=open("file-tunning.jsonl", "rb"),
  purpose="fine-tune"
)

nome_do_arquivo = response.id
print(nome_do_arquivo)