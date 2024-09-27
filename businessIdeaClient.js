const axios = require('axios');

const userSkills = "education, software development";

async function getBusinessIdea() {
    try {
        const response = await axios.post('http://localhost:5000/generate_business_idea', {
            skills: userSkills
        });

        if (response.data.error) {
            console.log('Error:', response.data.error);
            return null;
        }

        const businessIdea = response.data.business_idea;
        console.log('Business Idea:', businessIdea);
        return businessIdea;  // Return the business idea for further processing
    } catch (error) {
        console.error('Error generating business idea:', error);
    }
}

async function getSteps(businessIdea) {
    if (!businessIdea) {
        console.log('No business idea provided, skipping steps generation.');
        return;
    }
    try {
        const response = await axios.post('http://localhost:5000/generate_steps', {
            business_idea: businessIdea
        });

        if (response.data.error) {
            console.log('Error:', response.data.error);
            return;
        }

        const steps = response.data.steps;
        console.log('Steps to Achieve the Business:', steps);
    } catch (error) {
        console.error('Error generating steps:', error);
    }
}

async function getBusinessPlan(businessIdea) {
    if (!businessIdea) {
        console.log('No business idea provided, skipping business plan generation.');
        return;
    }
    try {
        const response = await axios.post('http://localhost:5000/generate_business_plan', {
            business_idea: businessIdea
        });

        if (response.data.error) {
            console.log('Error:', response.data.error);
            return;
        }

        const businessPlan = response.data.business_plan;
        console.log('Business Plan:', businessPlan);
    } catch (error) {
        console.error('Error generating business plan:', error);
    }
}

async function getMentors() {
    try {
        const response = await axios.post('http://localhost:5000/get_mentors', {
            skills: userSkills
        });

        if (response.data.error) {
            console.log('Error:', response.data.error);
            return;
        }

        const mentors = response.data.mentors;
        console.log('Matched Mentors:', mentors);
    } catch (error) {
        console.error('Error fetching mentors:', error);
    }
}

async function main() {
    const businessIdea = await getBusinessIdea();
    await getSteps(businessIdea);
    await getBusinessPlan(businessIdea);
    await getMentors();
}

main();
