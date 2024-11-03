print("1. Phone book:")
print("2. Messages:")
print("3. Chat:")
print("4. Call register:")
print("5. Tones:")
print("6. Settings:")
print("7. Call divert:")
print("8. Games:")
print("9. Calculator:")
print("10. Reminders:")
print("11. Clock:")
print("12. Profiles:")
print("13. SIM services:")
        
menu = int(input("Select an option: "))

if menu == 1:
            print("1. Search")
            print("2. Service Nos.")
            print("3. Add name")
            print("4. Erase")
            print("5. Edit")
            print("6. Assign tone")
            print("7. Send b' card")
            print("8. Options")
            print("9. Speed dial")
            print("10. Voice tags")
            phonebook = int(input("Select an option: "))

            if phonebook == 1:
                print("Search")
            elif phonebook == 2:
                print("Service Nos.")
            elif phonebook == 3:
                print("Add name")
            elif phonebook == 4:
                print("Erase")
            elif phonebook == 5:
                print("Edit")
            elif phonebook == 6:
                print("Assign tone")
            elif phonebook == 7:
                print("Send b' card")
            elif phonebook == 8:
                print("Options")
                opt = int(input("Select an option: "))
                if opt == 1:
                    print("Type of view")
                elif opt == 2:
                    print("Memory status")
            elif phonebook == 9:
                print("Speed dial")
            elif phonebook == 10:
                print("Voice tags")

elif menu == 2:
            print("1. Write message")
            print("2. Inbox")
            print("3. Outbox")
            print("4. Picture messages")
            print("5. Templates")
            print("6. Smileys")
            print("7. Message settings")
            print("8. Info service")
            print("9. Voice mailbox")
            print("10. Service command editor")
            msg = int(input("Select an option: "))

            if msg == 1:
                print("Write message")
            elif msg == 2:
                print("Inbox")
            elif msg == 3:
                print("Outbox")
            elif msg == 4:
                print("Picture messages")
            elif msg == 5:
                print("Templates")
            elif msg == 6:
                print("Smileys")
            elif msg == 7:
                print("Message settings")
            elif msg == 8:
                print("Info service")
            elif msg == 9:
                print("Voice mailbox number")
            elif msg == 10:
                print("Service command editor")

elif menu == 3:
            print("Chat")
            int(input("Select an option: "))  # This section is not detailed in original code

elif menu == 4:
            print("1. Missed calls")
            print("2. Received calls")
            print("3. Dialed number")
            print("4. Erase recent call lists")
            print("5. Show call duration")
            print("6. Show call cost")
            print("7. Call cost settings")
            print("8. Prepaid credit")
            Callregister = int(input("Select an option: "))

            if Callregister == 1:
                print("Missed calls")
            elif Callregister == 2:
                print("Received calls")
            elif Callregister == 3:
                print("Dialed number")
            elif Callregister == 4:
                print("Erase recent call lists")
            elif Callregister == 5:
                print("Show call duration")
                calllog = int(input("Select an option: "))
                if calllog == 1:
                    print("Last call duration")
                elif calllog == 2:
                    print("All calls duration")
                elif calllog == 3:
                    print("Received calls duration")
                elif calllog == 4:
                    print("Dialed calls duration")
                elif calllog == 5:
                    print("Clear timers")
            elif Callregister == 6:
                print("Show call cost")
                callme = int(input("Select an option: "))
                if callme == 1:
                    print("Last call cost")
                elif callme == 2:
                    print("All calls cost")
                elif callme == 3:
                    print("Clear counters")
            elif Callregister == 7:
                print("Call cost settings")
                callcost = int(input("Select an option: "))
                if callcost == 1:
                    print("Call cost limit")
                elif callcost == 2:
                    print("Show cost in")
            elif Callregister == 8:
                print("Prepaid credit")

elif menu == 5:
            print("1. Ringing tone")
            print("2. Ringing volume")
            print("3. Incoming call alert")
            print("4. Composer")
            print("5. Message alert tone")
            print("6. Keypad tones")
            print("7. Warning and games tones")
            print("8. Vibrating alert")
            print("9. Screen saver")
            tones = int(input("Select an option: "))

            if tones == 1:
                print("Ringing tone")
            elif tones == 2:
                print("Ringing volume")
            elif tones == 3:
                print("Incoming call alert")
            elif tones == 4:
                print("Composer")
            elif tones == 5:
                print("Message alert tone")
            elif tones == 6:
                print("Keypad tones")
            elif tones == 7:
                print("Warning and games tones")
            elif tones == 8:
                print("Vibrating alert")
            elif tones == 9:
                print("Screen saver")

elif menu == 6:
            print("1. Call settings")
            print("2. Phone settings")
            print("3. Security settings")
            print("4. Restore factory settings")
            settings = int(input("Select an option: "))

            if settings == 1:
                print("1. Automatic redial")
                print("2. Speed dialing")
                print("3. Call waiting options")
                print("4. Own number sending")
                print("5. Phone line in use")
                print("6. Automatic answer")
                callsettings = int(input("Select an option: "))
                if callsettings == 1:
                    print("Automatic redial")
                elif callsettings == 2:
                    print("Speed dialing")
                elif callsettings == 3:
                    print("Call waiting options")
                elif callsettings == 4:
                    print("Own number sending")
                elif callsettings == 5:
                    print("Phone line in use")
                elif callsettings == 6:
                    print("Automatic answer")

            elif settings == 2:
                print("1. Language")
                print("2. Cell info display")
                print("3. Welcome note")
                print("4. Network selection")
                print("5. Lights")
                print("6. Confirm SIM service actions")
                phonesettings = int(input("Select an option: "))
                if phonesettings == 1:
                    print("Language")
                elif phonesettings == 2:
                    print("Cell info display")
                elif phonesettings == 3:
                    print("Welcome note")
                elif phonesettings == 4:
                    print("Network selection")
                elif phonesettings == 5:
                    print("Lights")
                elif phonesettings == 6:
                    print("Confirm SIM service actions")

            elif settings == 3:
                print("1. Pin code request")
                print("2. Call barring service")
                print("3. Fixed dialing")
                print("4. Closed user group")
                print("5. Phone security")
                print("6. Change access codes")
                securitysettings = int(input("Select an option: "))
                if securitysettings == 1:
                    print("Pin code request")
                elif securitysettings == 2:
                    print("Call barring service")
                elif securitysettings == 3:
                    print("Fixed dialing")
                elif securitysettings == 4:
                    print("Closed user group")
                elif securitysettings == 5:
                    print("Phone security")
                elif securitysettings == 6:
                    print("Change access codes")

            elif settings == 4:
                print("Restore factory settings")

elif menu == 7:
            print("Call divert")

elif menu == 8:
            print("Games")

elif menu == 9:
            print("Calculator")

elif menu == 10:
            print("Reminders")

elif menu == 11:
            print("1. Alarm clock")
            print("2. Clock settings")
            print("3. Date settings")
            print("4. Stop settings")
            print("5. Stopwatch")
            print("6. Countdown timer")
            print("7. Auto update of date")
            clock = int(input("Select an option: "))
            if clock == 1:
                print("Alarm clock")
            elif clock == 2:
                print("Clock settings")
            elif clock == 3:
                print("Date settings")
            elif clock == 4:
                print("Stop settings")
            elif clock == 5:
                print("Stopwatch")
            elif clock == 6:
                print("Countdown timer")
            elif clock == 7:
                print("Auto update of date")

elif menu == 12:
                print("Profile")

elif menu == 13:
                print("SIM service")
