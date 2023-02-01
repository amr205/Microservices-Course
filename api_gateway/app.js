require("./config/database").connect();
const express = require("express")
const bcrypt = require("bcryptjs")
const jwt = require("jsonwebtoken")
const axios = require("axios")

const User = require("./model/user")
const auth = require("./middleware/auth")
const httpProxy = require("express-http-proxy")

const app = express();
app.use(express.json({limit: "50mb"}))


app.post("/register", async (req, res) => {
    try {
      const { first_name, last_name, email, password, age, favorite_genres } = req.body;
      if (!(email && password && first_name && last_name && age && favorite_genres)) {
        res.status(400).send("All input is required");
      }
      const oldUser = await User.findOne({ email });
      if (oldUser) {
        return res.status(409).send("User Already Exist. Please Login");
      }

      const profile_req = await axios.post('http://profileservice:8000/profile/', {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'favorite_genres': favorite_genres
      })
  
      if(profile_req.status != 201){
        res.status(500).json({'error': 'unable to create profile'})
      }
  
      const profile_id = profile_req.data['_id']
      const encryptedPassword = await bcrypt.hash(password, 10);
      const user = await User.create({
        'first_name': first_name,
        'last_name': last_name,
        'email': email.toLowerCase(),
        'password': encryptedPassword,
        'profile_id': profile_id
      });
      const token = jwt.sign(
        { 'user_id': user._id, 'email': email, 'profile_id': profile_id },
        process.env.TOKEN_KEY,
        {
          expiresIn: "2h",
        }
      );
      user.token = token;
  
      res.status(201).json(user);
    } catch (err) {
      console.log(err);
    }
});

app.post("/login", async (req, res) => {
    try {
      const { email, password } = req.body;
      if (!(email && password)) {
        res.status(400).send("All input is required");
      }
      const user = await User.findOne({ email });
  
      if (user && (await bcrypt.compare(password, user.password))) {
        const token = jwt.sign(
          { 'user_id': user._id, 'email': email, 'profile_id': user.profile_id },
          process.env.TOKEN_KEY,
          {
            expiresIn: "2h",
          }
        );
        user.token = token;
        res.status(200).json(user);
      }
  
      res.status(400).send("Invalid Credentials");
    } catch (err) {
      console.log(err);
    }
  });


app.use("*", (req, res)=>{
    res.status(404).send("NOT FOUND")
})

module.exports = app