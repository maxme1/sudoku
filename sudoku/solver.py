from itertools import islice
from typing import Iterable

import numpy as np


class NotSolvable(ValueError):
    pass


def get_cell_size(field):
    return int(np.sqrt(len(field)))


def get_field_size(values):
    return int(np.sqrt(len(values)))


def propagate_constraints(field, i, j, value):
    mask = field[..., value]
    update_at = np.zeros_like(mask)

    # rows, cols
    update_at[i] = 1
    update_at[:, j] = 1

    # cell
    cell_size = get_cell_size(field)
    start = (np.array((i, j)) // cell_size) * cell_size
    stop = start + cell_size
    update_at[tuple(map(slice, start, stop))] = 1

    # except
    update_at[i, j] = 0

    # only where should remove
    update_at = update_at & mask
    mask[update_at] = 0

    if not field.any(-1).all():
        # no possible values
        raise NotSolvable

    # propagate
    update_at = update_at & (field.sum(-1) == 1)
    xs, ys = np.where(update_at)
    for i, j in zip(xs, ys):
        unique_value, = np.where(field[i, j])[0]
        propagate_constraints(field, i, j, unique_value)


def is_solved(field):
    return (field.sum(-1) == 1).all()


def make_suggestions(field):
    if is_solved(field):
        values = np.where(field)[2] + 1
        field_size = get_field_size(values)
        yield values.reshape(field_size, field_size)
        return

    variants = field.sum(-1).astype(float)
    variants[variants == 1] = np.inf
    idx = np.argmin(variants)
    i, j = np.unravel_index(idx, field.shape[:2])

    for value in range(len(field)):
        if field[i, j, value]:
            suggestion = field.copy()
            # suppose that the real value at (i,j) is value
            suggestion[i, j] = 0
            suggestion[i, j, value] = 1

            try:
                propagate_constraints(suggestion, i, j, value)
                yield from make_suggestions(suggestion)
            except NotSolvable:
                pass


def parse_input(text: str):
    values = text.split()
    field_size = get_field_size(values)
    if len(values) != field_size ** 2:
        raise ValueError('Field is not square.')

    field = np.ones([field_size] * 3, dtype=bool)

    initial = []
    for i, value in enumerate(values):
        if value != '?':
            i, j = np.unravel_index(i, field.shape[:2])
            value = int(value) - 1
            field[i, j] = 0
            field[i, j, value] = 1
            initial.append((i, j, value))

    return field, initial


def solve(text: str) -> Iterable[np.ndarray]:
    field, initial = parse_input(text)
    for v in initial:
        propagate_constraints(field, *v)

    return make_suggestions(field)


def print_solutions(text: str, max_solutions: int = None):
    solutions = solve(text)
    if max_solutions is not None:
        solutions = islice(solutions, max_solutions)

    for solution in solutions:
        for row in solution:
            print(*row)
        print()
