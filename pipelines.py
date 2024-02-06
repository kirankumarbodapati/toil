#def main():
from toil_basic import  fn1,fn2,fn3,fn4,fn5
#from toil_basic import  first_job,second_job,third_job,fourth_job,fifth_job
from toil.job import Job

from toil.common import Toil
#from toil.lib.io import mkdtemp
import os 

#from toil_basic import job4,job5
#from toil_basic import parser,args
#from toil_basic import no_of_cores


# parser=argparse.ArgumentParser()
#parser.add_argument('--n-cores', type=int, default=1, help="number of cores to be used")
# args=parser.parse_args()
#jobstore: str= mkdtemp('my-job-store')
parser = Job.Runner.getDefaultArgumentParser()
parser.add_argument("--n-cores", type=int, default=1, help="number of cores to be used")
parser.add_argument("--enable-restart", action="store_true",help="restarts the failed jobs")
parser.add_argument("--no-job-cache", action="store_true", help="disabels job cache to keep workers running")
#parser.add_argument("--batchSystem", default="singleMachine", help="batch system to run jobs")
#parser.add_argument("--singularity", action="store_true", help="use Singularity container")

#parser.add_argument("--singularity-file", type=str, help="add a singularity file")
options = parser.parse_args()
options.logLevel = "INFO"
options.clean = "never"
'''options.batchSystem = "slurm"
options.batchSystemOptions = "slurm_script.sh"'''

#no_of_cores=int(input("Enter the number of cores you want to use:"))
root_job=Job()
job1=root_job.addChildJobFn(fn1,memory='100k',cores=options.n_cores)
job2=root_job.addChildJobFn(fn2,memory='100k',cores=options.n_cores)
job3=root_job.addChildJobFn(fn3,memory='100k',cores=options.n_cores)
job4=root_job.addFollowOnJobFn(fn4,job1.rv(),job2.rv(),memory='100k',cores=options.n_cores)
job5=root_job.addFollowOnJobFn(fn5,job2.rv(),job3.rv(),memory='100k',cores=options.n_cores)
    #root_job.addFollowOnJobFn(fourth_job,first_job.rv(),second_job.rv())
    #root_job.addFollowOnJobFn(fifth_job,second_job.rv(),third_job.rv())

with Toil(options) as toil:
       if options.restart:
              toil.restart()
       else:
              
           toil.start(root_job)
        # try:
        #     if options.restart:
        #      toil.restart()
        #     else:
        #      toil.start(root_job)
        # except NoSuchJobStoreException:
        #     print("no job store exists ")
        
        # finally:
        #     options.clear="never"
        #     toil.shutdownGraceful()






        


