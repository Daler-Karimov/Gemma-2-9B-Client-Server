import os
from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
from huggingface_hub import login

# Get the path to the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Create the path to the cache folder
cache_dir = os.path.join(base_dir, "model_cache")

# Create the cache folder if it does not exist
os.makedirs(cache_dir, exist_ok=True)

# Authenticate in Hugging Face
login(token='YOUR HB-TOKEN')

# Model ID
model_id = "google/gemma-2-9b"

# Quantization configuration setup
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

# Load the model with quantization and reduced precision
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    torch_dtype=torch.float16,
    device_map="auto",
    cache_dir=cache_dir
)

# Determine the device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Create a Flask instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    
    # Encode the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)

    # Generate text
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=150)

    # Decode the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return render_template('index.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)