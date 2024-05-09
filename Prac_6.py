import random

class StockMarketExpertSystem:
    def __init__(self, moving_average, rsi):
        self.moving_average = moving_average
        self.rsi = rsi

    def recommend_action(self):
        if self.moving_average == 'crossover' and self.rsi == 'overbought':
            return "Sell"
        elif self.moving_average == 'crossover' and self.rsi == 'oversold':
            return "Buy"
        elif self.moving_average == 'crossover':
            return "Hold"
        elif self.rsi == 'overbought':
            return "Hold"
        elif self.rsi == 'oversold':
            return "Buy"
        else:
            return "No clear recommendation"

def main():
    # Generate random indicators (for demonstration purposes)
    moving_average = random.choice(['crossover', 'no_crossover'])
    rsi = random.choice(['overbought', 'oversold', 'normal'])

    expert_system = StockMarketExpertSystem(moving_average, rsi)
    action = expert_system.recommend_action()

    print("Moving Average:", moving_average)
    print("RSI:", rsi)
    print("Recommendation:", action)

if __name__ == "__main__":
    main()
