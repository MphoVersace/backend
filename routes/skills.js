// routes/skills.js

const express = require("express");
const router = express.Router();

let skills = []; // In-memory array, replace this with a database connection (e.g., MongoDB)

// GET /api/skills - Retrieve all skills
router.get("/", (req, res) => {
  res.json(skills);
});

// POST /api/skills - Add a new skill
router.post("/", (req, res) => {
  const { skill } = req.body;
  if (skill && skill.trim() !== "") {
    skills.push(skill);
    res.status(201).json({ message: "Skill added successfully", skills });
  } else {
    res.status(400).json({ message: "Skill is required" });
  }
});

// DELETE /api/skills/:index - Remove a skill by index
router.delete("/:index", (req, res) => {
  const index = parseInt(req.params.index, 10);
  if (index >= 0 && index < skills.length) {
    skills.splice(index, 1);
    res.status(200).json({ message: "Skill removed successfully", skills });
  } else {
    res.status(400).json({ message: "Invalid index" });
  }
});

module.exports = router;
