# app.py
from flask import Flask, request, jsonify
from model import generate_business_idea, generate_business_steps_and_plan, suggest_mentors

app = Flask(__name__)

@app.route('/generate-idea', methods=['POST'])
def generate_idea():
    skills = request.json.get('skills')
    idea = generate_business_idea(skills)
    return jsonify({"idea": idea})

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    skills = request.json.get('skills')
    
    # First, generate the business idea
    business_idea = generate_business_idea(skills)
    
    # Now, generate the plan based on the business idea
    plan = generate_business_steps_and_plan(skills, business_idea)
    
    return jsonify({"plan": plan})

@app.route('/suggest-mentors', methods=['POST'])
def mentors():
    skills = request.json.get('skills')
    mentors = suggest_mentors(skills)
    return jsonify({"mentors": mentors})

@app.route('/generate-full-report', methods=['POST'])
def generate_full_report():
    skills = request.json.get('skills')
    
    # Generate business idea
    business_idea = generate_business_idea(skills)
    
    # Generate business plan
    business_plan = generate_business_steps_and_plan(skills, business_idea)
    
    # Suggest mentors
    mentors = suggest_mentors(skills)
    
    return jsonify({
        "idea": business_idea,
        "plan": business_plan,
        "mentors": mentors
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
