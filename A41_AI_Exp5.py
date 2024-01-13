from langchain import HuggingFaceHub
# import langchain.llms.HuggingFaceHub
import warnings

warnings.filterwarnings(action='ignore', category=FutureWarning)

model = "gpt2-medium"
conv = HuggingFaceHub(huggingfacehub_api_token='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', repo_id=model, model_kwargs={'temperature':0.3, "max_new_tokens":150})

while True:
    prompt = input("> ")
    sol = conv(prompt=prompt)
    print(sol)