print("welcome to the voting machine!")

bjp_votes=0
congress_votes=0
total_voters=0

while total_voters<5:
    print("voter", total_voters + 1)
    name=input("enter your name: ")
    Id = float(input("enter your voter id: "))
    age = int(input("enter your age:"))
    
    if age<18:
        print("you can't vote. age must be 18 or older.")
        continue
    
    else:
        print("you can vote")
        print("choose your party:")
        print("1. BJP")
        print("2. Congress")
        
        party = input("enter your choice(1/2): ")
        if party == "1":
            print("you voted for the BJP. Thank you!")
            bjp_votes +=1
        elif party == "2":
            print("you voted for the congress. Thank you!")
            congress_votes += 1
        else:
            print("invalid choice. please select 1 for BJP or 2 for congress.")
            
        total_voters +=1
        
    print("\nvoting has ended!")
    print("total votes for BJP", bjp_votes)
    print("total votes for congress:", congress_votes)
    
    if bjp_votes > congress_votes:
        print("BJP is the winner!")
    elif congress_votes > bjp_votes:
        print("congress is the winner!")
    else:
        print("its's a tie!")
        
        
        
