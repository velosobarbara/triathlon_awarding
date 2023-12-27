"""
this program determines an award for triathlon athletes.
convert input to integer: run, cycle, bike
store all activities into a variable converted into an integer
- if <100 print out 'Provincial Colours'
- if >100 and <105 print out 'Provincial Half Colours'
- if >105 and <110 print out 'Provincial Scroll'
- else: print out 'No Award'
"""

run_time = int(input("Please enter your finishing time in running: "))
cycle_time = int(input("Please enter your finishing time in cycling: "))
swim_time = int(input("Please enter your finishing time in swimming: "))
total = int((run_time) + (cycle_time) + (swim_time))

if total <=100:
    print("Your total time to complete the triathlon is: " + str(total), "minutes.")
    print("Award Won: Provincial Colours")
    
elif total >100 and total <=105:
    print("Your total time to complete the triathlon is: " + str(total), "minutes.")
    print("Award Won: Provincial Half Colours")
    
elif total >106 and total <=110:
    print("Your total time to complete the triathlon is: " + str(total), "minutes.")
    print("Award Won: Provincial Scroll")
    
else:
    print("Your total time to complete the triathlon is: " + str(total), "minutes.")
    print("No Award Won")