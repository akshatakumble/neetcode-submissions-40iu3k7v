class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for i in range(iterations):
            d = 2 * init #(derivative of x sq) and init is curr_guess
            init = init - d * learning_rate
        return round(init,5)
