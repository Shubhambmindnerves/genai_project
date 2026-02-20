import requests

class OllamaClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.ollama.com/v1'  # Assume this is the base URL for the Ollama API

    def get_model(self, model_name):
        endpoint = f'{self.base_url}/models/{model_name}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(endpoint, headers=headers)
        return response.json()

    def generate_response(self, model_name, prompt):
        endpoint = f'{self.base_url}/generate'
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        data = {
            'model': model_name,
            'prompt': prompt
        }
        response = requests.post(endpoint, headers=headers, json=data)
        return response.json()  

# Example usage (uncomment and use in actual implementation):
# ollama_client = OllamaClient(api_key='your_api_key')
# response = ollama_client.generate_response(model_name='text-gpt', prompt='Hello, how are you?')
# print(response)