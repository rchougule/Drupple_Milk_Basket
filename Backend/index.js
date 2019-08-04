const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const responseBody = require('./responseBody');
const AM = require("./AM");

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.get('/city-insights', async (req, res) => {
  try {
    const cityData = await AM.cityInsights();
    const socLatLong = await AM.societyArea();
    cityData["descriptive"]["societiesLatLong"] = socLatLong;
    const response = new responseBody(200, "City Data Found", cityData);
    res.status(response.statusCode).json(response);
  } catch (e) {
    const response = new responseBody(404, e.toString());
    res.status(response.statusCode).json(response);
  }
})

app.get('/area-insights', async (req, res) => {
  try {
    const area_id = +req.query.area_id;
    const areaData = await AM.areaInsights(area_id);
    const response = new responseBody(200, "Area Data Found", areaData);
    res.status(response.statusCode).json(response);
  } catch (e) {
    const response = new responseBody(404, e.toString());
    res.status(response.statusCode).json(response);
  }
})

app.get('/user-insights', async (req, res) => {
  try {
    const customer_id = +req.query.customer_id;
    const customerData = await AM.userInsights(customer_id);
    const response = new responseBody(200, "Customer Data Found", customerData);
    res.status(response.statusCode).json(response);
  } catch (e) {
    const response = new responseBody(404, e.toString());
    res.status(response.statusCode).json(response);
  }
})

app.listen(3003, () => {
  console.info("Server started on port 3003...");
})