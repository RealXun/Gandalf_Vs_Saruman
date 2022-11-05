# Assign the spell lists to variables
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
# We assign 0 to each variable that stores the wins
gandalfvictories=0
sarumanvictories=0
# Execution of spell shocks
for attacks in range(len(gandalf)):
    if gandalf[attacks]>saruman[attacks]:
        gandalfvictories+=1
        print ("Gandalf win.","Gandalf Attack", gandalf[attacks],"is higher than","Saruman attack",saruman[attacks])
    elif gandalf[attacks]<saruman[attacks]:
        sarumanvictories+=1
        print ("Saruman win.","Saruman attack",saruman[attacks],"is higher than","Gandalf Attack",gandalf[attacks])
    else: print ("Empate")
# We check who has won, do not forget the possibility of a tie.
# Print the result based on the winner.
print("Gandalf has won",gandalfvictories, "times")
print("Saruman has won",sarumanvictories, "times")