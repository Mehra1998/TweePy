import win_unicode_console , colorama
import os , sys , subprocess , shutil , time

width = os.get_terminal_size().columns

# Windows deserves coloring too :D
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\33[97m'  # white

def banner():
    print("""%s
                ___________                       __________         
                \__    ___/__  _  __  ____   ____ \______   \ ___.__.
                  |    |   \ \/ \/ /_/ __ \_/ __ \ |     ___/<   |  |
                  |    |    \     / \  ___/\  ___/ |    |     \___  |
                  |____|     \/\_/   \___  >\___  >|____|     / ____|
                                         \/     \/            \/      %sv1.0%s
                                            # Coded By Sahil Mehra
    """ % (G, W, Y))

def interface():
    subprocess.call("clear")
    print("%s-" % (R) * width)
    banner()
    print("%s-"%(R) * width)

    mode = input("""%s\nSearching the Tweets...\n
	%s\t1.) Text View
	\t2.) Graphical View
	\t3.) Delete History.
	\t4.) Exit
	\n%s[+] Enter Your Choice :- """%(Y,B,W))
    return mode

def function():
    from modules import textview

def Visualization():
    from modules import graphicalview

def delete():
    d = os.getcwd() + "/history/"
    shutil.rmtree(d)

def exit():
    import sys
    def Exit():
        sys.exit()

    exit = input("\n[+] Do You Want To Quit ? (Y/N)\n\t:- ")
    if exit == 'Y' or exit == 'y':
        Exit()
    elif exit == 'n' or 'N':
        main()
    else:
        print("\t--> Wrong Choice.!")

#The main routine
def main():
    try:
        chosen_option = interface()

        if chosen_option == '1':
            function()
            time.sleep(2)

        elif chosen_option == '2':
            Visualization()
            time.sleep(2)

        elif chosen_option == '3':
            delete()
            print("%s\n\t...History Deleted...\n" % (R))
            time.sleep(2)

        elif chosen_option == '4':
            exit()

        else:
            print("Wrong Choice.!")

    except Exception as err:
        print("%s\n[+] Sorry You Don't Have Any History." % (R))
        time.sleep(2)
        main()
try:
    while True:
        main()
except Exception as err:
    d = err
    print('%sNo Internet Connection.!' % (R))
