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



app.use("*", (req, res)=>{
    res.status(404).send("NOT FOUND")
})

module.exports = app