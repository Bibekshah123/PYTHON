# lab3.2 sub.ex

def get_next_point(step):
    x = int(input(f"Input x{step} coordinates: "))
    y = int(input(f"Input y{step} coordinates: "))
    return(x,y) #sending back x and y

def cal_distance(p1,p2):
    distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    distance = distance**(1/2)
    return distance

def main():
    print ("___Robot Program___")

    running = True #For inifite running code
    step = [(0,0)] # stores co-ordinate
    iter = 1
    printer = 1
    distance = [] #stores distance data
    
    while running:
        p1 = get_next_point(iter)
        step.append(p1)
        iter += 1
        if p1 == (999,999):
            running = False
            len_of_cal = len(step) #Function to find out the lenght of the step list which has stored co-ordinates
            for i in range(((int(len_of_cal/2))+1)):
                distance.append(cal_distance(step[i], step[i+1]))
            print("-"*10)
            for number in distance:
                print("Step {}: {:.2f} units".format(printer, number))
                printer += 1
            print("_"*10)
            
if __name__ == "__main__":
    main()