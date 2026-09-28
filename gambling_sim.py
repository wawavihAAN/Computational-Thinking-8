print("WELCOME TO THE GAMBLING SIM! (PRESS ENTER TO CONTINUE)")
input()
print("RULES:")
print("1: This is a number game. You must pick a number from one to 100. You have a starting money of $10,000. You can bet any amount of money on a number. There will be a range of 50 numbers on the first round. Every round, the range will decrease by 10. For example, First round: range of 50. Second round: range of 40, ...")
print("2: The last round will be with a range of 10.")
print("LETS START!")
total = 10000
bet1 = int(input("Make a bet. (ONLY ENTER A NUMBER) "))
round1 = int(input("Pick a number from 1 -  100 "))
if 20 <= round1 <= 70:
    print(f"You gain ${bet1}. Your new total money is {total + bet1}. ")
    bet2 = int(input("Make a bet. "))
    round2 = int(input("Pick a number from 1 - 100 "))
    if 58 <= round2 <= 98:
        print(f"You gain ${bet2}. Your new total money is {total + bet2 + bet1}")
        bet3 = int(input("Make a bet. "))
        round3 = int(input("Pick a number from 1 - 100 "))
        if 12 <= round3 <= 42:
            print(f"You gain ${bet3}. Your new total money is {total + bet1 + bet2 + bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total +bet1 + bet2 + bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 + bet2 + bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 + bet2 + bet3 + bet4 - bet5}")
            else:
                print(f"You lose${bet4}. Your new total money is {total + bet1 +bet2 + bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 + bet2 + bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 + bet2 + bet3 - bet4 - bet5}")
        else:
            print(f"You lose ${bet3}. Your new total money is {total +bet1 + bet2 - bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total + bet1 + bet2 - bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 + bet2 - bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 + bet2 - bet3 + bet4 - bet5}")
            else:
                print(f"You lose${bet4}. Your new total money is {total + bet1 +bet2 - bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 + bet2 - bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 + bet2 - bet3 - bet4 - bet5}")
    else:
        print(f"You lose ${bet2}. You new total money is {total + bet1 - bet2}")
        bet3 = int(input("Make a bet. "))
        round3 = int(input("Pick a number from 1 - 100 "))
        if 12 <= round3 <= 42:
            print(f"You gain ${bet3}. Your new total money is {total + bet1 - bet2 + bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total +bet1 - bet2 + bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 - bet2 + bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 - bet2 + bet3 + bet4 - bet5}")
            else:
                print(f"You lose ${bet4}. Your new total money is {total + bet1 - bet2 + bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 - bet2 + bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 - bet2 + bet3 - bet4 - bet5}")
        else:
            print(f"You lose ${bet3}. Your new total money is {total + bet1 - bet2 - bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total + bet1 - bet2 - bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 - bet2 - bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 - bet2 - bet3 + bet4 - bet5}")
            else:
                print(f"You lose ${bet4}. You new total money is {total + bet1 - bet2 - bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total + bet1 - bet2 - bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total + bet1 - bet2 - bet3 - bet4 - bet5}")
else:
    print(f"You lose ${bet1}. Your new total money is {total - bet1}. ")
    bet2 = int(input("Make a bet. "))
    round2 = int(input("Pick a number from 1 - 100 "))
    if 58 <= round2 <= 98:
        print(f"You gain ${bet2}. Your new total money is {total + bet2 - bet1}")
        bet3 = int(input("Make a bet. "))
        round3 = int(input("Pick a number from 1 - 100 "))
        if 12 <= round3 <= 42:
            print(f"You gain ${bet3}. Your new total money is {total - bet1 + bet2 + bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total - bet1 + bet2 + bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 + bet2 + bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 + bet2 + bet3 + bet4 - bet5}")
            else:
                print(f"You lose ${bet4}. You new total money is {total - bet1 + bet2 + bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 + bet2 + bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 + bet2 + bet3 - bet4 - bet5}")
        else:
            print(f"You lose ${bet3}. Your new total money is {total - bet1 + bet2 - bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total - bet1 + bet2 - bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 + bet2 - bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 + bet2 - bet3 + bet4 - bet5}")

            else:
                print(f"You lose ${bet4}. You new total money is {total - bet1 + bet2 - bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 + bet2 - bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 + bet2 - bet3 - bet4 - bet5}")
    else:
        print(f"You lose ${bet2}. You new total money is {total - bet1 - bet2}")
        bet3 = int(input("Make a bet. "))
        round3 = int(input("Pick a number from 1 - 100 "))
        if 12 <= round3 <= 42:
            print(f"You gain ${bet3}. Your new total money is {total - bet1 - bet2 + bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total - bet1 - bet2 + bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 - bet2 + bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 - bet2 + bet3 + bet4 - bet5}")
            else:
                print(f"You lose ${bet4}. You new total money is {total - bet1 - bet2 + bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 - bet2 + bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 - bet2 + bet3 - bet4 - bet5}")
        else:
            print(f"You lose ${bet3}. Your new total money is {total - bet1 - bet2 - bet3}")
            bet4 = int(input("Make a bet. "))
            round4 = int(input("Pick a number from 1 - 100 "))
            if 31 <= round4 <= 51:
                print(f"You gain ${bet4}. Your new total money is {total - bet1 - bet2 - bet3 + bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 - bet2 - bet3 + bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 - bet2 - bet3 + bet4 - bet5}")
            else:
                print(f"You lose ${bet4}. You new total money is {total - bet1 - bet2 - bet3 - bet4}")
                bet5 = int(input("Make a bet. "))
                round5 = int(input("Pick a number from 1 - 100 "))
                if 56 <= round5 <= 66:
                    print(f"You gain ${bet5}. Your new total money is {total - bet1 - bet2 - bet3 - bet4 + bet5}")
                else:
                    print(f"You lose ${bet5}. Your new total money is {total - bet1 - bet2 - bet3 - bet4 - bet5}")