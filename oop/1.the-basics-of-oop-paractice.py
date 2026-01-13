class Batsman:
    def __init__(self, name, innings, runs, balls_faced, not_outs):
        self.name = name
        self.innings = innings
        self.runs = runs 
        self.balls_faced = balls_faced
        self.times_notout = not_outs
    
    def avrage(self):
        dismissals = self.innings - self.times_notout
        return self.runs/dismissals if dismissals > 0 else 0
    
    def strike_rate(self):
        return (self.runs/self.balls_faced)*100 if self.balls_faced>0 else 0

    def display_record(self): 
        print(f"\n{self.name}:")
        print(f"\t Innings: {self.innings}")
        print(f"\t Runs: {self.runs}")
        print(f"\t Balls Faced: {self.balls_faced}")
        print(f"\t Not Out: {self.times_notout}")
        print(f"\t Strike Rate: {self.strike_rate():.2f}")
        print(f"\t Batting Avrage: {self.avrage():.2f}")


player_1 = Batsman("Rahmanullah Gurbaz", 80, 2067, 1533, 0)
player_2 = Batsman("Ibrahim Zadran", 58, 1558, 1405, 7)
player_1.display_record()
player_2.display_record()