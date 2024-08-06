import numpy as np

class StrategicPlanning:
    def __init__(self):
        self.strategic_groups = {
            "Offensive Strategies": ["Waging War by Stratagem", "Attack by Stratagem", "Exploiting Opportunities", "Strategy of Attack"],
            "Defensive Measures": ["Energy Conservation", "Adaptation to Circumstances", "Securing Advantages", "Protection of Vulnerabilities"],
            "Leadership and Command": ["Leadership and Command", "Maintaining Morale", "Coordination and Communication"],
            "Terrain and Movement": ["Terrain Analysis", "Forces in Conflict", "Terrain and Situational Analysis", "Flexibility in Deployment"],
            "Tactical Execution": ["Use of Energy", "Exploiting Weaknesses", "Speed and Agility", "Timing and Coordination", "Strategic Maneuvering"],
            # Add new groups with enhanced sophistication and future technology focus
            "Information Dominance": ["Cyber Operations", "Electronic Warfare"],
            "Energy and Resource Strategy": ["Resource Allocation Models", "Renewable Energy Tactics"],
            "Human Enhancement and Robotics": ["Exoskeletons in Combat", "AI Assisted Training"],
            "Environmental and Non-traditional Warfare": ["Climate Change Warfare", "Urban Combat Innovations"],
            "Space and Extraterrestrial Operations": ["Orbital Defense", "Lunar Resource Battles"]
        }
        self.tactical_ideas = {
            "Guan Yu": ["AI-Driven Surveillance", "Quantum Encrypted Communications", "Blockchain Coordination", "Drone Warfare"],
            "Zhang Fei": ["Cyber Defense", "Robotic Engineers", "Psychological Warfare", "Stealth Operations"],
            "Zhao Yun": ["Exoskeleton Deployment", "Rapid Deployment Tactics", "Laser Weapons", "Telecommunication Interference"],
            "Ma Chao": ["Guerrilla Tactics", "Deepfake PsyOps", "Radar Jamming", "Hypersonic Missiles"],
            "Huang Zhong": ["Sniper Drones", "Satellite Reconnaissance", "EMP Attacks", "High-altitude Warfare"]
        }

    def score_tactics(self, principle, tactics):
        """ Score tactics based on strategic principle alignment, technological relevance, and predictive effectiveness."""
        base_scores = {tactic: np.random.uniform(0.5, 0.7) for tactic in tactics}  # Base score influenced by random but within a higher range

        # Modify score based on principle-specific adjustments
        principle_adjustments = {
            "Offensive Strategies": 0.2,
            "Defensive Measures": 0.1,
            "Leadership and Command": 0.15,
            "Terrain and Movement": 0.05,
            "Tactical Execution": 0.1
        }
        
        adjustment_factor = principle_adjustments.get(principle, 0)  # Default to no adjustment if principle is not recognized
        
        # Apply technological and future context adjustments
        for tactic in tactics:
            tech_factor = 0.05 if "AI" in tactic or "drone" in tactic else 0
            future_factor = 0.05 if "quantum" in tactic or "cyber" in tactic else 0
            base_scores[tactic] += (adjustment_factor + tech_factor + future_factor)
            base_scores[tactic] = min(base_scores[tactic], 1.0)  # Ensure score does not exceed 1

        return base_scores
    
    def ai_mi_dictionary(self):
        ai_dict = {}
        for principle, groups in self.strategic_groups.items():
            ai_dict[principle] = {}
            for general, tactics in self.tactical_ideas.items():
                scores = self.score_tactics(principle, tactics)
                # Filter and select tactics that align with the current strategic group
                relevant_tactics = [tactic for tactic in tactics if tactic in groups]
                sorted_tactics = sorted(relevant_tactics, key=lambda x: scores[x], reverse=True)[:5]
                ai_dict[principle][general] = sorted_tactics
        return ai_dict

# Example instantiation and method usage
sp = StrategicPlanning()
print(sp.ai_mi_dictionary())
