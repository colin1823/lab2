def display_main_menu():
    print ("Enter the temperatures: ")
    return

def get_user_input():
    
    x = input()

    txt = x.split(",")
    txt2 = txt
    for x in range(len(txt)):
        txt2[x] = float(txt[x])
    print(txt2)
    return txt2
def get_avg_temp(txt2):
    sum_total = sum(txt2)
    total = len(txt2)
    average = sum_total / total 
    print ( "the average temperature is : " + str(average) )
    return average
def min_max (x):
    x.sort()
    print ("min temp is " + str(x[0]) )
    print ("max temp is " + str(x[-1]))
    return x
def find_median(x):
    x.sort()
    if len(x) % 2 == 0:
        median = (x[len(x)//2] + x[len(x)//2 - 1]) / 2
    else:
        median = x[len(x)//2]
    print ("median is " + str(median))
    return 

def main():
    display_main_menu()
    temps = get_user_input()
    get_avg_temp(temps)
    min_max(temps)
    find_median(temps)
    
if __name__ == "__main__":
    main()