from prm_database import mycursor


allocated = []
database = mycursor.fetchall()

def check_login(agent_id, password):
    new = database
    for i in new:
        if agent_id in i and password in i:
            allocated.append(i[2])
            return True


print('WELCOME TO PRM SYSTEM!')
print("LOG IN HERE")
while True:
    id = input("Enter Agent ID:")
    pword = input("Enter Agent password:")
    check_login(id, pword)
    if check_login(id, pword):
        print("Login successful!")
        print("Your allocated plot is:", allocated[0])
        break
    else:
        allocated = []
        print("Login unsuccessful.")
        question = input("Do you want to try again? [y/n]: ")
        if question == 'y':
            continue
        elif question == 'n':
            print("Thank you, goodbye")
            quit()
        else:
            print("Incorrect input.")
            quit()