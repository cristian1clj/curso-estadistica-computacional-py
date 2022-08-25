# Bokeh
from bokeh.plotting import figure, show

# Files
from drunk import TraditionalDrunk
from coordiante import Coordiante
from chart import Chart


def movement(steps, drunk, chart):
    start = chart.consult_coordinate(drunk)
    
    for _ in range(steps):
        chart.move_drunk(drunk)
    
    return start.distance(chart.consult_coordinate(drunk))


def generate_graph(x, y):
    graph = figure(title='Drunk road', x_axis_label='steps', y_axis_label='distance')
    graph.line(x, y, legend='distancia media')
    
    show(graph)


def simulate_walk(steps, attemps, drunk_type):
    drunk = drunk_type(name='Ban')
    start = Coordiante(0, 0)
    distances = []
    
    for _ in range(attemps):
        chart = Chart()
        chart.add_drunk(drunk, start)
        simulation = movement(steps, drunk, chart)
        distances.append(round(simulation, 1))
    
    return distances


def main(steps_list, attemps, drunk_type):
    average_distance_list = []
    
    for steps in steps_list:
        distances = simulate_walk(steps, attemps, drunk_type)
        average_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        
        average_distance_list.append(average_distance)
        
        print(f'{drunk_type.__name__} caminata aleatoria de {steps} pasos')
        print(f'Media = {average_distance}')
        print(f'Maxima = {max_distance}')
        print(f'Minima = {min_distance}')
    
    generate_graph(steps_list, average_distance_list)


def run():
    steps_list: list[int] = [10, 100, 1000, 10000]
    attempts: int = 100
    
    main(steps_list, attempts, TraditionalDrunk)


if __name__ == '__main__':
    run()