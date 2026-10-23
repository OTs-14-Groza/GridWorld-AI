from gridworld import GridWorld
import random
class Agent():
    """
    An agent that selects actions using an epsilon-greedy policy.
    """
    def __init__(self):
        # Probability of exploration and exploitation
        self.epsilon = 0.2
        self.exploration = self.epsilon
        self.exploitation = 1 - self.epsilon
        
        # Create the environment and initialize its Q-table
        self.environment = GridWorld()
        self.environment.initialize_q_table()
    def explore(self):
        """Select a random action for exploration."""
        action = ['up','down','right','left']
        return random.choice(action)
    def exploit(self):
        """
        Select an action with the highest Q-value.
        Randomly break ties between equally valued actions.
        """
        # TODO: Complete exploitation logic
        # TODO: Fix state access and dictionary operations
        row, col = self.position
        action_value_pair = {}
        for pair in self.environment.q_table[row, col]:
            action_value_pair.append(pair.items())
        
    def choice(self):
        """
        Select exploration or exploitation based on epsilon.
        Return the chosen action.
        """
        # Choose a strategy using weighted probabilities
        result = random.choices(
            ['explore', 'exploit'],
            weights=[self.exploration,self.exploitation]
            )
        if result == ['explore']:
            action = self.explore()
        elif result == ['exploit']:
            action = self.exploit()
        return action