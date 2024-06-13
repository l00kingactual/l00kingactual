# Import necessary components from TetraLogix files
from TetraLogixBit_table_cube import DecisionEngine, DataAnalyzer

class StrategyCube:
    def __init__(self):
        self.strategic_principles = [
            "Calculations", "Waging War by Stratagem", "Energy Conservation", 
            # More strategic principles...
        ]
        self.tactical_ideas = {
            # Tactical ideas mapped to generals...
        }
        self.decision_engine = DecisionEngine()
        self.data_analyzer = DataAnalyzer()

    def score_tactics(self, principle, tactics):
        # Use the TetraLogix DecisionEngine to score tactics based on a principle
        scores = self.decision_engine.evaluate_tactics(principle, tactics)
        return scores

    def ai_mi_dictionary(self):
        # Link each strategic principle to a set of tactical ideas using enhanced decision logic
        ai_dict = {}
        for principle in self.strategic_principles:
            ai_dict[principle] = {}
            for general, tactics in self.tactical_ideas.items():
                scores = self.score_tactics(principle, tactics)
                sorted_tactics = sorted(tactics, key=lambda x: scores[x], reverse=True)[:5]
                ai_dict[principle][general] = sorted_tactics
        return ai_dict

# Example usage
cube = StrategyCube()
ai_mi_dict = cube.ai_mi_dictionary()
for principle, tactics in ai_mi_dict.items():
    print(f"Strategic Principle: {principle}")
    for general, ideas in tactics.items():
        print(f"  {general}: {', '.join(ideas)}")
    print("\n")
