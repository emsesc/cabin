# learning-lab-automator

## Instructions:
1. Place all response files in `/responses`
2. Create `course-details.md` in root directory

## How it works:

User provides:
* Course name and description in `course-details.md`
* Response files in `/responses` and any images in `/images`

This returns:
* `config.yml`
* Course completion response files in `/responses`
* Feedback file
* A template repository

## Response Files

### Naming Conventions
Step response file name: `[Week#].[Step#]-[Step title].md`

> Example: `1.1-Week Step 1.md`

After each week is complete, a file that contains the link to move on the the next week (or issue): `[Week#]-complete.md`

> Example: `1-complete.md`

The `course-details.md` file must contain the course name and description. **The course name must be formatted with h1 and the course description must be italicized.**

> Example:

```md
# Course Title

*Course description*
```

### Structure

Response files are to be titled with h2 at the very beginning of each markdown file. The title at the top will be the same title used in Github Learning Labs (what is in the config.yml file). **The description of the step should be placed directly under formatted in h4.**

> Example:
```md
## Week 1 Step 1

#### This is the description
```

Completion response files are structured in this format: 
```md
[That's it for Week #! Click here to move on to Week #!]({{ repoUrl }}/issues)
```
*There are named by `#-complete.md`*

The last response file contains:
```md
That's it for Week #! Great work on completing the course!
```
