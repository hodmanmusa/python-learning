class Player:
    format = "T20I"

    def __init__(self, name, nationality, age, is_active, innings):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.is_active = is_active
        self.innings = innings

    def display_record(self):
        print(f"\n{self.name}:")
        print(f"\tNationality: {self.nationality}")
        print(f"\tAge: {self.age}")
        print(f"\tIs Active: {self.is_active}")
        print(f"\tInnings Played: {self.innings}")


class Batsman(Player):
    total_batsmen = 0   

    def __init__(self, name, nationality, age, is_active, innings,
                 runs, balls_faced, not_outs, high_score):
        super().__init__(name, nationality, age, is_active, innings)
        self.runs = runs
        self.balls_faced = balls_faced
        self.not_outs = not_outs
        self.high_score = high_score
        Batsman.total_batsmen += 1

    def calculate_average(self):   
        dismissals = self.innings - self.not_outs
        return self.runs / dismissals if dismissals > 0 else 0

    def calculate_strike_rate(self):   
        return (self.runs / self.balls_faced) * 100 if self.balls_faced > 0 else 0

    def display_record(self):
        super().display_record()
        print(f"\tRuns: {self.runs}")
        print(f"\tBalls Faced: {self.balls_faced}")
        print(f"\tHighest Score: {self.high_score}")
        print(f"\tStrike Rate: {self.calculate_strike_rate():.2f}")
        print(f"\tAverage: {self.calculate_average():.2f}")
        print("\tType: Batsman")


class Bowler(Player):
    total_bowlers = 0   

    def __init__(self, name, nationality, age, is_active, innings,
                 balls, runs, wickets, best_figures):
        super().__init__(name, nationality, age, is_active, innings)
        self.balls = balls
        self.runs = runs
        self.wickets = wickets
        self.best_figures = best_figures
        Bowler.total_bowlers += 1

    def calculate_economy(self):   
        return (self.runs * 6) / self.balls if self.balls > 0 else 0

    def calculate_average(self):   
        return self.runs / self.wickets if self.wickets > 0 else 0

    def calculate_strike_rate(self):   
        return self.balls / self.wickets if self.wickets > 0 else 0

    def display_record(self):
        super().display_record()
        print(f"\tRuns Conceded: {self.runs}")
        print(f"\tBalls Bowled: {self.balls}")
        print(f"\tWickets Taken: {self.wickets}")
        print(f"\tBest Bowling Figures: {self.best_figures}")
        print(f"\tEconomy: {self.calculate_economy():.2f}")
        print(f"\tStrike Rate: {self.calculate_strike_rate():.2f}")
        print(f"\tAverage: {self.calculate_average():.2f}")
        print("\tType: Bowler")


Gurbaz = Batsman("Rahmanullah Gurbaz", "Afghan", 24, True, 80, 2067, 1533, 0, 151)
Ibrahim = Batsman("Ibrahim Zadran", "Afghan", 24, True, 58, 1558, 1405, 7, 72)

Rashid = Bowler("Rashid Khan", "Afghan", 27, True, 108, 2462, 2492, 182, "5/3")
Farooqi = Bowler("Fazalhaq Farooqi", "Afghan", 25, True, 51, 1078, 1246, 63, "5/9")

Gurbaz.display_record()
Ibrahim.display_record()
Rashid.display_record()
Farooqi.display_record()
