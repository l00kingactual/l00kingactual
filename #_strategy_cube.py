import numpy as np

class StrategyCube:
    def __init__(self):
        self.strategic_principles = [
            "Calculations", "Waging War by Stratagem", "Energy Conservation", 
            "Adaptation to Circumstances", "Forces in Conflict", "Terrain and Situational Analysis",
            "Leadership and Command", "Attack by Stratagem", "Use of Energy",
            "Strategy of Attack", "Disposition of the Army", "Planning for Success",
            "Exploiting Opportunities", "Assessment of the Situation", "Flexibility in Deployment",
            "Securing Advantages", "Exploiting Weaknesses", "Adaptation to the Enemy",
            "Coordination and Communication", "Maintaining Morale", "Assessing Relative Strengths",
            "Conservation of Energy", "Expending Energy Wisely", "Timing and Opportunism",
            "Balancing Forces and Resources", "Strategic Maneuvering", "Understanding Strengths and Weaknesses",
            "Exploiting Enemy Weaknesses", "Protecting Vulnerabilities", "Maximizing Strengths",
            "Strategic Deception", "Maintaining Initiative", "Strategic Positioning",
            "Flexibility in Deployment", "Deception and Misdirection", "Speed and Agility",
            "Terrain Analysis", "Adaptation to Circumstances", "Variety of Tactics",
            "Deception and Surprise", "Exploiting Weaknesses", "Timing and Coordination",
            "Terrain Analysis", "Balance of Forces", "Effective Logistics", "Strategic Maneuvering",
            "Speed and Agility", "Terrain Analysis", "Security Measures", "Communication and Coordination",
            "Maintaining Morale", "Understanding Terrain", "Strategic Advantage", "Flexibility in Adaptation",
            "Deception and Misdirection", "Terrain Analysis", "Adaptation to Circumstances", "Exploiting Weaknesses",
            "Coordination and Communication"
        ]
        self.tactical_ideas = {
            "Guan Yu": [
                "Ambush at Jade Pass reimagined with drone surveillance and AI-predictive positioning to outmaneuver opponents in critical choke points.",
                "Flood Strategy at Fan Castle, utilizing environmental manipulation technologies to control water levels remotely for strategic advantage.",
                "Defense of Jing Province featuring network-centric warfare systems to enhance communication and coordination across a distributed force.",
                "Alliance with Sun Quan leveraging virtual war-gaming and real-time strategy optimizations driven by AI simulations to strengthen coalition forces.",
                "Brotherhood Oath at Peach Garden transformed into a decentralized command network, promoting unity and coordination through secure blockchain communications."
            ],
            "Zhang Fei": [
                "Stand at Changban Bridge now featuring automated defense systems and AI-guided artillery to hold strategic points with minimal manpower.",
                "Intimidation of Cao Cao's Troops using psychological operations enhanced by AI algorithms that analyze enemy morale and adapt propaganda in real-time.",
                "Rallying the Shu Forces by employing augmented reality training systems that enhance troop readiness and combat effectiveness.",
                "Guarding the River Passes with the use of aquatic drones for reconnaissance and underwater sabotage operations.",
                "Forced March Tactics optimized by AI for rapid deployment and energy efficiency, ensuring troops arrive battle-ready with optimized routes and schedules."
            ],
            "Zhao Yun": [
                "Rescue of Liu Shan, integrating personal exoskeleton suits for enhanced soldier protection and strength during critical extraction missions.",
                "Defense of Changban featuring cyber defense strategies to protect and control battlefield information flows.",
                "Advance on Cao Cao's Camp using stealth drones for reconnaissance and AI-coordinated precision strikes.",
                "Protection of the Standard now involving AI-driven quick response teams that adapt to dynamic battlefield conditions to secure key assets.",
                "Counterattack Techniques that use machine learning to analyze enemy tactics and develop counter-strategies in real-time."
            ],
            "Ma Chao": [
                "Charge at Tong Pass using advanced vehicle automation to coordinate armored assaults with precision and minimal risk to human operators.",
                "Coalition against Cao Cao now supported by real-time collaborative platforms that integrate intelligence from multiple sources for a unified strategy.",
                "Defection to Shu redefined with deepfake and other information warfare tools to disrupt enemy alliances without direct confrontation.",
                "Raids in Northwestern Campaign utilizing guerrilla tactics supported by local sensor networks for terrain advantage and ambush coordination.",
                "Guerrilla Warfare Tactics enhanced by grassroots intelligence networks, using community-driven data gathering and analysis to drive resistance operations."
            ],
            "Huang Zhong": [
                "Victory at Mount Dingjun employing satellite imagery and high-altitude drones for real-time strategic oversight and precision bombing.",
                "Old General's Charge featuring robotic units that mimic traditional cavalry charges, disrupting enemy lines with high-speed, high-impact tactics.",
                "Sniping Key Generals now involves long-range drones equipped with facial recognition to identify and neutralize high-value targets from a distance.",
                "Fortification Strategies using rapid-deployment building technologies that create instant defenses and fortified positions as needed.",
                "Longbow Ambushes updated with electromagnetic railguns that can be deployed in stealth positions, offering non-lethal options to incapacitate enemy forces at range."
            ]
        }


    def ai_mi_dictionary(self):
        # Linking each strategic principle to a set of tactical ideas
        ai_dict = {}
        for principle in self.strategic_principles:
            ai_dict[principle] = {}
            for general, tactics in self.tactical_ideas.items():
                ai_dict[principle][general] = np.random.choice(tactics, 5, replace=False).tolist()
        return ai_dict

# Example usage
cube = StrategyCube()
ai_mi_dict = cube.ai_mi_dictionary()
for principle, tactics in ai_mi_dict.items():
    print(f"Strategic Principle: {principle}")
    for general, ideas in tactics.items():
        print(f"  {general}: {', '.join(ideas)}")
    print("\n")
