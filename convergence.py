'''Plot the convergence of a Jaguar DFT calculation from the logfile using matplotlib
Doug Crandell-Indiana University 2014'''

import sys
import os
import matplotlib.pyplot as plt

def main(logfile):
    #Take logfile or calcid as input from command line
    data = open_file(logfile[0])
    energies, scaled = [], []
    for line in data.split('\n'):
        if line.strip().startswith("energy:"):
           line = (filter(None,line.split(' ')))
           energy = float(line[1]) * 627.509 #Convert energy from hartree to kcal/mol
           energies.append(energy)
    #Scale energies so that minimum energy is set at 0
    min_energy = min(energies)
    scaled = [energy - min_energy for energy in energies]

    plt.plot(range(1,len(scaled)+1),scaled)
    plt.ylabel('Energy change (kcal/mol)')
    plt.xlabel('Optimization Step')
    plt.title('Optimization Convergence')
    plt.show()

def open_file(file):
    if len(file.split('.')) > 1 and file.split('.')[1] == 'log':
            with open(file,'r') as f:
                data = f.read()
    else:
        try:
            outfile = os.getcwd() +'/' + file + '.log' #Get output file based on user input of calc_id
            with open (outfile, 'r') as f:
                data = f.read()
        except:
            print "The file does not exist!"
    return data

if __name__ == "__main__":
    main(sys.argv[1:])


