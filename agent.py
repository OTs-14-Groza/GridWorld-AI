from gridworld import GridWorld
import random
import copy
class Agent():
    """
    An agent that selects actions using an epsilon-greedy policy.
    """
    def __init__(self):
        # Probability of exploration and exploitation
        self.epsilon = 0.2
        self.exploration = self.epsilon
        self.exploitation = 1 - self.epsilon
        self.learning_rate = 0.1
        self.discount_factor = 0.9        
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
        row, col = self.environment.position
        store_q_value = []
        action_of_max_q_value = []
        for action in self.environment.q_table[(row, col)]: 
            store_q_value.append(self.environment.q_table[(row, col)][action])
        highest = max(store_q_value)
        for action in self.environment.q_table[(row, col)]:
            if self.environment.q_table[(row, col)].get(action) == highest:
                action_of_max_q_value.append(action)
        return random.choice(action_of_max_q_value)
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
        ## return result ## for testing purposes
    def update_q_table(self):
        """
        Update the Q-value for one action using the Q-learning rule.
        Handle terminal and non-terminal states separately.
        """
        alpha = self.learning_rate
        gamma = self.discount_factor

        # Store the current state before taking an action
        current_position = self.environment.position
        
        # Select and execute an action
        action = self.choice()
        next_position, reward, done = self.environment.step(action)
        q_value_next = []
        for movement in self.environment.q_table[next_position]:
            q_value_next.append(self.environment.q_table[next_position][movement])
        
        # Calculate the Q-value adjustment using the Bellman equation
        q_value_variable = alpha*(reward + gamma*max(q_value_next) - self.environment.q_table[current_position][action])
        if done == True:
            # Terminal state: update using only the immediate reward
            self.environment.q_table[current_position][action] += alpha*(reward - self.environment.q_table[current_position][action])
            return
        else:    
            # Non-terminal state: include discounted future rewards
            self.environment.q_table[current_position][action] += q_value_variable