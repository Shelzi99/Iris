flower_dict = {}
flower_name = ''
height = 0
iris = 'iris2.txt'
temp_height = 0
temp_name = ''


#FUNCTIONS:

def add_to_dict(flower, height):
    #function adds values to dictionary
    flower_dict[flower]= height

def get_tempheigh_and_tempname_in_line(line):
    global temp_name
    global temp_height

    index = line.rfind(",")
    temp_name = line[index+1:]
    temp_line = line[:index]
    index = temp_line.rfind(",")
    temp_height = temp_line[index+1:]

def is_same_name (flower_name,temp_name):
    if flower_name == temp_name:
        return True
    else:
        return False


###########################################
# read file:
with open(iris, 'r') as reading_file:
    for line in reading_file:
        #read line
        get_tempheigh_and_tempname_in_line(line)
        #ckeck if new flower
        if is_same_name(flower_name,temp_name):
            #add the temp height to height
            height= height+ float(temp_height)

        else:
            #add flower to dictionary
            if flower_name != '':
                add_to_dict(flower_name, height)
                height = float(temp_height)
                flower_name = temp_name
            else:
                flower_name = temp_name
                height = height+float(temp_height)


add_to_dict(flower_name, height)
print (flower_dict)