import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import panda as pd

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / N

N=300

def load_data(text_dir,Color,N,Label):
    episode_reward = np.loadtxt(text_dir)
    episode_length=episode_reward.size
    print episode_length
    reward_smooth = running_mean(episode_reward,N)
    plt.plot(episode_reward,color=Color,alpha=0.2 )
    plt.plot(reward_smooth,color=Color,label=Label)
    plt.ylabel('episode_reward')
    plt.xlabel('episode')
    # plt.show()
    return plt

def main():
    load_data("/home/lsy/Desktop/Unreal_results/results.txt","red",N,"UNREAL")
    load_data("/home/lsy/Desktop/results/results.txt", "blue", N,"D1D2")
    plt.grid()
    plt.legend(bbox_to_anchor=(0.25, 1.0, 0.102, .102), loc=2,ncol=2, borderaxespad=0.)
    plt.show()
if __name__ == "__main__":
    main()
