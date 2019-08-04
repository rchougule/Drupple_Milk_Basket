const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'milk';

const cityInsights = () => {
  return new Promise((resolve, reject) => {
    MongoClient.connect(url, {useNewUrlParser: true},  async (err, client) => {
      if (err) reject(err);
      const DB = client.db(dbName);
      const city = DB.collection("city");
      const cityData = await city.findOne({}, {fields: {_id: 0}});
      if (cityData) {
        resolve(cityData);
      } else {
        reject("No Data Found");
      }
    })
  })
}

const areaInsights = (area_id) => {
  return new Promise((resolve, reject) => {
    MongoClient.connect(url, {useNewUrlParser: true},  async (err, client) => {
      if (err) reject(err);
      const DB = client.db(dbName);
      const area = DB.collection("area");
      const areaData = await area.findOne({area_id: area_id}, {fields: {_id: 0}});
      if (areaData) resolve(areaData);
      reject("No Area Data Found")
    })
  })
}

const societyArea = () => {
  return new Promise((resolve, reject) => {
    MongoClient.connect(url, {useNewUrlParser: true},  async (err, client) => {
      if (err) reject(err);
      const DB = client.db(dbName);
      const soc = DB.collection("societies_latlong");
      soc.find({}, {fields: {_id: 0}}).toArray((err, result) => {
        let latLongSoc = [];
        result.reduce((a, b) => {
          latLongSoc.push([b["society_id"], b.location["lat"], b.location["long"]]);
          return latLongSoc;
        }, [])
        resolve(latLongSoc)
      })
    })
  })
}

const userInsights = (customer_id) => {
  return new Promise((resolve, reject) => {
    MongoClient.connect(url, {useNewUrlParser: true},  async (err, client) => {
      if (err) reject(err);
      const DB = client.db(dbName);
      const user = DB.collection("user");
      const userData = await user.findOne({customer_id}, {fields: {_id: 0}});
      if (userData) resolve(userData);
      reject("No User Data Found")
    })
  })
}

societyArea()

module.exports = {
  cityInsights,
  societyArea,
  areaInsights,
  userInsights
}