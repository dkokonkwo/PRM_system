from prm_database import mycursor


allocated = []
def check_login(agent_id, password):
    agent_id = agent_id.lower()
    password = password.lower()
    for agent in mycursor.fetchall():
        if agent_id in agent and password in agent:
            allocated.append(agent[2])
    return allocated


if __name__ == "__main__":
    print("WELCOME TO PRM SYSTEM")
    while allocated == []:
        agent_id = input("Enter Agent ID: ").lower()
        password = input("Enter Agent password: ").lower()
        check_login(agent_id, password)
        print(agent_id, password, allocated)
        if allocated != []:
            print("Login successful!")
            print("Your allocated plot is:", allocated[0])
            break
        else:
            agent_id = ''
            password = ''
            print("Login unsuccessful. Please try again.")
