import os
import time



class Logger:
    def __init__(self, script_path: str, filename: str="output.log"):
        self.fp = open(filename, "a")
        self.user = os.getlogin()
        self.script_path = script_path.split('\\')[-1]
        self.date_time = ""
    
    def __del__(self):
        self.fp.close()

    def write(self, log_message):
        string_message=str(log_message)
        self.__concat_date(time.localtime())
        self.fp.write(self.date_time + " ")
        self.fp.write(self.user + " ")
        self.fp.write(self.script_path + " ")
        self.fp.write("<OUTPUT=" + string_message + ">\n")

    def __concat_date(self, time_struct: time.struct_time):

        day = self.__add_leading_zero(time_struct.tm_mday)
        month = self.__add_leading_zero(time_struct.tm_mon)
        year = self.__add_leading_zero(time_struct.tm_year)
        hour = self.__add_leading_zero(time_struct.tm_hour)
        min = self.__add_leading_zero(time_struct.tm_min)
        sec = self.__add_leading_zero(time_struct.tm_sec)

        self.date_time =  day + "/" + month + "/" + year + " " + hour + ":" + min + ":" + sec

    def __add_leading_zero(self, number: int) -> str:
        if number < 10:
            return str("0" + str(number))
        return str(number)