from typing import Callable, Generator, List, Tuple, TypeVar

# Generic solution type T
T = TypeVar("T")


def hill_climbing(
    initial: T,
    operator: Generator[T, T, None],
    evaluate: Callable[[T], float],
    equals: Callable[[T, T], bool],
) -> Tuple[T, List[T]]:
    """Optimizes a solution for a problem by iteratively improving it

    Given a solution to a problem, this function iteratively generate new solutions
    with the given operator(s), improving the best one so far until the point there
    is no more improvement.

    Parameters
    ----------
    initial : T
        The initial solution that we want improve on using the hill climbing
        naive algorithm.
    operator : Generator[T, T, None]
        A python generator function that yields each new solution that comes from
        applying the operator over the current best solution.
    evaluate : Callable[[T], float]
        It evaluates the score of a solution. The goal here is maximizing, climbing,
        so the evaluation is a number that represents how good a solution is.
        The bigger the better.
    equals : Callable[[T, T], bool]
        A function that returns true if and only if two solutions are the same.

    Returns
    -------
    Tuple[T, List[T]]
        A tuple where the first element is the best solution found and the second
        element is the list of optimizing steps from the initial solution to the
        best one.
    """
    # Once we start, the best known solution is the initial one
    best_solution, best_score = initial, evaluate(initial)
    history = [initial]  # Let's record all solutions so that we can revisit later

    while True:
        # stores last best solution for deciding whether we should stop or not
        prev_best = best_solution
        next_solutions = [solution for solution in operator(best_solution)]

        # for each new solution that the operator generated
        for solution in next_solutions:
            if evaluate(solution) > best_score:  # if it improves, replace the best
                best_solution, best_score = solution, evaluate(solution)
                history.append(best_solution)
        if equals(best_solution, prev_best):
            break  # if there is no improvement, then we are done, finish it
    return best_solution, history
