<<<<<<< HEAD

# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter. 
total_votes=0

#Candidate Options and candidate votes
candidate_options=[]

#1. Decalre a empty dictionary 
candidate_votes={}

#Winning Candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0



# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Read and print the header row.
    headers = next(file_reader)
    
    # Priint each row in the csv file 
    for row in file_reader:
        #2. Add to the total vote count 
        total_votes+=1

        # Print the candidate name from each row 
        candidate_name= row[2]

        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidates vote count. 
            candidate_votes[candidate_name]=0

         #Add a vote to that candidat's count.
        candidate_votes[candidate_name]+=1

# Save the result to our text file.
with open(file_to_save,"w") as txt_file: 
    #Print the final vote count to the terminal.
    election_results=(
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"---------------------\n")

    print(election_results,end="")  

        
        

            # Determine the percentage of votes for each candidate by looping through the counts. 
            # 1. Iterate through the candidate list . 
    for candidate_name in candidate_votes:
        #2. Retreieve vote count of a candidate.
        votes=candidate_votes[candidate_name]
        #3. Calculate the percentage of votes. 
        vote_percentage=float(votes)/float(total_votes)*100
        #4. Print the candidate name and percentage of votes.
                
                
        candidate_results=(f"{candidate_name}:  {vote_percentage:1f}% ({votes:,})\n")

            #to do:print out each candidate's name, vote count, adnpercentage of 
            #votes to the terminal.
                
                
        print(election_results)
        # Save the final vote count to the text file.
        txt_file.write(election_results)


            #Determine winning vote count and candidate
            #Determine if the votes is greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count=votes and winning_percentage=
            #vote_percentage.
            winning_count=votes
            winning_percentage=vote_percentage
            #And, set the winning_candidate equal to the candidates name. 
            winning_candidate=candidate_name    

                    #to do:print out the winning candidate, vote count and percentage to 
                    # terminal 
                   
                    
                    #Print the winnig candidates resluts to the termainal.
            winning_candidate_summary=(

                f"---------------------\n"
                f"Winner:{winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"---------------------\n" )    
        
            print(winning_candidate_summary)
            #Save the winnign candidate's results to the text file
            txt_file.write(winning_candidate_summary)    





        
                    #If the candidate does not match any existing candidate...  
                    #if candidate_name not in candidate_options:
                        #Add it to the list of candidates.
                        #candidate_options.append(candidate_name)


            #Print the candidate list
            #print(candidate_options)

            #Print the candidate vote dictionary 
            #print(candidate_votes)




=======

# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter. 
total_votes=0

#Candidate Options and candidate votes
candidate_options=[]

#1. Decalre a empty dictionary 
candidate_votes={}

#Winning Candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0



# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Read and print the header row.
    headers = next(file_reader)
    
    # Priint each row in the csv file 
    for row in file_reader:
        #2. Add to the total vote count 
        total_votes+=1

        # Print the candidate name from each row 
        candidate_name= row[2]

        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidates vote count. 
            candidate_votes[candidate_name]=0

         #Add a vote to that candidat's count.
        candidate_votes[candidate_name]+=1

        # Determine the percentage of votes for each candidate by looping through the counts. 
        # 1. Iterate through the candidate list . 
for candidate_name in candidate_votes:
    #2. Retreieve vote count of a candidate.
    votes=candidate_votes[candidate_name]
    #3. Calculate the percentage of votes. 
    vote_percentage=float(votes)/float(total_votes)*100
    #4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: recieved  {vote_percentage}% of the vote.")

    #to do:print out each candidate's name, vote count, adnpercentage of 
    #votes to the terminal.



    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count. 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count=votes and winning_percentage=
        #vote_percentage.
        winning_count=votes
        winning_percentage=vote_percentage
        #And, set the winning_candidate equal to the candidates name. 
        winning_candidate=candidate_name    

#to do:print out the winning candidate, vote count and percentage to 
# terminal 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


winning_candidate_summary=(

f"---------------------\n"
f"Winner:{winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"---------------------\n" )    
print(winning_candidate_summary)
        #If the candidate does not match any existing candidate...  
        #if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            #candidate_options.append(candidate_name)


#Print the candidate list
#print(candidate_options)

#Print the candidate vote dictionary 
#print(candidate_votes)
>>>>>>> 7ac7b29121acd314e6a8b964036cd3da87e35e7d
