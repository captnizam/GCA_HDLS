import pandas as pd
import egcaFunction as e

e.openChrome()
e.login_egca()

df = pd.read_csv('nizam.csv')

entrty_count = 1

for row in df.values.tolist():
    try:
        entrty_count += 1
        try:
            e.fillLogbook_button()
        except:
            e.home_button()

        e.airline_selection()
        vt = row[7]

        e.aircraft_reg(vt)

        fo_name = row[8]
        e.copilot(fo_name)

        dep = row[2]
        dep_date = row[1]
        dep_time = row[3]

        shift = row[10]
        e.type_of_flight(shift)
        e.from_details(dep, dep_date, dep_time)

        arr = row[5]
        arr_date = row[4]
        arr_time = row[6]
        dist = row[13]
        e.arrival_entry(arr, arr_date, arr_time,dist)

        ir_time1 = row[9]
        e.instrument_time(ir_time1)

        d_time = row[11]
        n_time = row[12]

        e.day_or_night(shift, d_time, n_time)

        e.final_submission()

        print (entrty_count, " ENTRY SUBMITTEDddddddddddddddddddddddddddddddddddddddd                     SUBMITTED")
        print(dep_date, dep, fo_name,"Submitted")

    except:

        print(entrty_count," Entry Failedddddddddddddddddddddddddddddddddddddddddddd                         FAILED     ",)
        pass




