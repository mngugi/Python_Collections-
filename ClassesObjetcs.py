# -*- coding: utf-8 -*-
""" 
Author :Peter Mwangi
Purpose : this is a classes and objects in python  
"""
class Football:
    Effort = 10

    def Gkeeper(self):
        print("Makes saves")
        self.Effort = 3
        

    def Defenders(self):
        if self.Effort >= 4:
            print("Good defending")
        else:
                print("Not good enough add a defensive midfielder")

    def Midfielders(self):
        if self.Midfielders >= 5:
            print("Team is 65% complete")
        else:
                 print("Add 2 good strikers")

    def Strikers(self):
        if self.Strikers >= 7: 
            print("That is a very good team")


    soccer = Football()

    soccer.Gkeeper()
    soccer.Defenders()
    soccer.Midfielders()
    soccer.Strikers()
