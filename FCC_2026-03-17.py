from bisect import bisect

def get_milestone(years):
    breakpoints = [1, 5, 10, 25, 40, 50, 60, 70]
    milestones = ["Newlyweds", "Paper", "Wood", "Tin", "Silver", "Ruby", "Gold", "Diamond", "Platinum"]
    return milestones[bisect(breakpoints, years)]
