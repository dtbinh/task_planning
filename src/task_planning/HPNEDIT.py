from Fluents import Fluents
import time

def HPN():
        if goal.In(a,object_loc) is True:
                print "Robot is in storage!!"
                time.sleep(5)
        print "\nRobot should be in [3,5] \n"
        print "checking condition for clean...\n\n"
        if goal.wash(a) == 1:
                time.sleep(5)
                print("A is clean!!")
        else:
                T = goal.place(a,washer_loc)
                #print("\nplacing the object")
                time.sleep(5)
                                
                goal.Pick(a,object_loc)
                print("\n Robot is picking up the object")
                time.sleep(5)
        print "\n\nSUCCESSFULLY PLACED"        
                

def print_board():
        for row in grid:
                print "  ".join(row)
                        
def main():
        
        for row in range(7):
                grid.append([])  
                for col in range(7):
                        if row == 1 and col == 1:
                                grid[row].append('\033[91mO\033[0m')
                               
                        elif row == 5 and col == 5:
                                grid[row].append('\033[94mW\033[0m') 
                               
                        elif row == 3 and col == 5:
                                grid[row].append('\033[93mS\033[0m') 
                                
                        elif row == 6 and col ==0:
                                grid[row].append('\033[92mR\033[0m')                       
                        else:
                                grid[row].append('x')                        
        
        print_board()   
        HPN()                
 
if __name__ == "__main__":
        grid = []
        a = "robot"
        object_loc = [1,1]
        washer_loc = [5,5]
        storage_loc = [3,5]
        robot_loc = [6,0]
        goal = Fluents()
        main()
