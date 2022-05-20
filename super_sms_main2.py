
import os
from twilio.rest import Client
import time

import random

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
twiilio_number = "+15795000888"
account_sid = "ACddd2ede6c2beadb360ebfc4f6265cc44"
auth_token = "8f773ab7ea1fd0fbae74e9ee5232084a"
loop = 0
client = Client(account_sid, auth_token)


def main():
    global loop
    loop += 1
    messages = client.messages.list(limit=1)[0]

    def valid_date_of_birth(mm, dd, yyyy):
        if (1 <= mm <= 12) and (1 <= dd <= 12) and (1900 <= yyyy <= 2022):
            return True
        else:
            return False

    def get_name():
        save_path = '.\Y'
        file_name = messages.from_ + ".txt"
        y_path = os.path.join(save_path, file_name)

        save_path = '.\MEMBER'
        file_name = messages.from_ + ".txt"
        member_path = os.path.join(save_path, file_name)

        if (os.path.exists(member_path)) and (os.path.exists(y_path)):
            return True

    def get_date_of_birth():
        save_path = '.\Y'
        file_name = messages.from_ + ".txt"
        y_path = os.path.join(save_path, file_name)

        save_path = '.\MEMBER'
        file_name = messages.from_ + ".txt"
        member_path = os.path.join(save_path, file_name)

        save_path = '.\THENAME'
        file_name = messages.from_ + ".txt"
        member_path = os.path.join(save_path, file_name)

        if (os.path.exists(member_path)) and (os.path.exists(y_path)) and (os.path.exists(member_path)):
            return True

    if messages.from_ != twiilio_number:

        print(str(loop) + " " + messages.from_ + " " + messages.to +
              " " + messages.body + " " + str(messages.date_sent))
        customer_phone_number = messages.from_
        if messages.body.lower() == "stop":
            pass

        if get_name():

            save_path = '.\THENAME'
            file_name = messages.from_ + ".txt"
            name_path = os.path.join(save_path, file_name)
            if (os.path.exists(name_path)):
                pass
            else:
                outFile = open(name_path, "w")
                outFile.write(messages.body)
                outFile.close()
                message = client.messages \
                    .create(
                        body='What is your date of birth?\nFormat: MMDDYYYY. \nFor example: 01011988, if you were born on January, 1st, 1988',
                        from_='+15795000888',
                        to=customer_phone_number
                    )
        if get_date_of_birth():
            if (len(messages.body) == 8) and messages.body.isdigit():
                mm = int(messages.body[:2])
                dd = int(messages.body[2:4])
                yyyy = int(messages.body[4:8])

                if valid_date_of_birth(mm, dd, yyyy):
                    number = random.randint(1000, 9999)
                    save_path = '.\dob'
                    file_name = messages.from_ + ".txt"
                    dob_path = os.path.join(save_path, file_name)
                    outFile = open(dob_path, "w")
                    outFile.write(messages.body)
                    outFile.close()
                    message = client.messages \
                        .create(
                            body='''Congratulations! You have officially become Maple Leaf Queen's Buffet member. Stay tune for upcoming promotions!!''',
                            from_='+15795000888',
                            to=customer_phone_number
                        )
                    message = client.messages \
                        .create(
                            body='This is your 15% discount code: ' +
                            str(number) + '\nValid from: 05/21/2022 - 06/04/2022',
                            from_='+15795000888',
                            to=customer_phone_number
                        )
                    success_path = '.\SUCCESS'
                    file_name = messages.from_ + ".txt"
                    print(file_name)
                    success_path = os.path.join(success_path, file_name)
                    outFile = open(success_path, "w")
                    outFile.write(str(number))
                    outFile.close()

        if messages.body.lower() == "y":
            save_path = '.\Y'
            file_name = messages.from_ + ".txt"
            y_path = os.path.join(save_path, file_name)

            save_path = '.\MEMBER'
            file_name = messages.from_ + ".txt"
            member_path = os.path.join(save_path, file_name)

            if (os.path.exists(member_path)) and not(os.path.exists(y_path)):
                outFile = open(y_path, "w")
                outFile.write("")
                outFile.close()
                message = client.messages \
                    .create(
                        body='What is your name?',
                        from_='+15795000888',
                        to=customer_phone_number
                    )
            else:
                pass

        if messages.body.lower() == "member":
            save_path = '.\MEMBER'
            file_name = messages.from_ + ".txt"
            member_path = os.path.join(save_path, file_name)
            if (os.path.exists(member_path) or os.path.exists('.\MEMBER_FR\\'+file_name)):
                print("existed in en")
                pass
            else:
                outFile = open(member_path, "w")
                outFile.write("")
                outFile.close()
                message = client.messages \
                    .create(
                        body='Amazing! You are one step away from becoming our member.\nWe will need your name and date of birth. \nText "Y" to proceed. \nText "STOP" to opt-out.',
                        from_='+15795000888',
                        to=customer_phone_number
                    )

    def valid_date_of_birth_fr(mm, dd, yyyy):
        if (1 <= mm <= 12) and (1 <= dd <= 12) and (1900 <= yyyy <= 2022):
            return True
        else:
            return False

    def get_name_fr():
        save_path = '.\o'
        file_name = messages.from_ + ".txt"
        y_path = os.path.join(save_path, file_name)

        save_path = '.\MEMBER_FR'
        file_name = messages.from_ + ".txt"
        member_path = os.path.join(save_path, file_name)

        if (os.path.exists(member_path)) and (os.path.exists(y_path)):
            return True

    def get_date_of_birth_fr():
        save_path = '.\o'
        file_name = messages.from_ + ".txt"
        y_path = os.path.join(save_path, file_name)

        save_path = '.\MEMBER_FR'
        file_name = messages.from_ + ".txt"
        member_path = os.path.join(save_path, file_name)

        save_path = '.\THENAME_FR'
        file_name = messages.from_ + ".txt"
        member_path = os.path.join(save_path, file_name)

        if (os.path.exists(member_path)) and (os.path.exists(y_path)) and (os.path.exists(member_path)):
            return True

    if messages.from_ != twiilio_number:

        print(str(loop) + " " + messages.from_ + " " + messages.to +
              " " + messages.body + " " + str(messages.date_sent))
        customer_phone_number = messages.from_
        if messages.body.lower() == "stop":
            pass

        if get_name_fr():

            save_path = '.\THENAME_FR'
            file_name = messages.from_ + ".txt"
            name_path = os.path.join(save_path, file_name)
            if (os.path.exists(name_path)):
                pass
            else:
                outFile = open(name_path, "w")
                outFile.write(messages.body)
                outFile.close()
                message = client.messages \
                    .create(
                        body='Quelle est votre date de naissance ?\nFormat : MMJJAAAA. \nPar exemple : 01011988, si vous êtes né le 1er, janvier, 1988',
                        from_='+15795000888',
                        to=customer_phone_number
                    )
        if get_date_of_birth_fr():
            if (len(messages.body) == 8) and messages.body.isdigit():
                mm = int(messages.body[:2])
                dd = int(messages.body[2:4])
                yyyy = int(messages.body[4:8])

                if valid_date_of_birth_fr(mm, dd, yyyy):
                    number = random.randint(1000, 9999)
                    save_path = '.\DOB_FR'
                    file_name = messages.from_ + ".txt"
                    dob_path = os.path.join(save_path, file_name)
                    outFile = open(dob_path, "w")
                    outFile.write(messages.body)
                    outFile.close()
                    message = client.messages \
                        .create(
                            body='''Toutes nos félicitations! Vous êtes officiellement devenu membre du Maple Leaf Queen's Buffet. Restez à l'écoute pour les promotions à venir !!''',
                            from_='+15795000888',
                            to=customer_phone_number
                        )
                    message = client.messages \
                        .create(
                            body='Ceci est votre code de réduction de 15 %: ' +
                            str(number) + '\nValable du: 05/21/2022 - 06/04/2022',
                            from_='+15795000888',
                            to=customer_phone_number
                        )
                    success_path = '.\SUCCESS_FR'
                    file_name = messages.from_ + ".txt"
                    success_path = os.path.join(success_path, file_name)
                    outFile = open(success_path, "w")
                    outFile.write(str(number))
                    outFile.close()

        if messages.body.lower() == "o":
            save_path = '.\o'
            file_name = messages.from_ + ".txt"
            y_path = os.path.join(save_path, file_name)

            save_path = '.\MEMBER_FR'
            file_name = messages.from_ + ".txt"
            member_path = os.path.join(save_path, file_name)

            if (os.path.exists(member_path)) and not(os.path.exists(y_path)):
                outFile = open(y_path, "w")
                outFile.write("")
                outFile.close()
                message = client.messages \
                    .create(
                        body='Comment vous-appelez vous?',
                        from_='+15795000888',
                        to=customer_phone_number
                    )
            else:
                pass

        if messages.body.lower() == "membre":
            save_path = '.\MEMBER_FR'
            file_name = messages.from_ + ".txt"
            member_path = os.path.join(save_path, file_name)
            if (os.path.exists(member_path) or os.path.exists('.\MEMBER\\' + file_name)):
                print("existed in fr")
                pass
            else:
                outFile = open(member_path, "w")
                outFile.write("")
                outFile.close()
                message = client.messages \
                    .create(
                        body='Étonnante! Vous êtes sur le point de devenir membre.\nNous aurons besoin de votre nom et de votre date de naissance. \nTexte "O" pour continuer. \nTexte "STOP" pour vous désabonner.',
                        from_='+15795000888',
                        to=customer_phone_number
                    )


while True:
    time.sleep(0.5)
    main()
