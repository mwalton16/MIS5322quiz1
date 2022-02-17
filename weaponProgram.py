import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
unoriginal_name = open('weapons.csv','r')


# create a csv object from the file object
weapons_file = csv.reader(unoriginal_name, delimiter = ',')


#skip the header row
next(weapons_file)



#create an empty dictionary named 'weapons_dict'
weapons_dict={}



#use a for loop to iterate through every row of the csv file
for i in weapons_file:
    #use variables for name,speed and range (optional)
    name = i[0]
    speed = i[1]
    range = i[2]
    name_i = str(name)
    name_i = w.Weapon(name,speed,range)
    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
  

    # append the name and bullet count to 'weapons_dict'
    weapons_dict[name_i] = name_i.get_bullets()


    # print out the name of the weapon using the appropriate method of the object 
    print("Gun: "+name_i.get_name())

    # print out the speed of the weapon using the appropriate method of the object
    print("Speed: "+name_i.get_speed())
    # print out the range of the weapon using the appropriate method of the object
    print("Range: "+name_i.get_range())
    # print out the number of bullets of the weapon using the appropriate method of the object
    print("Bullet Count: "+str(name_i.get_bullets()))

    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    while name_i.get_bullets() > 0:
        name_i.fire_bullet()
    

    # use an appropriate loop to keep firing the weapon until all bullets run out
    
        # call the appropriate method to fire a bullet
       
        # print out the bullet count every time the weapon is fired
        

    


#using a loop print out the name and number of bullets from the dictionary
for i in weapons_dict:
    print("Gun: "+str(i)+"\n"+"Bullet Count: "+str(weapons_dict[i]))




    


    



