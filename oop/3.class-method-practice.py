class Batsman:
    
    format = "T20I"
    no_of_batsmen = 0

    def __init__(self, name, innings, runs, balls_faced, not_outs):
        self.name = name
        self.innings = innings
        self.runs = runs 
        self.balls_faced = balls_faced
        self.times_notout = not_outs
        # Updating the number of players every time a new batsman is added. 
        Batsman.no_of_batsmen += 1

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

    @classmethod
    def change_format(cls, format): 
        cls.format = format
    
    @classmethod
    def data_from_string(cls, str_data): 
        
        name, innings, runs, balls_faced, not_outs = str_data.split(',')
        return cls(name, int(innings), int(runs), int(balls_faced), int(not_outs))

    @staticmethod
    def compare_batsman(b1, b2): 
        b1_sr = b1.strike_rate()
        b2_sr = b2.strike_rate()
        b1_avg = b1.avrage()
        b2_avg = b2.avrage()

        print("\n------------------------")
        print("Comparing Two players")


        print(f" {b1.name} vs {b2.name}")
    
        print("\tStrike rate: ")
        print(f"\t\t{b1.name} -> {b1_sr:.2f}")
        print(f"\t\t{b2.name} -> {b2_sr:.2f}")
        print("\n\tAvrage: ")
        print(f"\t\t{b1.name} -> {b1_avg:.2f}")
        print(f"\t\t{b2.name} -> {b2_avg:.2f}")
        
        print("\nResult: ")
        if b1_sr>b2_sr: 
            print(f"\t{b1.name} has better strike rate")
        elif b2_sr>b1_sr: 
            print(f"\t{b2.name} has better strike rate")
        if b1_avg>b2_avg: 
            print(f"\t{b1.name} has better avrage")
        elif b2_avg>b1_avg: 
            print(f"\t{b2.name} has better avrage")
        if b1_sr>b2_sr and b1_avg>b2_avg: 
            print(f"\t{b1.name} is the clear winner in both strike rate and avrage category")
        elif b1_sr<b2_sr and b1_avg<b2_avg:
            print(f"\t{b2.name} is the clear winner in both strike rate and avrage category")
        elif b1_sr==b2_sr and b1_avg == b2_avg: 
            print("\tBoth batsmen have same strike rate and avrage")

player_1 = Batsman("Rahmanullah Gurbaz", 80, 2067, 1533, 0)
player_2 = Batsman("Ibrahim Zadran", 58, 1558, 1405, 7)

print()
print(f"Format: {Batsman.format}")
player_1.display_record()
player_2.display_record()


Batsman.change_format("ODI")
print(f"\nNew Format: {Batsman.format}")

player1_str = "Rahmat Shah Zurmatai,125,4034,5661,6"
player_3 = Batsman.data_from_string(player1_str)
player_3.display_record()

print(f"Players: {Batsman.no_of_batsmen}")


Batsman.compare_batsman(player_1, player_2)