# Bokeh
from bokeh.plotting import figure, show

# Files
from dice import Dice


def generate_graph(probabilities):
    x_vals = [element[0] for element in probabilities]
    y_vals = [element[1] for element in probabilities]
    
    graph = figure(x_axis_label='Dice sides', y_axis_label='probability', 
                   title='Dice sides probabilities')
    graph.line(x_vals, y_vals)
    
    show(graph)


def count_results(storage_dict, results):
    for key in results.keys():
        if results[key] > 0:
            try:
                storage_dict[key] += 1
            except KeyError:
                storage_dict[key] = 1
    
    return storage_dict


def calculate_probability(results_list, attempts):
    result = {}
    
    for results in results_list:
        result = count_results(result, results)
    
    for key, value in result.items():
        probability = value / attempts
        result[key] = probability
    
    return sorted(result.items())


def throw(dice):
    return dice.result()


def simulation(dice, throws):
    results = {}

    for _ in range(throws):
        result = throw(dice)
        
        try:
            results[result] += 1
        except KeyError:
            results[result] = 1
    
    return results


def main(sides, attempts, throws):
    dice = Dice(sides)
    results = []
    
    for _ in range(attempts):
        result = simulation(dice, throws)
        results.append(result)
    
    probabilities = calculate_probability(results, attempts)
    # generate_graph(probabilities)
    
    for element in probabilities:
        print(f'Probabilidad de obtener {element[0]} en {throws} lanzes: {element[1]}')


def run():
    sides: int = int(input('Ingrese el numero de lados del dado: '))
    throws: int = int(input('Ingrese el numero de lanzamientos: '))
    attempts: int = int(input('Cuantas veces correra la simulacion: '))
    
    main(sides, attempts, throws)


if __name__ == '__main__':
    run()