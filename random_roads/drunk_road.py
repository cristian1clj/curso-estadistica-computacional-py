# Bokeh
from bokeh.plotting import figure, show

# Files
from drunk import TraditionalDrunk
from chart import Chart


def generate_graph(coordinates_list):
    graph = figure(title='Camino de borrachos', x_axis_label='x', y_axis_label='y')
    
    for coordinates in coordinates_list:
        x_vals = [point[0] for point in coordinates]
        y_vals = [point[1] for point in coordinates]

        graph.line(x_vals, y_vals)
    
    show(graph)


def movement(drunk, chart, steps):
    coordinates = []
    
    for _ in range(steps):
        chart.move_drunk(drunk)
        coordinate = chart.consult_coordinate(drunk)
        coordinates.append(coordinate)
    
    return coordinates


def simulate_walk(attemps, drunk_type, steps):
    drunk = drunk_type(name='Ban')
    start = (0, 0)
    coordinates_list = []
    
    for _ in range(attemps):
        chart = Chart()
        chart.add_drunk(drunk, start)
        coordinates = movement(drunk, chart, steps)
        coordinates_list.append(coordinates)
    
    return coordinates_list


def main(steps_list, attemps, drunk_type):
    coordinates_list = []
    
    for steps in steps_list:
        coordinates_list = simulate_walk(attemps, drunk_type, steps)
        generate_graph(coordinates_list)


def run():
    steps_list: list[int] = [10000]
    attempts: int = 100
    
    main(steps_list, attempts, TraditionalDrunk)


if __name__ == '__main__':
    run()