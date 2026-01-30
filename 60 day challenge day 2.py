student_id = input("Enter Student ID: ")
email = input("Enter Email: ")
password = input("Enter Password: ")
referral = input("Enter Referral Code: ")

valid = True

if len(student_id) != 7:
    valid = False
elif student_id[3] != "-":
    valid = False
elif student_id[0:3] != "CSE":
    valid = False
elif student_id[4] < '0' or student_id[4] > '9':
    valid = False
elif student_id[5] < '0' or student_id[5] > '9':
    valid = False
elif student_id[6] < '0' or student_id[6] > '9':
    valid = False

elif '@' not in email or '.' not in email:
    valid = False
elif email[0] == '@':
    valid = False
elif email[len(email) - 4:] != ".edu":
    valid = False

elif len(password) < 8:
    valid = False
elif password[0] < 'A' or password[0] > 'Z':
    valid = False
elif not (
    '0' in password or '1' in password or '2' in password or
    '3' in password or '4' in password or '5' in password or
    '6' in password or '7' in password or '8' in password or
    '9' in password
):
    valid = False

elif len(referral) != 6:
    valid = False
elif referral[5] != '@':
    valid = False
elif referral[0:3] != "REF":
    valid = False
elif referral[3] < '0' or referral[3] > '9':
    valid = False
elif referral[4] < '0' or referral[4] > '9':
    valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")