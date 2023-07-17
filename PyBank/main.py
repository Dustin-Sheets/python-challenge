
import pandas as pd
#importing data
bd = pd.read_csv("Resourses/budget_data.csv")

# counting months
months = len(bd)

# getting net profit/loss
totprof = sum(bd["Profit/Losses"])

# finding avg change/greatest increase/greatest decrease
bd["shifted_profit/loss"] = bd["Profit/Losses"].shift(1)
bd["difference"] = bd["Profit/Losses"] - bd["shifted_profit/loss"]

avg = round(bd["difference"].mean(),2)
increase = round(bd["difference"].max())
decrease = round(bd["difference"].min())

# searching for date for greatest increase/decrease
rowinc = bd.loc[bd["difference"] == increase]
rowdec  = bd.loc[bd["difference"] == decrease]
incdate = rowinc.at[79,"Date"]
decdate = rowdec.at[49,"Date"]

# removing added columns
bd.drop(["shifted_profit/loss","difference"],axis = 1,inplace = True)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${totprof}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {incdate} (${increase})")
print(f"Greatest Decrease in Profits: {decdate} (${decrease})")

with open("analysis/Analysis.txt",'w') as a:
    a.write("Financial Analysis\n")
    a.write("----------------------------\n")
    a.write(f"Total Months: {months}\n")
    a.write(f"Total: ${totprof}\n")
    a.write(f"Average Change: ${avg}\n")
    a.write(f"Greatest Increase in Profits: {incdate} (${increase})\n")
    a.write(f"Greatest Decrease in Profits: {decdate} (${decrease})\n")





