# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or 
#                  fetching data from APIs


import threading
import time

def walk_dog(first, last):
    time.sleep(10)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(4)
    print("You take out the trash")

def get_mail():
    time.sleep(6)
    print("You get the mail")

def complete_clean():
    time.sleep(2)
    print("You cleaned the all house")

def read_mail():
    time.sleep(8)
    print("You have read all mails")



chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore4 = threading.Thread(target=complete_clean)
chore4.start()

chore5 = threading.Thread(target=read_mail)
chore5.start()


# .join() ensures that all tasks are completed before proceeding
chore1.join()
chore2.join()
chore3.join()
chore4.join()
chore5.join()

print("All chores are complete!")