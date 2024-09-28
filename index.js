// index.js
const express = require('express');
const connectDB = require('./config/db');
const dotenv = require('dotenv');
const session = require('express-session');
const authRoutes = require('./routes/auth');
const cors = require('cors'); 
const { generateFullReport } = require('./flaskApi'); // Import the new function

dotenv.config();

const app = express();

// Connect to MongoDB
connectDB();

// Middleware for parsing JSON bodies
app.use(express.json());

// Enable CORS for all requests
app.use(cors());

// Session management
app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: true,
  })
);

// Routes for authentication
app.use('/api/auth', authRoutes);

// New route to get the full report (idea, plan, mentors)
app.post('/api/generate-full-report', async (req, res) => {
    const { skills } = req.body;
    try {
        const report = await generateFullReport(skills);
        res.json(report);
    } catch (error) {
        res.status(500).send('Error generating full report.');
    }
});

// Set the port from environment variables or default to 5001
const PORT = process.env.PORT || 5001;

// Start the server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
