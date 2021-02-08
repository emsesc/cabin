import os
import re

try:
  responses = sorted(os.listdir("./.bit/responses"))

  print(responses)
  weeks = []
  steps = {}
  rm = []
  issue = 1

  try:
    # determining number of weeks
    for file in responses:
      if file[-12:] == "-complete.md" and len(file) <= 14:
        rm.append(file)
      elif file[0].isnumeric():
        weeks.append(file[0])
      else:
        rm.append(file)

    for delete in rm:
      responses.remove(delete)
  except:
    print("-------------------------\n[ERROR] Syncing was not successful. Please check your filenames and ensure that they adhere to the specified format.\n-------------------------")

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

  try:
    # determining course name and description
    name = "# (.*)"
    content = "(?<=\*)[^*]+(?=\*)"
    with open("./.bit/course-details.md", "r") as file:
      file = file.read()
      course_name = re.findall(name, file)[0]
      course_descr = re.findall(content, file)[0]
  except:
    print("-------------------------\n[WARNING] Syncing was not successful. Please check your 'course-details.md' file and make sure it adheres to the specified format.\n-------------------------")

  print("Course name: " + course_name + "\n" + "Course description: " + course_descr)

  try:
    # determining step names and descriptions
    stepContent = {}
    for i in responses:
      with open("./.bit/responses/" + i, "r") as file:
        title = "## (.*)"
        des = "#### (.*)"
        file = file.read()
        step_name = re.findall(title, file)[0]
        step_descr = re.findall(des, file)[0]
        stepContent[i] = [step_name, step_descr]

    print("Step data: ", stepContent)
  except:
    print("-------------------------\n[WARNING] Syncing was not successful. Please check your response files and ensure that the content adheres with the specified format.\n-------------------------")

  def createStep(week, title, descr, event, response, issue):
    content = "    - title: 'Week %s: %s'\n      description: %s\n      event: %s\n      link: '{{ repoUrl }}/issues'\n      actions:\n        - type: respond\n          with: %s\n          issue: %s\n" % (week, title, descr, event, response, issue)
    return content

  def writeyml():
    print("Creating the config.yml file...")
    final = ""
    content = "title: %s\ndescription: >-\n    %s\ntemplate:\n    name: %s\n    repo: %s\nbefore:\n    - type: createIssue\n      title: Week 1\n      body: %s" % (course_name, course_descr, "learninglab-template", "your-learninglab-template", responses[0])
    count = 0
    for i in range(nweeks):
      if i == 0:
        issue = 1
      else:
        issue += steps[i] + 1
      for y in range(steps[i+1]):
        if y == steps[i+1]-1:
          response = "feedback.md"
        else:
          response = responses[count+1]
        final += createStep(i+1, stepContent[responses[count]][0], stepContent[responses[count]][1], "pull_request.closed", response, issue)

        if y == steps[i+1]-1 and i == nweeks - 1:
          final += "    - title: 'Week %s: Feedback'\n      description: Provide your feedback for Week %s!\n      event: issue_comment.created\n      link: '{{ repoUrl }}/issues'\n      actions:\n        - type: respond\n          with: %s\n          issue: %s\n        - type: closeIssue\n          issue: %s\n" % (i+1, i+1, str(i+1)+"-complete.md", issue, issue)
        elif y == steps[i+1]-1:
          final += "    - title: 'Week %s: Feedback'\n      description: Provide your feedback for Week %s!\n      event: issue_comment.created\n      link: '{{ repoUrl }}/issues'\n      actions:\n        - type: respond\n          with: %s\n          issue: %s\n        - type: createIssue\n          title: Week %s\n          body: %s\n        - type: closeIssue\n          issue: %s\n" % (i+1, i+1, str(i+1)+"-complete.md", issue, i+2, responses[count+1], issue)
        count += 1
    
    configyml = content + "\nsteps:\n" + final
    return configyml

  with open("./.bit/responses/feedback.md", "w+") as myfile:
    print("Creating response files...")
    myfile.write("## Providing Feedback\n\nWhat was confusing about this week? If you could change or add something to this week, what would you do? Your feedback is valued and appreciated!")

  for i in range(1,nweeks+1):
    with open("./.bit/responses/" + str(i) + "-complete.md", "w+") as response:
      if i == nweeks:
        response.write("That's it for Week %s! Great job on finishing the course!" % str(i))
      else:
        response.write("That's it for Week %s, move on to Week %s in your new issue!" % (str(i), str(i + 1)))

  with open("config.yml", "w+") as file:
    file.write(writeyml())

except:
  print("-------------------------\n[WARNING] Syncing was not successful. Please make sure that you have placed response files in '.bit/responses' and course details under the directory '.bit/'\n-------------------------")
