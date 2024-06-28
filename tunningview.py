from openai import OpenAI
client = OpenAI(api_key = "")

completion = client.completions.create(
    model="ft:davinci-002:personal::9fEB8819",
    prompt= "Naquele exato momento, várias figuras importantes para a Seleção Real estavam reunidas em torno da mesa, enquanto os outros vigiavam a situação dos cantos.",
    stop=["\n"],
    max_tokens=1024
)

#print(completion.choices)
print(completion.choices[0].text)
#ft = "ft:davinci-002:personal::9esWQTOv"
#client = OpenAI(api_key = "")


#print(client.fine_tuning.jobs.retrieve("ftjob-B92w53zdLfSKxqpaantUWgKZ"))

#print(client.fine_tuning.jobs.list())