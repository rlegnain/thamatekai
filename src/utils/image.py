import ollama


response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['image.jpg']
    }]
)


def get_llm_vision():
    model = 'llama3.2-vision'
    llm = ollama.chat(
        model=model,
        messages=[{
            'role': 'user',
            'content': 'What is in this image?',
            'images': ['image.jpg']
        }]
    )
    return llm

def extract_data_from_image(query: dict):
    ## llm = get_llm(model)
    ## 
    pass