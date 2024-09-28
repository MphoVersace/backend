from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Function to generate business idea based on input skills
def generate_business_idea(skills):
    # Enhanced prompt with examples and detailed instructions
    prompt = (
        "You are an expert business consultant. Generate a unique business idea based on the given skills. The business idea should include a brief description, target market, potential revenue streams, key steps to start, and why the idea is promising.\n\n"
        
        "Example 1:\n"
        "Skills: cooking, social media\n"
        "Business Idea: Start a YouTube cooking channel that shares quick and easy recipes for busy professionals. Target young adults and working professionals who want to cook healthy meals. Use affiliate marketing and sponsorships as revenue streams. Key steps include setting up the channel, creating a content calendar, and collaborating with food brands. The idea is promising because there’s a high demand for accessible, healthy cooking content online.\n\n"
        
        "Example 2:\n"
        "Skills: software development, education\n"
        "Business Idea: Develop an online coding bootcamp focused on teaching practical software development skills. Target recent graduates and career switchers looking to enter the tech industry. Revenue comes from course fees and subscription plans. Key steps include creating a curriculum, building an interactive learning platform, and marketing through educational blogs and social media. The idea has potential due to the increasing demand for remote learning and tech jobs.\n\n"
        
        "Example 3:\n"
        "Skills: graphic design, fashion\n"
        "Business Idea: Launch an online custom apparel store where users can design their own clothing. Target fashion enthusiasts and small businesses looking for branded merchandise. Revenue streams include product sales and custom design services. Key steps include setting up an e-commerce platform, sourcing quality materials, and marketing through fashion blogs and social media ads. The idea is unique because it combines creativity with personalized fashion trends.\n\n"
        
        f"Skills: {skills}\n"
        "Business Idea:"
    )
    
    # Encode the input prompt
    inputs = tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=800)
    
    # Generate text with adjusted parameters
    outputs = model.generate(
        inputs,
        max_length=800,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        no_repeat_ngram_size=3,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Decode the generated text
    idea = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract the generated business idea by removing the prompt from the output
    generated_text = idea[len(prompt):].strip()
    
    return generated_text



# Function to generate business steps and plan
def generate_business_steps_and_plan(skills, business_idea):
    # Enhanced prompt for generating steps and business plan based on the provided business idea
    prompt = (
        "You are an expert business consultant. Based on the given business idea, generate detailed steps to achieve it and create a basic business plan. The plan should include a description of the business, the target market, revenue streams, a marketing strategy, and an estimated timeline.\n\n"
        
        "Example 1:\n"
        "Business Idea: Start a YouTube cooking channel for quick and easy recipes.\n"
        "Steps to Achieve:\n"
        "1. Set up a YouTube channel and social media accounts.\n"
        "2. Develop a content plan focusing on popular, easy-to-make dishes.\n"
        "3. Record and edit high-quality cooking videos.\n"
        "4. Engage with followers on social media to build a community.\n"
        "5. Monetize through affiliate marketing, sponsorships, and ads.\n"
        "Business Plan: Target busy professionals and young adults who seek simple meal ideas. Revenue comes from ads, sponsored content, and affiliate marketing. Marketing will involve cross-promotion on social media platforms. Estimated timeline: 3 months to build a content library and gain a following.\n\n"
        
        "Example 2:\n"
        "Business Idea: Create an online coding bootcamp.\n"
        "Steps to Achieve:\n"
        "1. Research market demand for coding bootcamps.\n"
        "2. Develop an interactive online platform with live coding lessons.\n"
        "3. Design a curriculum focusing on in-demand programming languages.\n"
        "4. Build a team of instructors and mentors.\n"
        "5. Launch a marketing campaign targeting recent graduates and career switchers.\n"
        "Business Plan: Target individuals looking to start a career in software development. Revenue streams include subscription plans and one-time course fees. Marketing strategies include social media ads, partnerships with tech blogs, and referral programs. Estimated timeline: 6 months to develop the platform and curriculum.\n\n"
        
        f"Business Idea: {business_idea}\n"
        "Steps to Achieve:\n"
        "1. "
    )
    
    # Encode the input prompt
    inputs = tokenizer.encode(prompt, return_tensors='pt', truncation=True, max_length=800)
    
    # Generate text with adjusted parameters
    outputs = model.generate(
        inputs,
        max_length=1000,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        no_repeat_ngram_size=3,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Decode the generated text
    plan = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract the generated steps and plan by removing the prompt from the output
    generated_text = plan[len(prompt):].strip()
    
    return generated_text


# Load mentor data from JSON file
def load_mentors():
    with open('AI_model/mentors.json', 'r') as f:
        mentors = json.load(f)
    return mentors

# Function to suggest mentors based on skills
def suggest_mentors(user_skills):
    # Load mentors data
    mentors = load_mentors()
    suggested_mentors = []

    # Prepare a prompt for mentor suggestions
    prompt = (
        "Based on the user's skills, suggest mentors who can provide guidance and describe how each mentor can assist in developing the business idea.\n\n"
        "Skills: marketing, software development\n"
        "Suggested Mentors:\n"
        "1. John Doe - Expertise in marketing strategies for tech startups. Can provide guidance on digital marketing campaigns and customer acquisition.\n"
        "2. Jane Smith - Experienced software developer with knowledge of building scalable web applications. Can mentor on technical aspects of product development and deployment.\n\n"
        "Skills: graphic design, social media\n"
        "Suggested Mentors:\n"
        "1. Emily Davis - Skilled graphic designer with a strong background in branding. Can help in creating a unique brand identity for social media presence.\n"
        "2. Michael Johnson - Social media marketing expert. Can provide insights on building a social media following and monetizing content.\n\n"
        f"Skills: {user_skills}\n"
        "Suggested Mentors:\n"
    )

    # Suggest mentors based on user skills
    for mentor in mentors:
        if any(skill in mentor['skills'] for skill in user_skills.split(", ")):
            suggested_mentors.append(f"{mentor['name']} - Expert in {', '.join(mentor['skills'])}.")

    # Fallback response if no suitable mentors are found
    if not suggested_mentors:
        suggested_mentors.append("No suitable mentors found based on the provided skills.")
    
    # Combine suggestions into the response
    mentor_suggestions = "\n".join([f"{i + 1}. {mentor}" for i, mentor in enumerate(suggested_mentors)])
    
    # Combine with the prompt for generating a complete response
    final_prompt = prompt + mentor_suggestions
    
    return final_prompt