import ollama

model_name = 'inclusion-bot:latest' 

try:
    stream = ollama.chat(
        model=model_name,
        messages=[
            {'role': 'user', 'content': 'hi there!'}
        ],
        stream=True
    )
    print(f"successfully connected to {model_name}\n")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
except ollama.ResponseError as e:
    if e.status_code == 404:
        print(f"Model '{model_name}' not found. Creating from Modelfile...")
        ollama.create(model_name)
        print(f"Model '{model_name}' created successfully. Please rerun the script.")
    else:
        print(f"An error occurred: {e}")
