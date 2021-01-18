import os


os.listdir("/responses")

def createFiles():
   with open("/responses/feedback.md", "x") as myfile:
        myfile.write("## Providing Feedback\n\nWhat was confusing about this week? If you could change or add something to this week, what would you do? Your feedback is valued and appreciated!")

# we need to know:
# - number of weeks
# - number of steps in each week
# - each step's title + description

# we need to create:
# - each yml step
# - completed response files
# - a feedback.md file
# - a new template repository
