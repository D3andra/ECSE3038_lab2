from flask import Flask,request,jsonify
from datetime import datetime
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

temp={}
database1 = []
database2 = []
count = 0

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

#-------------------PROFILE------------------------

#CREATE---------POST/profile
@app.route("/profile",methods=["POST"])
def post_profile():
    u = request.json["username"]
    c = request.json["color"]
    r = request.json["role"]

   
    profile =  {
        "last_updated" : datetime.now(),
        "username" : u,
        "color" : c,
        "role" : r
        }
    user_object = {
        "data": profile
    }
    global temp
    temp = user_object
    database1.append(profile)
    return jsonify(temp)

#READ----------GET/profile
@app.route("/profile",methods=["GET"])
def get_profile():
    return jsonify(temp)

#UPDATE--------PATCH/profile
@app.route("/profile",methods=["PATCH"])
def patch_profile():
    if "username" in request.json:
        database1[0]["username"] = request.json["username"]
    if "col0r" in request.json:
        database1[0]["color"] = request.json["color"]
    if "role" in request.json:
        database1[0]["role"] = request.json["role"]
    database1[0]["last_updated"]= datetime.now()
    user_object = {
        "data": database1[0]
    }
    return jsonify(user_object)       


#--------------------DATA--------------------------

#READ--------GET/data
@app.route("/data",methods=["GET"])
def get_data():
    return jsonify(database2)

#CREATE-------POST/data
@app.route("/data",methods=["POST"])
def post_data():
    tl = request.json["location"]
    pf = request.json["percentage_full"]
    latitude = request.json["lat"]
    lng = request.json["long"]
    global count
    count+=1
      
    tank = {
        "id": count,
        "location" : tl,
        "percentage_full" : pf,
        "lat" : latitude,
        "long" : lng
    }

    database2.append(tank)
    return jsonify(tank)

#UPDATE----------PATCH/data/:id
@app.route("/data/<int:id>",methods=["PATCH"])
def patch_data(id):
    for tank in database2:
        if tank["id"] == id:

            if "location" in request.json:
                tank["location"] = request.json["location"]
            if "percentage_full" in request.json:
                tank["percentage_full"] = request.json["percentage_full"]
            if "lat" in request.json:
                tank["lat"] = request.json["lat"]
            if "long" in request.json:
                tank["long"] = request.json["long"]

            return jsonify(tank)       

#DELETE-------------DELETE/data/:id
@app.route("/data/<int:id>", methods =["DELETE"])
def delete_data(id):
    for i in range (len(database2)):
        if database2[i]["id"] == id:
            database2.remove(database2[i])

            return f"success : true"

if __name__ == '__main__':
    app.run(
        debug=True,
        port=3000,
        host="0.0.0.0"
    )