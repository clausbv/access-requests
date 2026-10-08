access_requests = [  {
        "user": "Ana",
        "application": "Slack",
        "status": "rejected"
    },
    {
        "user": "Jon",
        "application": "Salesforce",
        "status": "pending"
    }
]

# if access_request["status"] == "pending":
# 


for access_request in access_requests:
    if access_request["status"] == "pending":
        access_request["status"] = "approved"


for access_request in access_requests:
    print(access_request["user"], access_request["status"])



for access_request in access_requests:
    if access_request["status"] == "pending":
        print(access_request["user"])

for access_request in access_requests:
    if access_request["status"] == "approved":
        print(access_request["application"])        

# if access_request["status"] == "pending":
#     access_request["status"] = "approved"
# else:
#     print("Solicitarea a fost deja procesata") 
    

# print(access_request["status"])
