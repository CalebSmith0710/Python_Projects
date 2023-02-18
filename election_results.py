"""
A program that allows users to evaluate districting fairness based on
wasted votes and efficiency gaps for all US House election districts
from 1976 - 2020. The data structure is sorted into a dictionary of
election results sorted into sub-dictionaries of states containing
Election objects as defined in "class Elections". Wasted votes and
efficiency gaps are calculated in the wasted_votes method contained
in the Elections class, the data is returned as a string and printed
in the main code block.

    Filename: caleb_smith_project_6.py
    Authors: Caleb Smith
    Date: 2/18/2023
    Course: COMP 1352
    Assignment: Project 6 - Fair districting, Gerrymandering, Wasted Votes and Efficiency Gap
    Collaborators: None
    Internet Source: https://www.quantamagazine.org/the-math-behind-gerrymandering-and-wasted-votes-20171012/
"""

election_results = {}

class Elections:
    def __init__(self, list: list):
        self.list = list

    def wasted_votes(self)->str:

        # assign variables based on list provided
        democrat_votes = self.list[1:-1:2]
        republican_votes = self.list[2:-1:2]
        num_districts = len(self.list[0:-1:3])

        # initialize wasted votes to 0
        wasted_rep_votes = 0
        wasted_dem_votes = 0

        # if the state has more than one district, calculate wasted votes and efficiency gap
        if num_districts > 1:
            for district_index in range(num_districts):
                # the number of votes required to win is half the total votes in the district
                num_to_win = (democrat_votes[district_index] + republican_votes[district_index]) / 2

                # if democrats have more votes, all the republican votes are wasted and the number of
                # wasted democrat votes is the excess votes that go past the number required to win
                if democrat_votes[district_index] > republican_votes[district_index]:
                    wasted_rep_votes += republican_votes[district_index]
                    wasted_dem_votes += democrat_votes[district_index] - num_to_win
                
                # same logic in reverse
                else:
                    wasted_dem_votes += democrat_votes[district_index]
                    wasted_rep_votes = republican_votes[district_index] - num_to_win

            # the efficiency gap is a percentage calculated by taking the difference in the wasted votes and dividing
            # it by the total number of votes in the state, this number is multiplied by 100 and rounded to 2 decimal
            # places to display it as a percentage
            efficiency_gap = f"Roughly {round((abs(wasted_rep_votes - wasted_dem_votes) / (sum(democrat_votes) + sum(republican_votes)) * 100), 2)}%"
            # this is what gets printed in the main code block
            return f"{num_districts} districts.\nWasted Democratic votes: {wasted_dem_votes}\nWasted Republican votes: {wasted_rep_votes}\nEfficiency gap: {efficiency_gap}"
        else:
            # this is printed to the main code block if the state has no more than one district
            return "Can't calculate efficiency gap for states with only one district"

# open the file "1976-2020votes.txt" and format it
with open("1976-2020votes.txt", "r") as a_file:
    for line in a_file:
        line = line.strip().split(",")

        # results is a list that takes the districts and votes from the line in the file and
        # turns each element into an integer in order to make calculations possible
        results = [int(result) for result in line[2:]]

        # if the string at the first index has not appeared in the file before, create
        # a new dictionary, the value of which is a dictionary with the state, found
        # at the next index in the line, as the key and "filler" as the value for
        # readability
        if line[0] not in election_results:
            election_results[f"{line[0]}"] = {f"{line[1]}": "filler"}

        # instantiate an Election object using the results list created earlier
        election = Elections(results)

        # replace "filler" with the new Election object as the value associated with the state
        election_results[f"{line[0]}"][f"{line[1]}"] = election


print("This program evaluates districting fairness for US House elections from 1976-2020.")

# while loop to determine when the program is running
run_program = "yes"
while run_program != "no":

    # get the year from the user
    year = input("What year would you like to examine?: ")
    while year not in election_results:
        year = input("Invalid input - Enter an even year between 1976 to 2020: ")

    # get the state from the user
    state = input("What state would you like to examine?: ").upper()
    while state not in election_results[year]:
        state = input("Invalid input - Enter a valid US state: ").upper()

    # store the dictionary value associated with the year and state (Election object)
    # in the variable year_and_state
    year_and_state = election_results[f"{year}"][f"{state.upper()}"]

    # print the retured value of the wasted_votes method to the terminal
    print(year_and_state.wasted_votes())

    # options to continue
    continue_options = ("yes", "no")

    # prompt the user to either continue or end the program
    continue_decision = input("Would you like to continue? YES/NO: ").lower()
    while continue_decision not in continue_options:
        continue_decision = input("Invalid input - Please choose from the following options YES/NO: ").lower()

    # tuple with options to end the program
    end_program = ("no")

    # if the user's input is not in end_program, continue running the program
    if continue_decision not in end_program:
        run_program = "yes"
    else:
        run_program = "no"
