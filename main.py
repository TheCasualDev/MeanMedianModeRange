
# import libraries
import statistics
import colorama
import os


# main script

colorama.init()
os.system("cls") # if you are using Linux or MacOS be sure to change this to os.system("clear")

print(" ")
print(colorama.Fore.LIGHTBLUE_EX + " WELCOME TO THE SECOND BEST MEAN, MEDIAN, MODE & RANGE CALCULATOR BY JACK (⌐■_■)" + colorama.Fore.RESET)
print(" ")

def main():

    print(colorama.Fore.RESET + " Input a list of numbers to calculate the Mean, Median, Mode & Range")

    rawValues = input(" Input the values here: " + colorama.Fore.LIGHTGREEN_EX)
    valuesX = list(map(float, rawValues.split( )))


    # calculate mean, meadian & mode
    modeX = statistics.mode(valuesX)
    meanX = statistics.mean(valuesX)
    medianX = statistics.median(valuesX)

    # calculate range
    rangeX = max(valuesX) - min(valuesX) 

    print()

    print(colorama.Fore.LIGHTCYAN_EX + " The Mean is: ", meanX)
    print(colorama.Fore.LIGHTCYAN_EX + " The Median is: ", medianX)
    print(colorama.Fore.LIGHTCYAN_EX + " The Mode is: ", modeX)
    print(colorama.Fore.LIGHTYELLOW_EX + " The Range is: ", rangeX)

    print()

# restart logic

    restart = input( colorama.Fore.RESET + " Would you like to run again? [y/n] ")

    if restart == "y":
        print()
        main()

    else:
        print(colorama.Fore.LIGHTRED_EX + " Exiting...")
        exit()

main()