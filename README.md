# Script which prints basic information about OS to console

These instructions describe how to write a Python script to take metrics(CPU, Memory) from Linux and pack script into Docker container.

Ster One: prepare script
--------------
At this point, please refer to the script metrics.py in this repository.
This script accept a single parameter to specify which metrics set to print:

- cpu - prints CPU metrics
- mem - prints RAM metrics

CPU Metrics
Output:
  + system.cpu.idle 78.8
  + system.cpu.user 17.3
  + system.cpu.guest 0.0
  + system.cpu.iowait 1.3
  + system.cpu.stolen 0.0
  + system.cpu.system 2.5

Memory Metrics
Output:
  + virtual total 16712351744
  + virtual used 9190146048
  + virtual free 1391624192
  + virtual shared 287655116
  + swap total 0
  + swap used 0
  + swap free 0

Step Two: prepare Dockerfile
---------------
Describe the Dockerfile to package and execute our script. Now you are ready to build an image from this Dockerfile. 
Dockerfile and metrics.py are in one directory. Run:
  ```
  docker build -t python-metrics .
  ```
Step Three: run docker image
---------------
After your image has been built successfully, you can run it as a container. 
In your terminal, run the command ```docker images``` to view your images. You should see an entry for “python-metrics”. 
Run image to display CPU metrics(parameter -c cpu):
  ```
  docker run python-metrics -c cpu
  ```
Run image to display Memory metrics(parameter -m mem):
  ```
  docker run python-metrics -m mem
  ```
