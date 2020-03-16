import psutil
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--metric_cpu', nargs='?')
    parser.add_argument('-m', '--metric_mem', nargs='?')

    return parser


parser = createParser()
nameargs = parser.parse_args()

# print('Enter type metric(cpu/mem):')
# temp = input()
if nameargs.metric_cpu == 'cpu':
    print('system.cpu.idle ' + format(psutil.cpu_times().idle))
    print('system.cpu.user ' + format(psutil.cpu_times().user))
    print('system.cpu.guest ' + format(psutil.cpu_times().guest))
    print('system.cpu.iowait ' + format(psutil.cpu_times().iowait))
    print('system.cpu.stolen ' + format(psutil.cpu_times().steal))
    print('system.cpu.system ' + format(psutil.cpu_times().system))
elif nameargs.metric_mem == 'mem':
    print('virtual total ' + format(psutil.virtual_memory().total))
    print('virtual used ' + format(psutil.virtual_memory().used))
    print('virtual free ' + format(psutil.virtual_memory().free))
    print('virtual shared ' + format(psutil.virtual_memory().shared))
    print('swap total ' + format(psutil.swap_memory().total))
    print('swap used ' + format(psutil.swap_memory().used))
    print('swap free ' + format(psutil.swap_memory().free))
else:
    print("Enter (-c cpu) or (-m mem) parameter")
