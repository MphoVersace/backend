// flaskApi.js
const axios = require('axios');

const FLASK_SERVER_URL = 'http://localhost:5000';

const generateIdea = async (skills) => {
    try {
        const response = await axios.post(`${FLASK_SERVER_URL}/generate-idea`, { skills });
        return response.data;
    } catch (error) {
        console.error('Error generating business idea:', error);
        throw error;
    }
};

const generatePlan = async (skills) => {
    try {
        const response = await axios.post(`${FLASK_SERVER_URL}/generate-plan`, { skills });
        return response.data;
    } catch (error) {
        console.error('Error generating business plan:', error);
        throw error;
    }
};

const suggestMentors = async (skills) => {
    try {
        const response = await axios.post(`${FLASK_SERVER_URL}/suggest-mentors`, { skills });
        return response.data;
    } catch (error) {
        console.error('Error suggesting mentors:', error);
        throw error;
    }
};

// New function to generate the full report
const generateFullReport = async (skills) => {
    try {
        const idea = await generateIdea(skills);
        const plan = await generatePlan(skills);
        const mentors = await suggestMentors(skills);

        return {
            idea: idea,
            plan: plan,
            mentors: mentors,
        };
    } catch (error) {
        console.error('Error generating full report:', error);
        throw error;
    }
};

module.exports = {
    generateIdea,
    generatePlan,
    suggestMentors,
    generateFullReport, // Export the new function
};
