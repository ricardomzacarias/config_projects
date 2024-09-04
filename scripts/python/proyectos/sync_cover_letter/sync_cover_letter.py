#!/usr/bin/python3
# script to automate the sending of cover letters to companies
import subprocess
from datetime import datetime

def copy_clipboard(solution):
    process = subprocess.Popen(
        # xclip o xsel in linux - the original function is put the pipe in between "echo" and "xclip"
        ['xclip', '-selection', 'clipboard'],
        stdin=subprocess.PIPE
    )
    process.communicate(input=solution.encode('utf-8')) # solution is the main function

def cover_letter(data):

    letter=f"""
Nombre: {data['name']}.
Profesion: {data['profession']}.
Título: {data['degree']}.
    """
    return letter.strip()

def cover_letter_email(data):
    letter=f"""
Nombre: {data['name']},
Email: {data['email']},
Direccion: {data['address']}
            """
    return letter.strip()


def main():
    #your data
    name=""
    email=""
    phoneNumber=""
    address=""
    profession=""
    degree=""
    dateTime=datetime.today().strftime("%d-%m-%Y")
    businessSector=""

    #input your data
    #name=input("name\n")
    #email=input("email\n")
    #phoneNumber=input("phoneNumber\n")
    #address=input("address\n")
    #profession=input("profession\n")
    #degree=input("degree\n")
    #dateTime=datetime.today().strftime("%d-%m-%Y")
    #businessSector=input("businessSector\n")

    company=input("")
    jobPosition=input("")
    
    universitySubjects=("")
    personalProjects=("")
    realExperience=("")

    data={
        #remember the second name is a variable
        #create dictionary
        'name': name,
        'email': email,
        'phone number': phoneNumber,
        'address': address,
        'degree': degree,
        'profession': profession,
        'date time': dateTime,
        'business sector': businessSector,
        #access
        'company': company,
        'job position': jobPosition,
        'university subjects': universitySubjects,
        'personal projects': personalProjects,
        'real experience': realExperience
    }

    #select presentation
    print("\nSelect your presentation type")
    print("1 - cover letter")
    print("2 - cover letter email")
    opcion = input("Opción (1/2): ")
    
    #better than case, you can use this conditional
    if opcion == '1':
        letter = cover_letter(data)
    elif opcion == '2':
        letter = cover_letter_email(data)
    else:
        print("Invalid Option, please select your true option")
        return

    #isn't necessary
    print(letter)

    #copy to clipboard any output for print
    copy_clipboard(letter)

if __name__ == "__main__":
    main()
