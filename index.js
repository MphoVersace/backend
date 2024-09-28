// index.js
const express = require('express');
const connectDB = require('./config/db');
const dotenv = require('dotenv');
const session = require('express-session');
const authRoutes = require('./routes/auth');
const cors = require('cors'); 
const { generateFullReport } = require('./flaskApi'); // Import the new function
const Report = require('./models/Report');


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
  const { skills, userId } = req.body; // Assume `userId` is passed from the frontend

  try {
      // Generate the full report
      const reportData = await generateFullReport(skills);
      
      // Extract the specific string data from the report
      const idea = reportData.idea.toString();
      const plan = reportData.plan.toString();
      const mentors = reportData.mentors.toString();
      
      // Create a new report document
      const newReport = new Report({
          user: userId, // Use the user ID passed from the frontend
          skills: skills,
          idea: idea, // Store as a string
          plan: plan, // Store as a string
          mentors: mentors // Store as a string
      });

      // Save the report to the database
      await newReport.save();

      // Return the generated report as a response
      res.json(reportData);
  } catch (error) {
      console.error('Error generating and saving report:', error);
      res.status(500).send('Error generating full report.');
  }
});
// Set the port from environment variables or default to 5001
const PORT = process.env.PORT || 5001;

// Start the server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
