"""
MIT License

Copyright (c) 2017 cgalleguillosm, AlessioNetti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from time import clock as _clock, sleep as _sleep
from datetime import datetime
from abc import abstractmethod, ABC
from accasim.utils.reader_class import reader
from accasim.utils.misc import CONSTANT, watcher_daemon, DEFAULT_SIMULATION, load_config, path_leaf, clean_results
from accasim.utils.visualization_class import scheduling_visualization
from accasim.base.event_class import event_mapper
from accasim.base.resource_manager_class import resources_class, resource_manager
from accasim.base.scheduler_class import scheduler_base
from accasim.base.event_class import job_factory
from accasim.base.additional_data import additional_data
from threading import Thread, Event as THEvent
from os import getpid as _getpid, path as _path, makedirs as _makedirs
from psutil import Process as _Process
from _functools import reduce
import inspect
import asyncio

class simulator_base(ABC):

    def __init__(self, _resource_manager, _reader, _job_factory, _dispatcher, _additional_data, config_file=None, **kwargs):
        """
        Simulator base constructor
        @param _resource_manager: Resource manager class instantiation
        @param _reader: Reader class instantiation
        @param _job_factory: Job Factory instantiation
        @param _dispatcher: Dispatcher instantiation
        @param config_file: Path to the config file in json format.
        @param ****kwargs: Dictionary of key:value parameters to be used in the simulator. It overwrites the current parameters. All parameters will be available on the constant variable    
        """
        self.constants = CONSTANT()
        self.define_default_constants(config_file, **kwargs)
        self.real_init_time = datetime.now()
        assert(isinstance(_reader, reader))
        self.reader = _reader
        assert(isinstance(_resource_manager, resource_manager))
        self.resource_manager = _resource_manager
        assert(isinstance(_job_factory, job_factory))
        assert(self.check_request(_job_factory.attrs_names)), 'System resources must be included in Job Factory descrpition.'
        self.job_factory = _job_factory
        assert(isinstance(_dispatcher, scheduler_base))
        self.dispatcher = _dispatcher

        self.mapper = event_mapper(self.resource_manager)
        self.additional_data = self.additional_data_init(_additional_data)
        
        self.show_config()
        if self.constants.OVERWRITE_PREVIOUS:
            self.remove_previous()
        
    @abstractmethod
    def start_simulation(self):
        """
        Simulation initialization
        """
        raise NotImplementedError('Must be implemented!')

    @abstractmethod
    def load_events(self):
        """
        Method that loads the job from a datasource. Check the default implementation in the hpc_simulator class.
        """
        raise NotImplementedError('Must be implemented!')
    
    def additional_data_init(self, _additional_data):
        """
        Initializes the additional_data classes or set the event manager in the objects  
        @param _additional_data: A list of additional_data objects or classes
        @return: Return a list with all the additional_data objects ready to be executed
        """
        _ad = []
        for ad in _additional_data:
            if isinstance(ad, additional_data):
                ad.set_event_manager(self.mapper)
                _ad.append(ad)
            elif issubclass(ad, additional_data):
                _ad.append(ad(self.mapper))
            else:
                raise('Additional data class must be a subclass of the additional_data class')
        return _ad

    def check_request(self, attrs_names):
        """
        Verifies that the job factory attributes can be supported by the system resurces.
        
        @return: True if attributes are supported, False otherwise.
          
        """
        _system_resources = self.resource_manager.resources.system_resource_types
        for _res in _system_resources:
            if not(_res in attrs_names):
                return False
        return True
    
    def generate_enviroment(self, config_path):
        """
        Generated the syntethic system from the config file
        
        @param config_path: Path the config file
        
        @return: resource manager object.  
        """        
        config = load_config(config_path)
        resources = resources_class(**config)
        return resources.resource_manager()
    
    def define_filepaths(self, **kwargs):
        """
        Add to the kwargs useful filepaths. 
        """
        kwargs['WORKLOAD_FILENAME'] = path_leaf(kwargs['WORKLOAD_FILEPATH'])[1]
        if 'RESULTS_FOLDER_PATH' not in kwargs:
            script_path, script_name = path_leaf(inspect.stack()[-1].filename) 
            rfolder = kwargs.pop('RESULTS_FOLDER_NAME')
            kwargs['RESULTS_FOLDER_PATH'] = _path.join(script_path, rfolder)
        self.create_folder(kwargs['RESULTS_FOLDER_PATH'])
        return kwargs
        
    def create_folder(self, path):
        """
        Create folder if it does not exists. Pass to misc
        
        @param path: Name of the folder
        @return: Path of the created folder 
        """
        if not _path.exists(path):
            _makedirs(path)
        return path
    
    def set_workload_input(self, workload_path, **kwargs):
        """
        Create the reader object
        @param workload_path: Path to the workload
        @param ****kwargs: extra arguments
        
        @return: A reader object         
        """
        return reader(workload_path, **kwargs)
    
    def prepare_arguments(self, possible_arguments, arguments):
        """
        Verifies arguments for a specific instantation and create the dictionary. *Move to misc
        @param possible_arguments: Required arguments.
        @param arguments: Available arguments.  
        """
        return {k:v for k, v in arguments.items() if k in possible_arguments}
    
    def define_default_constants(self, config_filepath, **kwargs):
        """
        Defines the default constants of the simulator, and update if the user gives new values.
        
        @param config_filepath: Path to the config file in json format 
        """
        config = DEFAULT_SIMULATION.parameters
        for k, v in config.items():
            if k not in kwargs:
                kwargs[k] = v
        if config_filepath:
            for k, v in load_config(config_filepath).items():
                kwargs[k] = v
        kwargs = self.define_filepaths(**kwargs)
        self.constants.load_constants(kwargs)
        
    def show_config(self):
        """
            Shows the current simulator config
        """
        print('Initializing the simulator')
        print('Settings: ')
        print('\tSystem Configuration file: {}'.format(self.constants.SYS_CONFIG_FILEPATH))
        print('\tWorkload file: {}'.format(self.constants.WORKLOAD_FILEPATH))
        print('\tResults folder: {}{}.'.format(self.constants.RESULTS_FOLDER_PATH, ', Overwrite previous files' if self.constants.OVERWRITE_PREVIOUS else ''))
        print('\t\t ({}) Dispatching Plan Output. Prefix: {}'.format(self.on_off(self.constants.SCHEDULING_OUTPUT), self.constants.SCHED_PREFIX))
        print('\t\t ({}) Statistics Output. Prefix: {}'.format(self.on_off(self.constants.STATISTICS_OUTPUT), self.constants.STATISTICS_PREFIX))
        print('\t\t ({}) Dispatching Plan. Pretty Print Output. Prefix: {}'.format(self.on_off(self.constants.PPRINT_OUTPUT), self.constants.PPRINT_PREFIX))
        print('\t\t ({}) Benchmark Output. Prefix: {}'.format(self.on_off(self.constants.BENCHMARK_OUTPUT), self.constants.BENCHMARK_PREFIX))
        print('Ready to Start')
        
    def on_off(self, state):
        """
        True: ON, False: OFF
        Just for visualization purposes.
        
        @param state: State of a constant. True or False 
        """
        return 'ON' if state else 'OFF'
    
    def remove_previous(self):
        """
        To clean the previous results.
        """
        _wouts = [(self.constants.SCHEDULING_OUTPUT, self.constants.SCHED_PREFIX), (self.constants.STATISTICS_OUTPUT, self.constants.STATISTICS_PREFIX),
            (self.constants.PPRINT_OUTPUT, self.constants.PPRINT_PREFIX), (self.constants.BENCHMARK_OUTPUT, self.constants.BENCHMARK_PREFIX)]
        
        _paths = [_path.join(self.constants.RESULTS_FOLDER_PATH, _prefix + self.constants.WORKLOAD_FILENAME) for state, _prefix in _wouts if state]            
        clean_results(*_paths)


class hpc_simulator(simulator_base):
    """
    Default implementation of the simulator_base class.    
    """
    def __init__(self, sys_config, _scheduler, workload=None, _resource_manager=None, _reader=None, _job_factory=None, _additional_data=[], _simulator_config=None, overwrite_previous=True,
        scheduling_output=True, pprint_output=False, benchmark_output=False, statistics_output=True, show_statistics=True, **kwargs):
        """
        Constructor of the HPC Simulator class.
        @param sys_config: Filepath to the synthetic system configuration. Used by the resource manager to create the system.
        @param _scheduler: Dispatching method
        @param workload: Filepath to the workload, it is used by the reader. If a reader is not given, the default one is used.
        @param _resource_manager: Optional. Instantiation of the resource_manager class.
        @param _reader: Optional. Instantiation of the reader class.
        @param _job_factory: Optional. Instantiation of the job_factory class.
        @param _additional_data: Optional. Array of Objects or Classes of additional_data class.  
        @param _simulator_config: Optional. Filepath to the simulator config. For replacing the misc.DEFAULT_SIMULATION parameters.
        @param overwrite_previous: Default True. Overwrite previous results. 
        @param scheduling_output: Default True. Dispatching plan output. Format modificable in DEFAULT_SIMULATION  
        @param pprint_output: Default False. Dispatching plan output in pretty print version. Format modificable in DEFAULT_SIMULATION
        @param benchmark_output: Default False. Measurement of the simulator and dispatcher performance.
        @param statistics_output: Default True. Statistic of the simulation.
        @param show_statistics: Default True. Show Statistic after finishing the simulation.
        @param **kwargs: Optional parameters to be included in the Constants.
        
        """
        kwargs['OVERWRITE_PREVIOUS'] = overwrite_previous
        kwargs['SYS_CONFIG_FILEPATH'] = sys_config
        kwargs['WORKLOAD_FILEPATH'] = workload
        kwargs['SCHEDULING_OUTPUT'] = scheduling_output
        kwargs['PPRINT_OUTPUT'] = pprint_output
        kwargs['BENCHMARK_OUTPUT'] = benchmark_output
        kwargs['STATISTICS_OUTPUT'] = statistics_output
        kwargs['SHOW_STATISTICS'] = show_statistics

        if not _resource_manager:
            _resource_manager = self.generate_enviroment(sys_config)
        if not _job_factory:
            _jf_arguments = ['job_class', 'job_attrs', 'job_mapper']
            args = self.prepare_arguments(_jf_arguments, kwargs)
            _job_factory = job_factory(_resource_manager, **args)
        if 'tweak_function' not in kwargs:
            kwargs['tweak_function'] = self.default_tweak_function
        if workload and not _reader:
            _reader_arguments = ['max_lines']
            args = self.prepare_arguments(_reader_arguments, kwargs)
            _reader = self.set_workload_input(workload, **args)
        if not isinstance(_additional_data, list):
            assert(isinstance(_additional_data, additional_data) or issubclass(_additional_data, additional_data)), 'Only subclasses of additional_data class are acepted as _additional_data argument '
            _additional_data = [_additional_data]
            
        _scheduler.set_resource_manager(_resource_manager)
        
        simulator_base.__init__(self, _resource_manager, _reader, _job_factory, _scheduler, _additional_data, config_file=_simulator_config, **kwargs)
        
        self.start_time = None
        self.end_time = None
        self.max_sample = 2
        self.daemons = {}
        self.loaded_jobs = 0
               
    def monitor_datasource(self, _stop):
        '''
        runs continuously and updates the global data
        Useful for daemons
        @param _stop: Signal for stop 
        '''
        while (not _stop.is_set()):
            self.constants.running_at['current_time'] = self.mapper.current_time
            self.constants.running_at['running_jobs'] = {x: self.mapper.events[x] for x in self.mapper.running}
            _sleep(self.constants.running_at['interval'])
    
    def start_simulation(self, init_unix_time, watcher=False, visualization=False, **kwargs):
        """
        Initializes the simulation
        @param init_unix_time: Adjustement for job timings. If the first job corresponds to 0, the init_unix_time must corresponds to the real submit time of the workload. Otherwise, if the job contains the real submit time, init_unix_time is 0.
        @param watcher: Initializes the watcher. 
        @param visualization: Initializes the running jobs visualization using matplotlib.
        @param **kwargs: a 'tweak_function' to deal with the workloads.
         
        """
        if visualization:
            running_at = {
                'interval': 1,
                'current_time': self.mapper.current_time,
                'running_jobs': {}
            }
            self.constants.load_constant('running_at', running_at)
            _stop = THEvent()
            monitor = Thread(target=self.monitor_datasource, args=[_stop])
            monitor.daemon = True
            self.daemons['visualization'] = {
                'class': scheduling_visualization,
                'args': [(None, 'constants.running_at'), (None, 'resource_manager.resources.system_capacity',)],
                'object': None
            }
            monitor.start()

            
        if watcher:
            functions = {
                'usage_function': self.mapper.usage,
                'availability_function': self.mapper.availability,
                'simulated_status_function': self.mapper.simulated_status,
                'current_time_function': self.mapper.simulated_current_time
            }
            self.daemons['watcher'] = {
                'class': watcher_daemon,
                'args': [self.constants.WATCH_PORT, functions],
                'object': None
            }
        self.reader.open_file()

        kwargs['init_unix_time'] = init_unix_time

        simulation = Thread(target=self.start_hpc_simulation, kwargs=kwargs)
        simulation.start()

        # Starting the daemons
        self.daemon_init()
        simulation.join()
        # Stopping the daemons    
        [d['object'].stop() for d in self.daemons.values() if d['object']]
        if visualization:
            _stop.set()
        
    def default_tweak_function(self, _dict, init_unix_time):
        """
            Function will disappear. It will be part of the default SWF reader
        """
        # At this point, where this function is called, the _dict object have the assignation from the log data.
        # As in the SWF workload logs the numbers of cores are not expressed, just the number of requested processors, we have to tweak this information
        # i.e we replace the number of processors by the number of requested cores.
        _processors = _dict.pop('requested_number_processors') if _dict['requested_number_processors'] != -1 else _dict.pop(
            'allocated_processors')
        _memory = _dict.pop('requested_memory') if _dict['requested_memory'] != -1 else _dict.pop('used_memory')
        # For this system configuration. Each processor has 2 cores, then total required cores are calculated as
        # required_processor x 2 cores =  required cores of the job
        _dict['core'] = _processors * 2
        # The requested memory is given for each processor, therefore the total of requested memory is calculated as memory x processors = required memory of the job
        _dict['mem'] = _memory * _processors
        # If the following keys are not given, these are calculated by the job factory with the previous data
        # In this dataset there is no way to know how many cores of each node where requested, by default both cores are requested by processor
        # Each node has two processor, then it is possible to alocate upto 2 processor by node for the same job.
        _dict['requested_nodes'] = _processors
        _dict['requested_resources'] = {'core': 2, 'mem': _memory}
        # A final and important tweak is modifying the time corresponding to 0 time. For this workload as defined in the file
        # the 0 time corresponds to Sun Jul 28 09:04:05 CEST 2002 (1027839845 unix time)
        _dict['submit_time'] = _dict.pop('submit_time') + init_unix_time
        assert (
        _dict['core'] >= 0), 'Please consider to clean your data cannot exists requests with any info about core request.'
        assert (
        _dict['mem'] >= 0), 'Please consider to clean your data cannot exists requests with any info about mem request.'
        return _dict
        
    def start_hpc_simulation(self, _debug=False, tweak_function=None, init_unix_time=0):
        """
            Initializes the simulation in a new thread. It is called by the start_timulation using its arguments.
            @param _debug: Debugging flag
        """
        
        # TODO move to the default swf reader
        if tweak_function:
            assert(callable(tweak_function)), 'tweak_function argument must be a function.'
            self.tweak_function = tweak_function
        else:
            self.tweak_function = self.constants.tweak_function
        self.init_unix_time = init_unix_time
                    
        
        #=======================================================================
        # Load events corresponding at the "current time" and the next one
        #=======================================================================
        event_dict = self.mapper.events
        self.start_time = _clock()
        self.constants.load_constant('start_time', self.start_time)

        print('Starting the simulation process.')
        
        self.load_events(event_dict, self.mapper, _debug, self.max_sample)
        events = self.mapper.next_events()

        #=======================================================================
        # Loop until there are not loaded, queued and running jobs
        #=======================================================================
        while events or self.mapper.has_events():
            _actual_time = self.mapper.current_time
            
            benchStartTime = _clock() * 1000
            
            if _debug:
                print('{} INI: Loaded {}, Queued {}, Running {}, Finished {}'.format(_actual_time, len(self.mapper.loaded), len(self.mapper.queued), len(self.mapper.running), len(self.mapper.finished)))
            self.mapper.release_ended_events(event_dict)
            
            #===================================================================
            # External behavior
            #===================================================================
            self.execute_additional_data()
            
            queuelen = len(events)
            schedStartTime = _clock() * 1000
            schedEndTime = schedStartTime
            if events:
                if _debug:
                    print('{} DUR: To Schedule {}'.format(_actual_time, len(events)))
                to_dispatch = self.dispatcher.schedule(self.mapper.current_time, event_dict, events, _debug)
                # to_dispatch = self.dispatcher.schedule(self.mapper.current_time, event_dict, events, len(self.mapper.finished) > 15000)
                if _debug:
                    print('{} DUR: To Dispatch {}. {}'.format(_actual_time, len(to_dispatch), self.resource_manager.resources.usage()))
                time_diff = 0
                schedEndTime = _clock() * 1000
                try:
                    self.mapper.dispatch_events(event_dict, to_dispatch, time_diff, _debug)
                except AssertionError as e:
                    print('{} DUR: {}'.format(_actual_time, e))
                    print('{} DUR: Loaded {}, Queued {}, Running {}, Finished {}'.format(_actual_time, len(self.mapper.loaded), len(self.mapper.queued), len(self.mapper.running), len(self.mapper.finished)))
                    _exit()
                                   
            if _debug:
                print('{} END: Loaded {}, Queued {}, Running {}, Finished {}'.format(_actual_time, len(self.mapper.loaded), len(self.mapper.queued), len(self.mapper.running), len(self.mapper.finished)))

            #===================================================================
            # Loading next jobs
            #===================================================================
            if len(self.mapper.loaded) < 10:
                sample = self.max_sample if(len(self.mapper.loaded) < self.max_sample) else 2
                self.load_events(event_dict, self.mapper, _debug, sample)
            #===================================================================
            # Continue with next events            
            #===================================================================
            events = self.mapper.next_events()

            if self.constants.BENCHMARK_OUTPUT:
                benchEndTime = _clock() * 1000
                benchMemUsage = self.memory_usage_psutil()
                scheduleTime = schedEndTime - schedStartTime
                dispatchTime = benchEndTime - benchStartTime - scheduleTime
                
                asyncio.create_subprocess_exec(
                    self.write_to_benchmark(_actual_time, queuelen, benchEndTime - benchStartTime, scheduleTime, dispatchTime, benchMemUsage)
                )

        self.end_time = _clock()
        assert(self.loaded_jobs == len(self.mapper.finished)), 'Loaded {} and Finished {}'.format(self.loaded_jobs, len(self.mapper.finished))
        self.statics_write_out(self.constants.SHOW_STATISTICS, self.constants.STATISTICS_OUTPUT)
        print('Simulation process completed.')
        self.mapper.current_time = None

    def statics_write_out(self, show, save):
        """
        Write the statistic output file
        @param show: True for showing the statistics, False otherwise.
        @param save: True for saving the statistics, False otherwise.
        """
        if not(show or save):
            return
        wtimes = self.mapper.wtimes
        slds = self.mapper.slowdowns
        sim_time_ = 'Simulation time: {0:.2f} secs\n'.format(self.end_time - self.start_time)
        disp_method_ = 'Dispathing method: {}\n'.format(self.dispatcher)
        total_jobs_ = 'Total jobs: {}\n'.format(self.loaded_jobs)
        makespan_ = 'Makespan: {}\n'.format(self.mapper.last_run_time - self.mapper.first_time_dispatch)
        avg_wtimes_ = 'Avg. waiting times: {}\n'.format(reduce(lambda x, y:x + y, wtimes) / float(len(wtimes)))
        avg_slowdown_ = 'Avg. slowdown: {}\n'.format(reduce(lambda x, y:x + y, slds) / float(len(slds)))
        if show:
            print('\n\t' + '\t'.join([sim_time_, disp_method_, total_jobs_, makespan_, avg_wtimes_, avg_slowdown_]))
        if save:
            _filepath = _path.join(self.constants.RESULTS_FOLDER_PATH, self.constants.STATISTICS_PREFIX + self.constants.WORKLOAD_FILENAME)
            with open(_filepath, 'a') as f:
                f.write(sim_time_)            
                f.write(disp_method_)
                f.write(total_jobs_)
                f.write(makespan_)
                f.write(avg_wtimes_)
                f.write(avg_slowdown_)

    def write_to_benchmark(self, time, queueSize, stepTime, schedTime, simTime, memUsage):
        """
            Writes to an output file the resource usage string related to the current simulation step.

            The output string contains 6 fields, corresponding to the input arguments, separated by ":", and can
            be easily parsed by any Python program.

        :param time: the timestamp relative to the simulation step
        :param queueSize: the size of the queue at the simulation step (before scheduling)
        :param stepTime: the total time required to perform the simulation step
        :param schedTime: the time related to the scheduling procedure
        :param simTime: the remaining time used in the step, related to the simulation process
        :param memUsage: memory usage (expressed in MB) at the simulation step
        """
        bvalues = [time, queueSize, stepTime, schedTime, simTime, memUsage]
        sep_token = ';' 
        bline = sep_token.join([str(v) for v in bvalues]) + '\n'
        
        _filepath = _path.join(self.constants.RESULTS_FOLDER_PATH, self.constants.BENCHMARK_PREFIX + self.constants.WORKLOAD_FILENAME)
        with open(_filepath, 'a') as f:
            f.write(bline)

    def load_events(self, jobs_dict, mapper, _debug=False, time_samples=2):
        """
            Incremental loading. Load the new jobs into the 
            @param jobs_dict: Dictionary of the current load, queued and running jobs
            @param mapper: Job event mapper object
            @param _debug: Debug flag
            @param time_samples: Default 2. It load the next two time steps. 
        """
        _time = None
        while not self.reader.EOF and time_samples > 0:
            _dicts = self.reader.next_dicts()
            if not _dicts:
                break
            tmp_dict = {}
            job_list = []
            for _dict in _dicts:
                if self.tweak_function:
                    self.tweak_function(_dict, self.init_unix_time)
                je = self.job_factory.factory(**_dict)
                if self.checkJobValidity(je):
                    self.loaded_jobs += 1
                    tmp_dict[je.id] = je
                    job_list.append(je)
                elif _debug:
                    print("Job %s violates the system's resource constraints and will be discarded" % je.id)
                if _time != je.queued_time:
                    _time = je.queued_time
                    time_samples -= 1
            mapper.load_events(job_list)
            jobs_dict.update(tmp_dict)

    def checkJobValidity(self, job):
        """
            Simple method that checks if the loaded job violates the system's resource constraints.

        :param job: Job object 
        :return: True if the job is valid, false otherwise
        """
        resGroups = self.resource_manager.groups_available_resource()
        validGroups = 0
        for group in resGroups.values():
            valid = True
            for k, res in job.requested_resources.items():
                if group[k] < res:
                    valid = False
                    break
            if valid:
                validGroups += 1
        return validGroups > 0

    def memory_usage_psutil(self):
        """
            Returns the memory usage in MB
        """
        process = _Process(_getpid())
        memr = process.memory_info().rss / float(2 ** 20)
        return memr
    
    def daemon_init(self):         
        """
            Initialization of the simulation daemons. I.e. visualization or watcher
        """
        _iter_func = lambda act, next: act.get(next) if isinstance(act, dict) else (getattr(act, next)() if callable(getattr(act, next)) else getattr(act, next))
        for _name, d in self.daemons.items():
            _class = d['class']
            if not _class:
                continue
            _args = []
            for _arg in d['args']:
                if isinstance(_arg, tuple):
                    res = reduce(_iter_func, _arg[1].split('.'), self if not _arg[0] else _arg[0])
                    _args.append(res)
                else:
                    _args.append(_arg)
            self.daemons[_name]['object'] = _class(*_args)
            self.daemons[_name]['object'].start()
            
    def execute_additional_data(self):
        for ad in self.additional_data:
            ad.execute()            