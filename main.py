import os
import re

responses = os.listdir("./responses")
weeks = []
steps = {}

# determining number of weeks
for file in responses:
  weeks.append(file[0])

nweeks = int(max(weeks))
print("Number of weeks:", nweeks)

# determining number of steps per week
for i in range(1,nweeks+1):
  count = 0
  for file in responses:
    if int(file[0]) == i:
        count += 1
  steps[i] = count

print("Number of steps each week:", steps)

# determining course name and description
name = "# (.*)"
content = "(?<=\*)[^*]+(?=\*)"
with open("./course-details.md", "r") as file:
  file = file.read()
  course_name = re.findall(name, file)[0]
  course_descr = re.findall(content, file)[0]

print("Course name: " + course_name + "\n" + "Course description: " + course_descr)

# determining step names and descriptions
stepContent = {}
for i in responses:
  with open("./responses/" + i, "r") as file:
    title = "## (.*)"
    des = "#### (.*)"
    file = file.read()
    step_name = re.findall(title, file)[0]
    step_descr = re.findall(des, file)[0]
    stepContent[i] = [step_name, step_descr]

print("Step data: ", stepContent)

# def createStep():

# def writeyml():
content = "title: %s\ndescription: >-\n    %s\ntemplate:\n    name: %s\n    repo: %s\nbefore:\n    - type: %s\n      title: %s\n      body: %s" % (course_name, course_descr, "learninglab-template", "sample-learninglab-template", "createIssue", "Week 1", responses[0])

with open("config.yml", "x") as file:
  file.write(content)


def createFiles():
  # create feedback.md
  with open("./responses/feedback.md", "x") as myfile:
    myfile.write("## Providing Feedback\n\nWhat was confusing about this week? If you could change or add something to this week, what would you do? Your feedback is valued and appreciated!")
  

  for i in range(1,nweeks+1):
    with open("./responses/" + str(i) + "-complete.md", "x") as response:
      if i == nweeks+1:
        response.write("That's it for Week %s! Great job on finishing the course!" % str(i))
      else:
        response.write("[That's it for Week %s! Click here to move on to Week %s!]({{ repoUrl }}/issues)" % (str(i), str(i + 1)))


  

# we need to know:
# - number of weeks (done)
# - number of steps in each week (done)
# - each step's title + description (done)
# - course title + description (done)

# we need to create:
# - each yml step
# - completed response files (done)
# - a feedback.md file (done)
# - a new template repository
