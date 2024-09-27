from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pre-trained GPT-2 model and tokenizer from Hugging Face
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Predefined list of mentors for demonstration
mentors_data = [
    {"name": "Alice Smith", "skills": ["marketing", "sales"]},
    {"name": "Bob Johnson", "skills": ["software development", "AI"]},
    {"name": "Carol White", "skills": ["business strategy", "finance"]},
]

# Function to generate text using the model
def generate_text(prompt, max_length=150, stop_token=None):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Use stop token to clean up the response
    if stop_token:
        text = text.split(stop_token)[0]
    return text.strip()

# Generate a business idea using GPT-2
@app.route('/generate_business_idea', methods=['POST'])
def generate_business_idea():
    try:
        user_input = request.json.get('skills', '')
        print(f"Received skills: {user_input}")  # Debugging line

        prompt = f"Based on the skills {user_input}, a great business idea would be to"
        business_idea = generate_text(prompt, max_length=100, stop_token='.')

        return jsonify({"business_idea": business_idea})

    except Exception as e:
        print(f"Error in generate_business_idea: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Generate steps to achieve the business idea
@app.route('/generate_steps', methods=['POST'])
def generate_steps():
    business_idea = request.json.get('business_idea', '')

    try:
        prompt = f"To achieve the business idea '{business_idea}', follow these steps:"
        steps = generate_text(prompt, max_length=200, stop_token='.')

        return jsonify({"steps": steps})

    except Exception as e:
        print(f"Error in generate_steps: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Generate a business plan for the business idea
@app.route('/generate_business_plan', methods=['POST'])
def generate_business_plan():
    business_idea = request.json.get('business_idea', '')

    try:
        prompt = f"Create a detailed business plan for the business idea: {business_idea}. The plan should include market analysis, revenue streams, and marketing strategy."
        business_plan = generate_text(prompt, max_length=300, stop_token='.')

        return jsonify({"business_plan": business_plan})

    except Exception as e:
        print(f"Error in generate_business_plan: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Match mentors based on user skills
@app.route('/get_mentors', methods=['POST'])
def get_mentors():
    user_skills = request.json.get('skills', '').lower().split(', ')
    matched_mentors = []

    for mentor in mentors_data:
        if any(skill in mentor['skills'] for skill in user_skills):
            matched_mentors.append(mentor)

    return jsonify({"mentors": matched_mentors})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
