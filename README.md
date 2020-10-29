# Election_Analysis_2
## Overview of Election Audit
The task was to provide an election audit of tabulated results for a US congressional precint in Colorado.  I calculated election results to include total votes cast, total number of votes for each candidates, percentage of vote for each candidate and the winner of the election based on popular vote.  In this summary we also provide results that include total votes cast in three counties, county with largest number of turnout voters and percent. There are three primary voting methods we took into account for the total votes cast.  Those include:
-Main-In Ballots
-Punch cards
-Direct Recording Electronic

## Resources
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code

## Election Audit Results
Total number of votes cast for this congressional election was **369,711**
There are three counties included in this precint, Jefferson, Denver and Arapahoe.  Also provided is a breakdown of the number of votes and the percentage of total votes for each county. The results are as follows:
* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)
The county identified with the largest number of total votes was **Denver** with **82.8%**.  An impressive amount compared to the other two counties.  

Below is a breakdown of votes and percentage of votes for each candidate.
* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73,8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)
And finally, the candidate that won the election, their vote count and percentage of total votes:
* Winner: **Diana DeGette**
* Winning Vote Count: 272,892
* Winning Percentage: 73.8%

## Election Audit Summary
In summary, now that this script has been utilized to deliver the aforementioned results, this script, with some minor modifcations, can be used again for other election results.  For example, the data could be changed to include other counties, to find similar results or even changed slightly to include individual city voting results or used for Senatorial elections.
