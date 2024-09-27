from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask import Flask, request, jsonify

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

app = Flask(__name__)

# Predefined list of mentors for demonstration
mentors_data = [
    {"name": "Alice Smith", "skills": ["marketing", "sales"]},
    {"name": "Bob Johnson", "skills": ["software development", "AI"]},
    {"name": "Carol White", "skills": ["business strategy", "finance"]},
]

# Generate a business idea based on user skills
@app.route('/generate_business_idea', methods=['POST'])
def generate_business_idea():
    user_input = request.json.get('skills', '')
    prompt = f"Business idea for someone with skills in {user_input}: Here's an innovative business idea: "

    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    idea = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"business_idea": idea})

# Generate steps to achieve the business
@app.route('/generate_steps', methods=['POST'])
def generate_steps():
    business_idea = request.json.get('business_idea', '')
    prompt = f"Steps to achieve the business idea: {business_idea}. Step 1:"

    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)
    steps = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"steps": steps})

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
