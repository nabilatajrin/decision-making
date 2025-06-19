# Causal AI with a Value Scorecard

def get_action_scores():
    """
    Define actions with scores on four value dimensions.
    Scores are on a scale from 0 to 10.
    You can adjust these values based on your personal judgment.
    """
    actions = {
        "nap": {
            "long_term_growth": 6,    # Rest can be beneficial but won't build skills
            "emotional_peace": 7,     # A gentle nap may soothe stress
            "mental_clarity": 8,      # Refreshes your mind after a short sleep
            "spiritual_return": 5     # Moderate spiritual benefit in self-care
        },
        "study": {
            "long_term_growth": 10,   # Strong impact on skill-building and progress
            "emotional_peace": 9,     # Can lead to pride and satisfaction
            "mental_clarity": 7,      # Requires focus but can clear doubts when successful
            "spiritual_return": 7     # Productive actions can align with your higher purpose
        },
        "scroll": {
            "long_term_growth": 2,    # Minimal benefit in personal growth
            "emotional_peace": 4,     # Provides short-term entertainment but often followed by regret
            "mental_clarity": 3,      # Generally distracts and may clutter your thoughts
            "spiritual_return": 2     # Often considered a waste of time in spiritual contexts
        }
    }
    return actions

def calculate_total_scores(actions):
    """Calculate the total score for each action."""
    total_scores = {}
    for action, factors in actions.items():
        total = sum(factors.values())
        total_scores[action] = total
    return total_scores

def choose_best_action(total_scores):
    """Choose the action with the highest total score."""
    best_action = max(total_scores, key=total_scores.get)
    return best_action, total_scores[best_action]

def display_decision(actions, total_scores):
    print("Value Scorecard for Decisions:\n")
    for action, factors in actions.items():
        print(f"Action: {action.upper()}")
        for factor, score in factors.items():
            print(f"   {factor.replace('_', ' ').capitalize()}: {score}/10")
        print(f"   -> Total Score: {total_scores[action]}/40\n")
    
    best_action, best_score = choose_best_action(total_scores)
    print(f"🤖 AI's Decision: **{best_action.upper()}** with a total score of {best_score}/40")
    print("\nThis is the most valuable option based on the defined consequences.")

# Main program
if __name__ == "__main__":
    actions = get_action_scores()
    total_scores = calculate_total_scores(actions)
    display_decision(actions, total_scores)
