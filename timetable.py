from datetime import datetime

def main():
    # Read input file
    inFile = open("timetable.txt", "r")
    line = inFile.readline()
    lines = list()
    lines.append(line)
    while line != "":
        line = inFile.readline()
        if line != "":
            lines.append(line)
    print("Number of class: ", len(lines))

    # Split lines into records
    myClasses = []
    for line in lines:
        record = line.split("\t")
        record.remove(record[3])
        record.remove(record[4])
        record.remove(record[4])
        record.remove(record[6])
        myClasses.append(record)

    # Open output file
    outFile = open("timetable.csv", "w")
    outFile.write("Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private" + "\n")   
    # Process records
    for rc in myClasses:
        print("----------------------")
        group = rc[0].split("_")[2]
        subject = group + " - " + rc[1]
        print("Subject: " + subject)
        location = rc[2]
        print("Location: " + location)
        weekday = rc[3]
        print("Weekday: " + weekday)
        classTime = rc[4].split(" - ")
        startTime = classTime[0]
        endTime = classTime[1]
        print("Start Time: ")
        print(startTime)
        print("End Time: ")
        print(endTime)
        weeks = rc[5].split("|")
        while "--" in weeks:
            weeks.remove("--")
        while "" in weeks:
            weeks.remove("")
        print(weeks)
        for week in weeks:
            isoDate = str(datetime.today().year) + "-W" + str(week) + "-" + str(int(weekday) -1)
            normalDate = datetime.strptime(isoDate, "%Y-W%W-%w").date()
            year = str(normalDate).split("-")[0]
            month = str(normalDate).split("-")[1]
            day = str(normalDate).split("-")[2]
            print(year + "/" + month + "/" + day + " ")
            print(normalDate.ctime() + "\n")
            outFile.write(subject + ",")
            outFile.write(year + "/" + month + "/" + day + ",")
            outFile.write(str(startTime) + ",")
            outFile.write(year + "/" + month + "/" + day + ",")
            outFile.write(str(endTime) + ",")
            outFile.write("False,")
            outFile.write(",")
            outFile.write(location + ",")
            outFile.write("True\n")
    outFile.close()

main()