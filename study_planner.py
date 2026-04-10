# Simple Study Planner

subjects = ["Math", "DBMS", "CN"]
days = 3

for i in range(days):
    print(f"Day {i+1}: Study {subjects[i % len(subjects)]}")
