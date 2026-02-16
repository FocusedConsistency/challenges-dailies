def get_semifinal_matchups(teams):
    team_totals = []
    for team in teams:
        team_totals.append((team[0:3], 3 * int(team[5]) + 2 * int(team[7]) + int(team[9])))
    sorted_teams = sorted(team_totals, key=lambda x: x[1], reverse=True)
    ranked_teams = [team for team, points in sorted_teams]
    return f"The semi-final games will be {ranked_teams[0]} vs {ranked_teams[3]} and {ranked_teams[1]} vs {ranked_teams[2]}."

get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]) should return "The semi-final games will be FIN vs SWE and CAN vs USA."

def get_semifinal_matchups(teams):
    team_totals = []
    for team in teams:
        team_name, record = team.split(": ")
        wins, ot_wins, ot_losses, losses = map(int, record.split("-"))
        team_totals.append((team[0:3], 3 * wins + 2 * ot_wins + ot_losses))
    sorted_teams = sorted(team_totals, key=lambda x: x[1], reverse=True)
    ranked_teams = [team for team, points in sorted_teams]
    return f"The semi-final games will be {ranked_teams[0]} vs {ranked_teams[3]} and {ranked_teams[1]} vs {ranked_teams[2]}."
