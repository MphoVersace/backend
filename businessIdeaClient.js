const axios = require('axios');

const userSkills = 'software development, marketing';

async function getBusinessIdea() {
    try {
        const response = await axios.post('http://localhost:5000/generate_business_idea', {
            skills: userSkills
        });
        const businessIdea = response.data.business_idea;
        console.log('Business Idea:', businessIdea);
        return businessIdea;
    } catch (error) {
        console.error('Error generating business idea:', error);
    }
}

async function getSteps(businessIdea) {
    try {
        const response = await axios.post('http://localhost:5000/generate_steps', {
            business_idea: businessIdea
        });
        console.log('Steps to Achieve the Business:', response.data.steps);
    } catch (error) {
        console.error('Error generating steps:', error);
    }
}

async function getMentors() {
    try {
        const response = await axios.post('http://localhost:5000/get_mentors', {
            skills: userSkills
        });
        console.log('Matched Mentors:', response.data.mentors);
    } catch (error) {
        console.error('Error fetching mentors:', error);
    }
}

async function main() {
    const businessIdea = await getBusinessIdea();
    await getSteps(businessIdea);
    await getMentors();
}

main();
