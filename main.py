import db
import datetime
import notifications


def main():
    stime, duration = input("Enter date time reservation (example 2022-07-15 08:30)"), input(
        "Enter Reservation duration at minutes (example 35)")
    num, mail = input("Enter your phone number (example +992xxxxxxxxx)"), input("Enter your email (example@gmail.com)")
    for column in db.db_select("""select*from "MeetingRoom"."RoomReservation" """):
        if stime.format("%yyyy-%MM-%dd %HH:mm") >= format(column[3]) or column[3] is None:
            etime = datetime.datetime.strptime(stime, "%Y-%m-%d %H:%M") + datetime.timedelta(minutes=int(duration))
            db.db_update(
                f"""UPDATE "MeetingRoom"."RoomReservation" SET "Stime"='{stime}', "Etime"='{etime}', "BusyBy"='{mail}'
                                     WHERE "ID"={column[0]} and "Name"='{column[1]}';""")
            print(notifications.send_email(mail, 'Room Reservation', 'You booked a ' + str(column[1]) + ' from '
                                           + str(column[2]) + ' to ' + str(column[3])))
            print(notifications.send_sms(num, 'You booked a ' + str(column[1]) + ' from ' + str(column[2]) + ' to '
                                         + str(column[3])))
            break
        else:
            print("Unfortunately there are not available rooms")


if __name__ == "__main__":
    main()
