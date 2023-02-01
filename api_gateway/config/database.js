const mongoose = require("mongoose")

const { MONGO_URI } = process.env

exports.connect = () => {
    console.log(MONGO_URI)

    mongoose.connect(MONGO_URI, {
        useNewUrlParser: true
    }).then(()=>{
        console.log("conectado a la bdd")
    }).catch((error)=>{
        console.error(error)
        process.exit(1)
    })

}