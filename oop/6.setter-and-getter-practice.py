# --------------------------------------------------
# Base Class: Player
# --------------------------------------------------
# Represents a generic cricket player
# --------------------------------------------------

class Player:
    # Match format shared by all players
    format = "T20I"

    def __init__(self, name, nationality, age, is_active, innings):
        # Common player attributes
        self.name = name
        self.nationality = nationality
        self.age = age
        self.is_active = is_active
        self.innings = innings


# --------------------------------------------------
# Subclass: Batsman
# --------------------------------------------------
# Represents a batsman and batting statistics
# --------------------------------------------------

class Batsman(Player):
    # Counts total batsman objects created
    total_batsmen = 0

    def __init__(self, name, nationality, age, is_active, innings,
                 runs, balls_faced, not_outs, high_score):
        # Initialize base Player attributes
        super().__init__(name, nationality, age, is_active, innings)

        # Batsman-specific attributes
        self.runs = runs
        self.balls_faced = balls_faced
        self.not_outs = not_outs
        self.high_score = high_score

        Batsman.total_batsmen += 1

    @property
    def calculate_average(self):
        # Batting average = runs / dismissals
        dismissals = self.innings - self.not_outs
        return self.runs / dismissals if dismissals > 0 else 0
    
    @property
    def calculate_strike_rate(self):
        # Strike rate = (runs / balls faced) * 100
        return (self.runs / self.balls_faced) * 100 if self.balls_faced > 0 else 0

    def __len__(self):
        # Return total runs scored
        return self.runs

    def __add__(self, other):
        # Combine runs of two batsmen
        if isinstance(other, Batsman):
            return (
                f"Total runs of {self.name} and {other.name} are: "
                f"{self.runs + other.runs}"
            )
        return "Both objects must be batsmen"

    def __str__(self):
        # Readable batting record
        return f"""
        Name: {self.name},\tNationality: {self.nationality}
        Age: {self.age},\t\tIs Active: {self.is_active}
        Innings: {self.innings},\t\tFormat: {self.format}
        Balls Faced: {self.balls_faced},\tRuns Scored: {self.runs}
        High Score: {self.high_score},\t\tTimes Not Out: {self.not_outs}
        Batting Average: {self.calculate_average:.2f}\t
        Strike Rate: {self.calculate_strike_rate:.2f}
        --------------------------------------
        """


# --------------------------------------------------
# Subclass: Bowler
# --------------------------------------------------
# Represents a bowler and bowling statistics
# --------------------------------------------------

class Bowler(Player):
    # Counts total bowler objects created
    total_bowlers = 0

    def __init__(self, name, nationality, age, is_active, innings,
                 balls, runs, wickets, best_figures):
        # Initialize base Player attributes
        super().__init__(name, nationality, age, is_active, innings)

        # Bowler-specific attributes
        self.balls = balls
        self.runs = runs
        self.wickets = wickets
        self.best_figures = best_figures

        Bowler.total_bowlers += 1

    @property
    def calculate_economy(self):
        # Economy rate = (runs conceded * 6) / balls bowled
        return (self.runs * 6) / self.balls if self.balls > 0 else 0

    @property
    def calculate_average(self):
        # Bowling average = runs conceded / wickets taken
        return self.runs / self.wickets if self.wickets > 0 else 0

    @property
    def calculate_strike_rate(self):
        # Bowling strike rate = balls bowled / wickets taken
        return self.balls / self.wickets if self.wickets > 0 else 0

    def __add__(self, other):
        # Combine wickets of two bowlers
        if isinstance(other, Bowler):
            return (
                f"Total wickets of {self.name} and {other.name} are: "
                f"{self.wickets + other.wickets}"
            )
        return "Both objects must be bowlers"

    def __len__(self):
        # Return total wickets taken
        return self.wickets

    def __str__(self):
        # Readable bowling record
        return f"""
        Name: {self.name},\tNationality: {self.nationality}
        Age: {self.age},\t\tIs Active: {self.is_active}
        Innings: {self.innings},\t\tFormat: {self.format}
        Balls Bowled: {self.balls},\tRuns Conceded: {self.runs}
        Wickets Taken: {self.wickets},\tBest Figures: {self.best_figures}
        Bowling Average: {self.calculate_average:.2f}\t
        Economy Rate: {self.calculate_economy:.2f}
        Strike Rate: {self.calculate_strike_rate:.2f}
        --------------------------------------
        """


# --------------------------------------------------
# Object Creation
# --------------------------------------------------

Gurbaz = Batsman("Rahmanullah Gurbaz", "Afghan", 24, True, 80, 2067, 1533, 0, 151)
Ibrahim = Batsman("Ibrahim Zadran", "Afghan", 24, True, 58, 1558, 1405, 7, 72)

Rashid = Bowler("Rashid Khan", "Afghan", 27, True, 108, 2462, 2492, 182, "5/3")
Farooqi = Bowler("Fazalhaq Farooqi", "Afghan", 25, True, 51, 1078, 1246, 63, "5/9")


# --------------------------------------------------
# Using the Objects
# --------------------------------------------------

print(Farooqi)
print(Rashid)
print(Gurbaz)
print(Ibrahim)
print()

print(f"Total wickets of Rashid: {len(Rashid)}")
print(f"Total runs of Gurbaz: {len(Gurbaz)}")
print()

print(Rashid + Farooqi)
print(Gurbaz + Ibrahim)
print()

print(Ibrahim + Farooqi)
print(Rashid + Gurbaz)
print()

print("Gurbaz's Strike Rate: ", Gurbaz.calculate_strike_rate)
print("Rashid Khan's Economy: ", Rashid.calculate_economy)

