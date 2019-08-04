## HOW TO INSTALL
1. npm start
2. Server will begin on http://localhost:3003
   1. GET /city-insights
      1. Fetches the predictive and declarative insights of a specific city
   2. GET /area-insights
      1. Fetches the predictive and declarative insights of an area.
      2. Query string "area_id" : [0..13]
   3. GET /user-insights
      1. Fetches the predictive and declarative insights of a customer
      2. Query string "customer_id" : 23166080