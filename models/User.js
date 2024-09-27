// models/User.js
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

// User schema definition
const UserSchema = new mongoose.Schema({
  firstName: {
    type: String,
    required: true,
  },
  middleName: {
    type: String,
  },
  lastName: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
  gender: {
    type: String,
    enum: ['female', 'male', 'non-binary'],
  },
  dateOfBirth: {
    month: {
      type: String,
      required: true,
    },
    date: {
      type: Number,
      required: true,
    },
    year: {
      type: Number,
      required: true,
    },
  },
  countryOfResidence: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    enum: ['mentor', 'youth'],
    required: true,
  },
});

// Hash password before saving to the database
UserSchema.pre('save', async function (next) {
  if (!this.isModified('password')) return next(); // Skip if the password is not modified

  // Generate salt and hash the password
  const salt = await bcrypt.genSalt(10);
  this.password = await bcrypt.hash(this.password, salt);
  next();
});

module.exports = mongoose.model('User', UserSchema);
