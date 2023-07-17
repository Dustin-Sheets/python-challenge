import pandas as pd
ed = pd.read_csv("Resources/election_data.csv")

# counting total votes
total = len(ed)

# counting individual votes
counts = ed["Candidate"].value_counts()

# storing values
dianatot = counts[0]
dianaper = round(100*(dianatot/total),3)

chartot = counts[1]
charper = round(100*(chartot/total),3)

raytot = counts[2]
rayper = round(100*(raytot/total),3)

# finding winner
if dianatot > chartot and dianatot > raytot:
    winner = "Diana DeGette"
elif chartot > raytot:
    winner = "Charles Casper Stockham"
else:
    winner = "Raymon Anthony Doane"


print(f"Election Results\n-------------------------\nTotal Votes: {total}\n-------------------------\nCharles Casper Stockham: {charper}% ([{chartot}])\nDiana DeGette: {dianaper}% ({dianatot})\nRaymon Anthony Doane: {rayper}% ({raytot})\n-------------------------\nWinner: {winner}\n-------------------------\n")

with open("analysis/Analysis.txt","w") as a:
    a.write(f"Election Results\n-------------------------\nTotal Votes: {total}\n-------------------------\nCharles Casper Stockham: {charper}% ([{chartot}])\nDiana DeGette: {dianaper}% ({dianatot})\nRaymon Anthony Doane: {rayper}% ({raytot})\n-------------------------\nWinner: {winner}\n-------------------------\n")