#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 17:50:57 2025

@author: Itri26
"""
# Problem Set 1:

## Part A: Saving for a House

yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
r = 0.05

down_payment_goal = cost_of_dream_home * portion_down_payment

amount_saved = 0
months = 0

while amount_saved < down_payment_goal:
    
    # Calculate Monthly Investment Return
    monthly_return = amount_saved * r/12
    
    # Claculate Monthly Salary Contribution
    monthly_salary_contribution = (yearly_salary/12) * portion_saved
    
    # Total Saving Update
    amount_saved += monthly_return + monthly_salary_contribution
    
    # Month Counter Increment
    months += 1

print("Number of months: ", months)
    
    


    