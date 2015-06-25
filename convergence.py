'''Plot the convergence of a Jaguar DFT calculation from the logfile using matplotlib
Doug Crandell-Indiana University 2015'''

import sys
import os
import matplotlib.pyplot as plt

def main(argv):
    data = open_file(argv[0])
    energies, delta, points, = [], [], []
    count = 0
    for line in data.split('\n'):
        if line.strip().startswith("energy:"):
           count += 1
           points.append(count)
           line = (filter(None,line.split(' ')))
           energy = float(line[1]) * 627.509 #Convert energy from hartree to kcal/mol
           energies.append(energy)
    x = min(energies)
    scaled = []
    for energy in energies:
        scaled.append(energy-x)
    plt.plot(points,scaled)
    #Set axis labels
    plt.ylabel('Energy change (kcal/mol)')
    plt.xlabel('Optimization Step')
    plt.title('Optimization Convergence')
    plt.show()

def open_file(file):
    if len(file.split('.')) > 1:
        if file.split('.')[1] == 'log':
            with open(file,'r') as f:
                data = f.read()
    else:
        try:
            outfile = os.getcwd() +'/' + file + '.log' #Get output file based on user input of calc_id
            print outfile
            with open (outfile, 'r') as f:
                data = f.read()
        except:
            print "The file does not exist!"
    return data

if __name__ == "__main__":
    main(sys.argv[1:])


