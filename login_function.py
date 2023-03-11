#!/usr/bin/python3

def check_authorization(agent_id, password):
    authorization_data = {'agent_1': {'password': '#p@sswd1', 'plot': 'ALU park, Plot J'},
             'agent_2': {'password': '#p@sswd2', 'plot': 'Kigali park,Plot I'},
             'agent_3': {'password': '#p@sswd3', 'plot': 'ALU park,Plot D'},
             'agent_4': {'password': '#p@sswd4', 'plot': 'Kigali park,Plot F'},
             'agent_5': {'password': '#p@sswd5', 'plot': 'ALU park,Plot G'},
             'agent_6': {'password': '#p@sswd6', 'plot': 'Uganda park,Plot E'},
             'agent_7': {'password': '#p@sswd7', 'plot': 'Nigeria park,Plot C'},
             'agent_8': {'password': '#p@sswd8', 'plot': 'ALU park,Plot B'},
             'agent_9': {'password': '#p@sswd9', 'plot': 'Kampala park,Plot H'},
             'agent_10': {'password': '#p@sswd10', 'plot': 'ALU park,Plot A'}}
    agent_id = agent_id.lower()
    password = password.lower()
    if agent_id in authorization_data:
        if password == authorization_data[agent_id]['password']:
            return authorization_data[agent_id]
    return False

while True:
    agent_id = input("Enter Agent ID: ").lower()
    password = input("Enter Agent password: ").lower()
    if check_authorization(agent_id, password):
        print("Login successful!")
        print("Your allocated plot is:", check_authorization(agent_id, password)['plot'])
        break
    else:
        print("Login unsuccessful. Please try again.")
