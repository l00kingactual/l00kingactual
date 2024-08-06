# Constants
total_hours_in_year = 24 * 7 * 365

# Scenario 1: 50-hour workweek, 40 weeks per year
hours_per_week_scenario1 = 50
weeks_per_year_scenario1 = 40
total_hours_worked_scenario1 = hours_per_week_scenario1 * weeks_per_year_scenario1
people_needed_scenario1 = total_hours_in_year / total_hours_worked_scenario1

# Scenario 2: 40-hour workweek, 48 weeks per year
hours_per_week_scenario2 = 40
weeks_per_year_scenario2 = 48
total_hours_worked_scenario2 = hours_per_week_scenario2 * weeks_per_year_scenario2
people_needed_scenario2 = total_hours_in_year / total_hours_worked_scenario2

# Scenario 3: 30-hour workweek, 50 weeks per year
hours_per_week_scenario3 = 30
weeks_per_year_scenario3 = 50
total_hours_worked_scenario3 = hours_per_week_scenario3 * weeks_per_year_scenario3
people_needed_scenario3 = total_hours_in_year / total_hours_worked_scenario3

# Print results
print("Scenario 1: Number of people needed for each team:", people_needed_scenario1)
print("Scenario 2: Number of people needed for each team:", people_needed_scenario2)
print("Scenario 3: Number of people needed for each team:", people_needed_scenario3)
