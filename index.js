const express = require("express");
const connectDB = require("./config/db");
const dotenv = require("dotenv");
const session = require("express-session");
const authRoutes = require("./routes/auth");
const skillsRoutes = require("./routes/skills");
const cors = require("cors");

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
app.use("/api/auth", authRoutes);

// Routes for skills
app.use("/api/skills", skillsRoutes); // Add skills route

// Set the port from environment variables or default to 5000
const PORT = process.env.PORT || 5001;

// Start the server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
