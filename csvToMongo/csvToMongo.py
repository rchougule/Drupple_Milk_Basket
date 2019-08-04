import csv
import os
import ast
import random

from pymongo import MongoClient
client = MongoClient()
DB = client.milk

fileNames = ["user.csv"]

podOne = {
  "lat": 18.485728,
  "long": 73.802289
}
podTwo = {
  "lat": 18.681886,
  "long": 73.725115
}
podThree = {
  "lat": 18.670743,
  "long": 73.828048
}
defaultWarehouse = {
  "lat": 18.676853,
  "long": 73.897229
}

productIds = []

with open("product_ids.csv", mode='r') as csvFile:
  readerFile = csv.DictReader(csvFile)
  for row in readerFile:
    productIds.append(int(row["product_id"]))

for filename in fileNames:
  with open(filename, mode='r') as csvFile:
    readerFile = csv.DictReader(csvFile)
    collectionName = filename.split(".")[0]
    collection = DB[collectionName]
    collection.drop()
    for row in readerFile:
      if filename == "city.csv":
        daysOfWeek = ast.literal_eval(row["day_of_week_graph"])
        weeksOfMonth = ast.literal_eval(row["week_of_month_graph"])
        rowToInsert = {
          "descriptive": {
            "noOfUsers": int(row["num_users"]),
            "avgOrdersPerDay": float(row["avg_order_per_day"]),
            "avgValuePerDay": float(row["avg_value_per_day"]),
            "meanOrderCost": float(row["mean_order_cost"]),
            "noOfWarehouses": int(row["number_of_warehouses"]),
            "maxDistanceFromWarehouse": float(row["max_distance_from_warehouse"]),
            "warehouseLocation": {
              "lat": float(row["warehouse_lat"]),
              "long": float(row["warehouse_long"])
            },
            "dayOfWeekGraph": {
              "sunday": daysOfWeek[0],
              "monday": daysOfWeek[1],
              "tuesday": daysOfWeek[2],
              "wednesday": daysOfWeek[3],
              "thursday": daysOfWeek[4],
              "friday": daysOfWeek[5],
              "saturday": daysOfWeek[6]
            },
            "weekOfMonthGraph": {
              "week-1": weeksOfMonth[0],
              "week-2": weeksOfMonth[1],
              "week-3": weeksOfMonth[2],
              "week-4": weeksOfMonth[3],
              "week-5": weeksOfMonth[4]
            },
            "areaCenters": [[18.464815, 73.796439], [18.507762, 73.798775], [18.52517, 73.779009], [18.56792, 73.770989], [18.556043, 73.812341], [18.683466, 73.731081], [18.665461, 73.808566], [18.565205, 73.911494], [18.529224, 73.860415], [18.435227, 73.889246], [18.50861, 73.934341], [18.635565, 73.843959], [18.606168, 73.874991], [18.599301, 73.927049]]
          },
          "predictive": {
            "valueTomorrow": float(row["predicted_value"]),
            "pods": [{
              "lat": float(row["pod1_lat"]),
              "long": float(row["pod1_long"])
            }, {
              "lat": float(row["pod2_lat"]),
              "long": float(row["pod2_long"])
            },{
              "lat": float(row["pod3_lat"]),
              "long": float(row["pod3_long"])
            }],
            "newMaxDistanceFromWarehouse": float(row["predicted_distance"])
          }
        }
      elif filename == "area.csv":
        daysOfWeek = ast.literal_eval(row["day_of_week_graph"])
        weeksOfMonth = ast.literal_eval(row["week_of_month_graph"])
        top5Brands = ast.literal_eval(row["top_5_brands"])
        top5Products = ast.literal_eval(row["top_5_products"])
        top5ProductsEstimatedSale = ast.literal_eval(row["estimated_quantity_of_sale"])
        if row["closest_pod_or_warehouse"] == "pod1":
          podLocation = podOne
        elif row["closest_pod_or_warehouse"] == "pod2":
          podLocation = podTwo
        elif row["closest_pod_or_warehouse"] == "pod3":
          podLocation = podThree
        else:
          podLocation = defaultWarehouse
        rowToInsert = {
          "area_id": int(row["area_id"]),
          "descriptive": {
            "avgOrdersPerDay": float(row["avg_order_per_day"]),
            "avgValuePerDay": float(row["avg_value_per_day"]),
            "meanOrderCost": float(row["mean_order_cost"]),
            "noOfUsers": int(row["num_users"]),
            "noOfSocieties": int(row["num_societies"]),
            "quintile": int(float(row["quintile"])),
            "location": {
              "lat": float(row["lat"]),
              "long": float(row["long"])
            },
            "dayOfWeekGraph": {
              "sunday": daysOfWeek[0],
              "monday": daysOfWeek[1],
              "tuesday": daysOfWeek[2],
              "wednesday": daysOfWeek[3],
              "thursday": daysOfWeek[4],
              "friday": daysOfWeek[5],
              "saturday": daysOfWeek[6]
            },
            "weekOfMonthGraph": {
              "week-1": weeksOfMonth[0],
              "week-2": weeksOfMonth[1],
              "week-3": weeksOfMonth[2],
              "week-4": weeksOfMonth[3],
              "week-5": weeksOfMonth[4]
            },
            "top5Brands": top5Brands,
            "top5Products": top5Products,
            "distanceFromOriginalWarehouse": float(row["distance_from_ware_house"])
          },
          "predictive": {
            "nearestWarehouseDistance": float(row["distance_from_pod_if_made"]),
            "top5ProductsEstimatedSaleUpcomingWeek": top5ProductsEstimatedSale,
            "warehouseLocation": podLocation
          }
        }
      elif filename == "societies_latlong.csv":
        rowToInsert = {
          "society_id": int(row["society_id"]),
          "area_id": int(row["area"]),
          "location": {
            "lat": float(row["lat"]),
            "long": float(row["long"])
          }
        }
      elif filename == "user.csv":
        top5Products = ast.literal_eval(row["top_5_products"])
        recommendedProducts = []
        for i in range(random.randrange(3,6)):
          recommendedProducts.append(productIds[int(random.random()*5200)])
        rowToInsert = {
          "customer_id": int(row["customer_id"]),
          "descriptive": {
            "avgOrdersPerDay": float(row["avg_order_per_day"]),
            "avgSpendPerDay": float(row["avg_spend_per_day"]),
            "favouriteBrand": int(row["favourite_brand"]),
            "frequentHourSlot": int(row["frequent_hour_slot"]),
            "meanOrderCost": float(row["mean_order_cost"]),
            "totalUniqueProducts": int(row["num_products"]),
            "productCategory": int(row["product_category"]),
            "quintile": int(float(row["quintile"])),
            "subscription": bool(row["subscription"]),
            "topProducts": top5Products
          },
          "predictive": {
            "recommendedProducts": recommendedProducts
          }
        }
      elif filename == "alldata.csv":
        rowToInsert = row
      collection.insert_one(rowToInsert)

