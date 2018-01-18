'''
I'm not sure how to solve this using a specific DP solution
So let's just solve it with value iteration

Turns out the solution was like a memoized forward, exhaustive search
'''
import collections
import numpy as np

class ChoiceOfAreaEnv(object):

    def __init__(
            self,
            action_info=dict(
                a=20,
                b=8
            ),
            area_info=dict(
                x=dict(
                    a=3,
                    b=2
                ),
                y=dict(
                    a=-5,
                    b=-10
                ),
                z=dict(
                    a=-20,
                    b=5
                ),
            )):
        self.action_info = action_info
        self.action_info_keys = list(sorted(action_info.keys()))
        self.area_info = area_info
        # ironically, the areas are the actions
        # and the actions are states in this naming convention
        self.actions_list = list(sorted(area_info.keys()))
        # dummy start state
        self.area_info['none'] = {k:0 for k in self.action_info_keys}
        self._compute_states()  
           
    def _compute_states(self):
        '''
        Perform a DFS through the state space to find all the states in the mdp
        and store them in a class member.

        A state is defined by the following properties:
        power level for each action
        current area
        '''
        visited = set()
        unvisited = []
        unvisited.append(self.reset())
        while len(unvisited) > 0:
            state = unvisited.pop()
            visited.add(state)
            for action in self.actions(state):
                succ_costs = self.successors_and_costs(state, action)
                for (next_state, _) in succ_costs:
                    if next_state not in visited:
                       unvisited.append(next_state)
        self.states = list(sorted(visited))
        self.n_states = len(visited)

    def reset(self):
        '''
        Return the start state
        '''
        state = [self.action_info[k] for k in self.action_info_keys]
        state += ['none']
        return tuple(state)

    def actions(self, state):
        return [a for a in self.actions_list if a != state[-1]]

    def successors_and_costs(self, state, action):
        '''
        Given a state and an action returns a list of tuples
        each tuple in that list is a possible next state and the cost of 
        moving to that state

        state is a tuple indicating the power level of the different actions
        also the state has the current area in it 
        action is a key into area_infos

        in this case the next state is a deterministic function of the current 
        state and action
        '''
        powers, area = state[:-1], state[-1]
        # if terminal, return empty list
        if any([p <= 0 for p in powers]):
            return []
        next_state = []
        reward = 0 if area == 'none' else 1
        for i, k in enumerate(self.action_info_keys):
            cur = powers[i]
            nxt = cur + self.area_info[action][k]
            next_state.append(nxt)
        next_state = tuple(next_state + [action])
        return [(next_state, reward)]

def value_iteration(mdp, max_itr=10, thresh=1e-3):
    v = collections.defaultdict(int)
    for t in range(max_itr):
        res = 0
        for s in mdp.states:
            opt_a_v = -np.inf
            for a in mdp.actions(s):
                cur_a_v = 0
                for succ, cost in mdp.successors_and_costs(s, a):
                    cur_a_v += cost + v[succ]
                if cur_a_v >= opt_a_v:
                    opt_a_v = cur_a_v
            res = max(res, opt_a_v - v[s])
            v[s] = opt_a_v
        if res < thresh:
            break
    return v

if __name__ == '__main__':
    env = ChoiceOfAreaEnv()
    v = value_iteration(env)
    sorted_states = sorted(v.items(), key=lambda t: t[1], reverse=True)
    print(sorted_states)

    action_info=dict(
        a=20,
        b=8,
        c=20
    )
    area_info=dict(
        x=dict(
            a=3,
            b=2,
            c=5
        ),
        y=dict(
            a=-5,
            b=-10,
            c=-6
        ),
        z=dict(
            a=-20,
            b=5,
            c=-10
        ),
        w=dict(
            a=-5,
            b=5,
            c=-10
        ),
    )

    print()
    env = ChoiceOfAreaEnv(
        action_info=action_info,
        area_info=area_info
    )
    v = value_iteration(env)
    sorted_states = sorted(v.items(), key=lambda t: t[1], reverse=True)
    print(sorted_states)
