from main_class import Car_bot
from sys import exit

states = "Any, AL, AK, AZ, AR, CA, CO, CT, DE, DC, FL, GA, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY".split(", ")

domain = input("Enter domain: ").strip()
if domain == "":
    try:
        with open("domain.txt","r") as f:
            domain = f.read().strip()
            f.close()
    except:
        print("Incorrect domain")
        exit()
else:
    with open("domain.txt","w") as f:
        f.write(domain.strip())
        f.close()

while True:
    state = input("Enter pickup state: ").strip().upper()
    if state in states:
        break
    else:
        print(f"Enter correct states like {', '.join(states[1:7])}... !!")
print("if you want to stop typeing delivery state write exit")
d_state_list = []
while True:
    d_state = input("Enter delivery state: ").strip().upper()
    if d_state == "EXIT":
        if len(d_state_list) == 0:
            print("You must select at least one delivery state to exit")
        else:
            break
    elif d_state in states:
        if d_state not in d_state_list:
            d_state_list.append(d_state)
    else:
        print(f"Enter correct states like {', '.join(states[1:7])}... !!")



while True:
    sleep_time = input("Enter bot sleep time: ").strip()
    if sleep_time == "":
        try:
            with open("mixed_sleep.txt","r") as f:
                sleep_time = f.read().strip()
                sleep_time = float(sleep_time)
                break
        except FileNotFoundError:
            print("There is no any default sleep time please type it")
        except ValueError:
                print(f"Incorrect sleep input: '{sleep_time}' please change it")
    else:
        try:

            sleep_time = float(sleep_time)
            with open("mixed_sleep.txt","w") as f:
                f.write(str(sleep_time))
                f.close()
            break
        except ValueError:
                print(f"Incorrect sleep input: '{sleep_time}' please change it")


bot = Car_bot(domain,"mixed_database.db",sleep_time)
bot.login("username","password")
bot.select_jobs_mixed(state,d_state_list)

################### Created By JAGATA ;) ####################
