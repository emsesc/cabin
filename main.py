import os


responses = os.listdir("./responses")
weeks = []
steps = {}

# determining number of weeks
for file in responses:
  weeks.append(file[0])

nweeks = max(weeks)
print("Number of weeks:", nweeks)

# determining number of steps per week
for i in range(1,int(nweeks)+1):
  count = 0
  for file in responses:
    if int(file[0]) == i:
        count += 1
  steps[i] = count

print(steps)


def createFiles():
   with open("/responses/feedback.md", "x") as myfile:
        myfile.write("## Providing Feedback\n\nWhat was confusing about this week? If you could change or add something to this week, what would you do? Your feedback is valued and appreciated!")

# we need to know:
# - number of weeks (done)
# - number of steps in each week (done)
# - each step's title + description

# we need to create:
# - each yml step
# - completed response files
# - a feedback.md file
# - a new template repository
