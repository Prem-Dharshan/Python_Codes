# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:26:28 2023

@author: 22pw29
"""

"""1. Write a program that created a dictionary containing course numbers and
room numbers of the rooms where the courses meet. The dictionary should
have the following key-value pair
Course Number (key) Room Number ( Value )
CS101 3004
CS102 4501
CS103 6755
NT110 1244
CM241 1411
The program should also create a dictionary containing course numbers
and the names of the instructors that teach each course.
Course Number (key) Instructor ( Value )
CS101 Haynes
CS102 Alvarado
CS103 Rich
NT110 Burke
CM241 Lee
The program should also create a dictionary containing course numbers
and the meeting times of each course.
Course Number (key) Meeting Time ( Value )
CS101 8.00 am
CS102 9.00 am
CS103 10.00 am
NT110 11.00 am
CM241 1.00pm"""

from typing import Dict

def main() -> None
    course: Dict[str, Dict[str, str]]
    
    course = {
                "CS101" : 
                    {
                        "RoomNo" : 3004,
                        "Instructor" : "Haynes",
                        "MeetingTime" : "8.00 am"
                    },
    
                "CS102" : 
                    {
                        "RoomNo" : 4501,
                        "Instructor" : "Alvarado",
                        "MeetingTime" : "9.00 am"
                    },
                
                "CS103" : 
                    {
                        "RoomNo" : 6755,
                        "Instructor" : "Rich",
                        "MeetingTime" : "10.00 am"
                    },
                
                "NT110" :
                    {
                        "RoomNo" : 1244,
                        "Instructor" : "Burke",
                        "MeetingTime" : "11.00 am"
                    },
                    
                "CM241" :
                    {
                        "RoomNo" : 1411,
                        "Instructor" : "Lee",
                        "MeetingTime" : "1.00pm"
                    }
                
               }
        
    courseid = input("Enter a Course Number: ")
    
    print(f"""The Course Details are 
              Course Room Number: {course[courseid]['RoomNo']},
              Course Instructor: {course[courseid]['Instructor']},
              Course Meeting Time: {course[courseid]['MeetingTime']}.""")
        
        return None

if __name__ == "__main__":
    main()