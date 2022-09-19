# Gandalf Vs Saruman
### An epic battle between two powerful wizards!!!!
![](https://github.com/RealXun/Gandalf_Vs_Saruman/blob/main/Gandalf%20y%20Saruman/Cover.jpg)

You are witnessing an epic battle between two powerful wizards: Gandalf and Saruman. Each mage has 10 spells of varying power in his mind and they are going to cast them one after another. The winner of the duel will be the one who wins the most of those clashes between spells. Spells are represented as a list of 10 integers whose value equals the power of the spell.
```
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
```
For example:
1. The first clash is won by Saruman: 10 against 23, wins on 23
2. The second clash wins Saruman: 11 against 66, wins the 66
3.etc

We are going to create two variables, one for each wizard, where the sum of spell hits won will be stored. Depending on which variable is greater at the end of the duel, you will display one of the following three results on the screen:
* Gandalf wins
*saruman wins
* Tie

### Solution
```
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
gandalfvictories=0
sarumanvictories=0
for attacks in range(len(gandalf)):
    if gandalf[attacks]>saruman[attacks]:
        gandalfvictories+=1
        print ("Gandalf win.","Gandalf Attack", gandalf[attacks],"is higher than","Saruman attack",saruman[attacks])
    elif gandalf[attacks]<saruman[attacks]:
        sarumanvictories+=1
        print ("Saruman win.","Saruman attack",saruman[attacks],"is higher than","Gandalf Attack",gandalf[attacks])
    else: print ("Empate")
print("Gandalf has won",gandalfvictories, "times")
print("Saruman has won",sarumanvictories, "times")
```
### Example of the result
```
Saruman win. Saruman attack 23 is higher than Gandalf Attack 10
Saruman win. Saruman attack 66 is higher than Gandalf Attack 11
Gandalf win. Gandalf Attack 13 is higher than Saruman attack 12
Saruman win. Saruman attack 43 is higher than Gandalf Attack 30
Gandalf win. Gandalf Attack 22 is higher than Saruman attack 12
Gandalf win. Gandalf Attack 11 is higher than Saruman attack 10
Saruman win. Saruman attack 44 is higher than Gandalf Attack 10
Gandalf win. Gandalf Attack 33 is higher than Saruman attack 23
Gandalf win. Gandalf Attack 22 is higher than Saruman attack 12
Gandalf win. Gandalf Attack 22 is higher than Saruman attack 17
Gandalf has won 6 times
Saruman has won 4 times
```
