import os
import datetime

working_dir = "D:\\anime\\Otakudesu_Saekano.S2_720p"
print(datetime.datetime.now())

def file_list():
    """
    return a list of file in the working directory
    """
    os.chdir(working_dir)
    file_list = os.listdir() # Gets a list of files in the CWD
    #file_list = file_list.sort()
    for index, name in enumerate(file_list):
        print(index, name) # Print the file with a number
    

    return file_list

def file_print(number):
    """
    return a single filename
    """
    os.chdir(working_dir)
    file_list = os.listdir() # Gets a list of files in the CWD
    return file_list[number]

def rename(old_filename, new_name):
    """
    accepts old filename, and changes its name to the specified new filename
    """
    try:
        os.rename(old_filename, new_name)
        print(f"Renamed '{old_filename}' to '{new_name}'")

    except FileNotFoundError:
        print(f"Error: '{old_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to rename '{old_filename}'.")
    except Exception as e:
        print(f"Error: {e}")

def name_prefix(file_names, extension):
    new_name = input("Enter a new name : ")
    temp_new_names = []

    print("1 =(1 filename) | 2 =(filename 1) | 3 =(1 - filename) | 4 =(filename - 1)")
    num_location = input("Enter a number location preference : ")

    if num_location == "1":
        for index, file in enumerate(file_names, start=1):
            temp_new_names.append(file + " --> " + str(index) + " " + new_name + extension)

    elif num_location == "2":
        for index, file in enumerate(file_names, start=1):
            temp_new_names.append(file + " --> " + new_name + " " + str(index) + extension)

    elif num_location == "3":
        for index, file in enumerate(file_names, start=1):
            temp_new_names.append(file + " --> " + str(index) + " - " + new_name + extension)

    elif num_location == "4":
        for index, file in enumerate(file_names, start=1):
            temp_new_names.append(file + " --> " + new_name + " - " + str(index) + extension)

    else : 
        print("Invalid input")

def mainloop():
    """
    mainloop of the program
    """
    looping = True
    command = "" # the command variable
    file_number = "" # for picking a file using a number in the CLI
    while looping:
        command = input("Enter a Command : ")
        if command == "1": # Gets a file list and input a file number
            file_list()

        elif command == "2": # Single file rename
            file_list()
            file_number = int(input("Enter a file number (rename) : "))
            file_name = file_print(file_number)
            new_name = input("Enter a new name : ")
            extension = "." + str(input("Enter file extension (ex = mkv, mp4, wav) : "))
            rename(file_name, new_name + extension)

        elif command == "3": # Bulk rename
            file_names = file_list()
            print("1 = replace all / new name | 2 = replace a specific text")
            replace_command = input("Enter a replace command : ")

            if replace_command == "1": # replace all
                new_file_names = name_prefix(file_names, "mkv")
                print(new_file_names)
            
                
                
                confirm = input("Y / N")
                if confirm.lower() == "y":
                    for file in new_file_names:
                        rename(file, new_file_names)
                    
            
            elif replace_command == "2": # replace a spesific text
                pass
            
            else: 
                pass

            # for name in file_names:




            
        elif command == "4": # exit
            print("Bye Bye :)")
            looping = False
            break


mainloop()
