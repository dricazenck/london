# Website Automations

- [Website Automations](#website-automations)
  - [Dependencies](#dependencies)
  - [Create mentor](#create-mentor)
  - [Update Mentor](#update-mentor)
    - [How to Execute](#how-to-execute)
      - [Script](#script)
      - [How to Test](#how-to-test)

## Dependencies

Install the following dependencies
* python3
* pip

```shell
pip install -r requirements.txt
```

## Create mentor

TBD

## Update Mentor

We will receive some new information from mentors about availability via email and it is necessary to update the information in the website.

This script will update mentor by email to include: availability, disable, matched, relationship type and others.

### How to Execute

#### Script

```shell
python update_mentors_availability.py
```

It will print the total of mentors existent in the yml file. 

#### How to Test

```shell
 python -m unittest discover -p '*_test.py'  
```

output
```shell
.......
----------------------------------------------------------------------
Ran 7 tests in 1.342s

OK
```