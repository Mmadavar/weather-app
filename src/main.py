from Weather_Data import get_data
from Display_Data import result_data

def main():
    #Here we call the different files and the methods involved with it.
    Weather_Data = get_data()
    Display_Data = result_data(Weather_Data)

# Here we call the main function.
if __name__ == "__main__":
    main()
