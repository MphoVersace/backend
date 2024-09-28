// models/Report.js
const mongoose = require('mongoose');

const ReportSchema = new mongoose.Schema({
    user: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: false }, // Make `user` optional
    skills: { type: String, required: true },
    idea: { type: String, required: true },
    plan: { type: String, required: true },
    mentors: { type: String, required: true },
    timestamp: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Report', ReportSchema);
