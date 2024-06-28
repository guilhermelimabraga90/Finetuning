import openai
from openai import OpenAI

# Create the fine-tuning job
client = OpenAI(api_key = "")
client.fine_tuning.jobs.create(
  training_file="file-zlXhKYIfPvzt81faJXHI3USK", 
  model="davinci-002",
)
