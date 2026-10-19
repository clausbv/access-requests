from flask import Flask, jsonify, request



access_requests = [
    {
        "user": "Ana",
        "application": "Slack",
        "status": "pending",
    },
    {
        "user": "Jon",
        "application": "Salesforce",
        "status": "pending",
    },
]


app = Flask(__name__)

@app.route("/requests", methods=["GET"])
def get_requests():
    return jsonify(access_requests)

@app.route("/requests", methods=["POST"])
def post_requests():

    

    data =request.get_json()

    if not data.get("user") or not data.get("application"):
        return jsonify({"error": "Both user and application are required"}), 400

    

    user = data.get("user")
    application = data.get("application")
    #prevent duplication
    
        
        

    new_dict = {
        "user": data["user"],
        "application": data["application"],
        "status": "pending",
    }

    for existing_request in access_requests:
        if existing_request["user"] == user and existing_request["application"] == application:
            return jsonify({"error": "Duplicate request"}), 409
    
    access_requests.append(new_dict)

    return jsonify(new_dict), 201

@app.route("/requests/<user_name>", methods=["PATCH"])
def change_status(user_name):

    data = request.get_json()


    if not isinstance(data, dict):
        return jsonify({"error": "JSON body mu be and object"}), 400
    
    new_status = data.get("status")

    for request_item in access_requests:
        if request_item["user"] == user_name:
            if request_item["status"] != "pending":
                return jsonify({"error": "Request has already been processed"}), 400

            request_item["status"] = new_status 
            return jsonify(request_item), 200   

    if new_status not in ["approved", "rejected", "pending"]:
        return jsonify({"error": "status must be approved or rejected"}), 400

    return jsonify("new_status"), 201

if __name__ == "__main__":
    app.run(debug=True)




def filter_requests(requests, wanted_status):
    matches = []

    for request in requests:
        if request["status"] == wanted_status:
            matches.append(request)

    return matches


def get_application(request):
    return request["application"]


def get_status(request):
    return request["status"]


def find_request(requests, user_name):
    for request in requests:
        if request["user"] == user_name:
            return request

    return None


def get_users_by_application(requests, application_name):
    users = []

    for request in requests:
        if request["application"] == application_name:
            users.append(request["user"])

    return users


def get_users_by_status(requests, wanted_status):
    users = []

    for request in requests:
        if request["status"] == wanted_status:
            users.append(request["user"])

    return users


def find_request_by_status(requests, wanted_status):
    matching_requests = []

    for request in requests:
        if request["status"] == wanted_status:
            matching_requests.append(request)

    return matching_requests


def count_by_status(requests):
    counts = {}

    for request in requests:
        status = request["status"]

        if status in counts:
            counts[status] += 1
        else:
            counts[status] = 1

    return counts


# 3. Funcții pentru crearea și procesarea solicitărilor
def create_request(user, application):
    return {
        "user": user,
        "application": application,
        "status": "pending",
    }


def add_request(new_request, requests):
    access_requests.append(new_request)
    return access_requests

# neww_request = add_request("vasile", "slack")
# print(neww_request)

new_request = create_request("Alex", "zoom")
add_request(new_request, access_requests)
print(access_requests)


def process_user_request(requests, user_name, new_status):
    found_request = find_request(requests, user_name)

    if found_request is None:
        return "Access request not found"

    return process_request(found_request, new_status)