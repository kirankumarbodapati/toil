from toil import job
import time
import toil
#import subprocess
#import singularity
#import python3
#import pipelines
import os 

#import argparse
#import click
#from pipelines import no_of_cores


# def root():
#     pass

def fn1(job):
    time.sleep(30)
    command="singularity exec container.sif python3 pipelines.py"
    os.system(command) 

     
    
    '''instance_name = "instance_1"
    container_path="container.sif"
    command = f"singularity instance start {container_path} {instance_name}"'''
    '''command=f"singularity run instance://{instance_name}"
    command=f"singularity exec instance://{instance_name}"'''
    # subprocess.run(command, shell=True)
    # instance_command = f"singularity exec instance://instance_1 python3 your_script.py"
    # subprocess.run(instance_command, shell=True)

    # Stop the instance when done
    # subprocess.run(f"singularity instance stop {instance_name}", shell=True)
    # subprocess.run(f"singularity instance stop {instance_name}", shell=True)

    #job.fileStore.readGlobalFile("conatiner.sif",container_path)
    '''command="singularity exec conatiner.sif python3 pipelines.py"
    os.system(command)''' 
    a=2
    return a

def fn2(job):
    time.sleep(60)
    #container_path="container.sif"
    #job.fileStore.readGlobalFile("conatiner.sif",container_path)
    command="singularity exec container.sif python3 pipelines.py"
    os.system(command) 
    b=3
    return b

def fn3(job):
    time.sleep(70)
    #container_path="container.sif"
    #job.fileStore.readGlobalFile("conatiner.sif",container_path)
    command="singularity exec container.sif python3 pipelines.py"
    os.system(command) 
    c=4
    return c

def fn4(job,a,b):
    #container_path="container.sif"
    #job.fileStore.readGlobalFile("conatiner.sif",container_path)
    command="singularity exec container.sif python3 pipelines.py"
    os.system(command)
    d=a+b
    
    return d
  

def fn5(job,b,c):
    #container_path="container.sif"
    #job.fileStore.readGlobalFile("conatiner.sif",container_path)
    command="singularity exec container.sif python3 pipelines.py"
    os.system(command)
    e=b+c
    return e



#no_of_cores=int(input("Enter the number of cores you want to use:"))

# parser=argparse.ArgumentParser(description="Toil workflow")
# parser.add_argument('--n-cores', type=int, default=1, help="number of cores to be used")
# parser.add_argument("--logFile", type=str, help="Path to log file")
# args=parser.parse_args()



# root_job=job.FunctionWrappingJob(root,memory='100k',n_cores=args.n_cores)
# first_job=job.FunctionWrappingJob(job1,memory='100k',n_cores=args.n_cores)
# second_job=job.FunctionWrappingJob(job2,memory='100k',n_cores=args.n_cores)
# third_job=job.FunctionWrappingJob(job3,memory='100k',n_cores=args.n_cores)
# fourth_job=job.FunctionWrappingJob(job4)
# fifth_job=job.FunctionWrappingJob(job5)






        




    
  
    
    


















    

# if __name__=="__main__":
#     main()
    



