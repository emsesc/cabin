# learning-lab-automator

The Github Action automatically generates the needed files to create a Github Learning Lab. Refer to the below documentation for formatting requirements, how it works, and how to incorporate it:

---

## Adding it to a repository

* Place `learninglabauto.py` and `commit.sh` in `/scripts`
* Add secrets USERNAME and EMAIL to Github repository
* Place `main.yml` in `.github/workflows/`

What your `main.yml` should look like:

```yml
name: Learning Lab Automator

on:
  push:
    branches:
      - master

jobs:

  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Setup Python Environment
        uses: actions/setup-python@v2
        with:
          python-version: 3.7

      - name: Execute Python script
        run: |
          python scripts/learninglabauto.py
          
      - name: setup git config
        run: |
          git config user.name ${{ secrets.USERNAME }}
          git config user.email ${{ secrets.EMAIL }}
      - name: commit changes
        run: |
          chmod +x ./scripts/commit.sh
          ./scripts/commit.sh
```

## Instructions:
1. Place all response files in `/responses`
2. Create `course-details.md` in root directory

### :one: Input and Output

**User must provide:**
- Response files in `/camp-name/homework/responses`
- `course-details.md` file in `/camp-name/homework/course-details.md`

**Github Action produces:**
- Completion response files named `#-complete.md` and `feedback.md`
- A `config.yml` file

Note: "camp-name" is whatever the Bit Camp is called. If we were to create files for a camp named "Serverless-Functions", the file path would be `/Serverless-Functions/homework/responses`.

### :two: Formatting Requirements

In order for the Action to successfully parse content, the files **must** be named and formatted like so:

#### Response files

File name format: `[Week#].[Step#]-[Step title].md`

> Example: `1.1-Week Step 1.md`

File path: `/Serverless-Functions/homework/responses/[all response files]`

File content: 
* Response files are to be **titled with h2** at the very beginning of each markdown file. The title at the top will be the same title used in Github Learning Labs (what is in the config.yml file). 
* The **description** of the step should be placed directly under formatted in **h4**.

> Example:
```md
## Week 1 Step 1

#### This is the description
```

#### `course-details.md` File

File name: `course-details.md`

File path: `/camp-name/homework/course-details.md`

File content: 
* The `course-details.md` file must contain the course name and description.
* The course name must be **formatted with h1** and the course description **must be italicized.**

> Example:

```md
# Course Title

*Course description*
```

### :three: Specifying the Camp name

The Github Action will not run the Python file until a subdirectory (ie. Serverless-Functions) is specified. To do so, edit the `learninglabauto.py` file's `subdir` value.

**Before:**
```py
subdir = ""

if subdir == "":
  exit()
```

**After:**
```py
subdir = "[Insert your camp name. Ex: Serverless-Functions]"

if subdir == "":
  exit()
```

### :four: Finishing up

Once both the change to the `learninglabauto.py` file in `scripts/` and the addition of the other files are committed, the Github Action should trigger and run.

Linked [here](https://github.com/emsesc/sample-learninglab) is a sample containing correctly formatted file names and structures.

Watch this video for a walkthrough:
[![Watch the video](https://cdn.loom.com/sessions/thumbnails/d21df3bc8776488b81c6682449e81776-with-play.gif)](https://www.loom.com/share/d21df3bc8776488b81c6682449e81776)
