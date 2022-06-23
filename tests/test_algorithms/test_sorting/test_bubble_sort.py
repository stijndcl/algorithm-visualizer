from algorithm_visualizer.algorithms.presets.sorting import BubbleSort


def test_bubble_sort(set_random_seed):
    bs = BubbleSort(list(range(500)))
    for _ in bs.run():
        pass

    assert bs.data == sorted(bs.data)
