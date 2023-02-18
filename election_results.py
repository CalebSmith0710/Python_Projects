election_results = {}
election_results_list = []
line_index = 0

class Elections:
    def __init__(self, list: list):
        self.list = list

    def wasted_votes(self, list)->str:
        democrat_votes = sum(list[1:-1:2])
        republican_votes = sum(list[2:-1:2])
        num_districts = sum(list[0:-1:2])
        num_to_win = (democrat_votes + republican_votes) / 2

        if democrat_votes > republican_votes:
            wasted_dem_votes = democrat_votes - num_to_win
            wasted_rep_votes = num_to_win - republican_votes
        else:
            wasted_dem_votes = num_to_win - democrat_votes
            wasted_rep_votes = republican_votes - num_to_win

        efficiency_gap = abs(wasted_rep_votes - wasted_dem_votes) / (democrat_votes + republican_votes)

        return f"{num_districts} districts.\nWasted Democratic votes: {wasted_dem_votes}\nWasted Republican votes: {wasted_rep_votes}\nEfficiency gap: {efficiency_gap}"


with open("1976-2020votes.txt", "r") as a_file:
    for line in a_file:
        line = line.strip().split(",")

        list = []
        for element in line[2::]:
            list.append(int(element))

        election_results_objects = [(Elections(list))]
        election_results_list.append(election_results_objects)
        
        if line[0] not in election_results:
            election_results[f"{line[0]}"] = {f"{line[1]}": f"{election_results_list[line_index]}"}
        else:
            election_results[f"{line[0]}"][f"{line[1]}"] = (election_results_list[line_index])
        
        line_index += 1


        

# year = input("What year would you like to examine?: ")
# state = input("What state would you like to examine?: ").lower()

year_and_state = election_results["1976"]["ALABAMA"]

#year_and_state.wasted_votes()

print(year_and_state)
print(type(year_and_state))


# voting_data = [[331621,105955],[316925,182547],[194122,220634],[173945,285606],[161600,249013],[250314,175192],[250525,159301]]

# wasted_democrat_votes = 0
# wasted_republican_votes = 0
# num_votes = 0

# for voting_data_index in range(len(voting_data)):
#     num_votes += (voting_data[voting_data_index][0] + voting_data[voting_data_index][1])
#     if voting_data[voting_data_index][0] > voting_data[voting_data_index][1]:
#         wasted_republican_votes += voting_data[voting_data_index][1]
#         wasted_democrat_votes += (voting_data[voting_data_index][0] - ((voting_data[voting_data_index][0] + voting_data[voting_data_index][1]) // 2))
#     else:
#         wasted_democrat_votes += voting_data[voting_data_index][0]
#         wasted_republican_votes += (voting_data[voting_data_index][1] - ((voting_data[voting_data_index][0] + voting_data[voting_data_index][1]) // 2))

# efficiency_gap = abs((wasted_democrat_votes - wasted_republican_votes) // 3057300) * 100

# if wasted_democrat_votes > wasted_republican_votes:
#     print(f"{wasted_democrat_votes} wasted Democrat votes\n{wasted_republican_votes} wasted Republican votes\nEfficiency gap of {efficiency_gap}% in favor of Democrats")
# else:
#     print(f"{wasted_democrat_votes} wasted Democrat votes\n{wasted_republican_votes} wasted Republican votes\nEfficiency gap of {(efficiency_gap)}% in favor of Republicans")

# print(f"Number of Votes : {num_votes}")