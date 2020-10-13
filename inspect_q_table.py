import pickle
import gym

env = gym.make("Taxi-v3").env
q_path = "./q_table.pickle"
state = int(input('Enter a number for the state you want to inspect: \n\n'))

def main():
    with open(q_path, 'rb') as f:
        q_table = pickle.load(f)
    env.s = state
    frame = env.render(mode='ansi')
    try:
        print(q_table[state])
        print(frame)
        print('Action Keys: 0 - South, 1 - North, 2 - East, 3 - West, 4 - Pickup, 5 - Dropoff')
    except:
        print('That state does not exist in the table. \n')


if __name__ == "__main__":
    main()
