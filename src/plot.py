from typing import List, Tuple
import matplotlib.pyplot as plt


def plot(
    solution: List[Tuple[int, float, float]],
    trajectory: List[float],
    title: str,
) -> None:
    """Plots a solution of the travelling salesman problem

    Parameters
    ----------
    solution : List[Tuple[int, float, float]]
        Solution to the travelling salesman problem in the format (id, x, y)
    trajectory : List[float]
        Evaluation of the best solution of each iteration of the hill climbing
        algorithm.
    title : str
        Title of the plot
    """

    x = [v[1] for v in solution]  # only x
    y = [v[2] for v in solution]  # only y

    fig = plt.figure(figsize=(12, 8))
    fig.suptitle(title, fontsize=14, fontweight="bold")

    ax1 = fig.add_subplot(121)
    ax1.plot(y + [y[0]], x + [x[0]], "--bo")  # seems like x and y are inverted

    ax2 = fig.add_subplot(122)
    ax2.plot(trajectory, "-r")