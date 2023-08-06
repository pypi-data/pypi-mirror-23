from unittest import TestCase

_missing = object()

class TestBatcher(TestCase):

    def one(self, source, end_batch_callback=_missing, **kw): 								# **kw allows passing only some keyworks (the others will be set to default by batcher), easier for user
        log = []
        if end_batch_callback is _missing:
            def end_batch_callback():
                log.append('X')
        from .. import batcher
        batcher = batcher.run_in_batches(
                source,
                end_batch_callback=end_batch_callback,
                **kw)
        for letter in batcher:              
            log.append(letter)
        return ''.join(log)

    def test_no_end_batch_callback(self):
        result = self.one('abcdefg', end_batch_callback=None)
        self.assertEqual(result, 'abcdefg')

    def test_Make_batches(self):
        result = self.one('abcdefg')			
        self.assertEqual(result, 'abXcdXefXgX')		

    def test_Make_big_batches(self):								# one incomplete batch of maximum 1000 elements
        result = self.one('abcdefg', batch_size=1000)			
        self.assertEqual(result, 'abcdefgX')

    def test_Max_batches(self):
        result = self.one('abcdefg', max_batches=2)
        self.assertEqual(result, 'abXcdX')

    def test_Batch_size(self):
        result = self.one('abcdefg', batch_size=3, max_batches=2)
        self.assertEqual(result, 'abcXdefX')

    def test_Start_batch(self):
        result = self.one('abcdefg', batch_start=2, max_batches=3)  				# batch_start=1 means skipping the first batch (the 0-batch)
        self.assertEqual(result, 'efXgX')		

    def test_End_iterator(self):
        result = self.one('abc', batch_size=2, max_batches=2)
        self.assertEqual(result, 'abXcX')


class TestParser(TestCase):

    def create_test_parser(self):								# simulates the parser within the main script
        import argparse
        parser = argparse.ArgumentParser(description='simulates passing arguments to script')
        parser.add_argument('--db', dest='to_db', help="destination database")			# the main script adds all general arguments (9 more)	
        parser.add_argument('--from-db', dest='from_db', help="source database")		
        return parser
	
    def test_help(self):
        # printing help used to error
        from .. import batcher
        try:
            from StringIO import StringIO
        except ImportError:
            from io import StringIO
        parser = self.create_test_parser()
        batcher.add_arguments(parser)					
        parser.print_help(file=StringIO())

    def test_Add_arguments(self):
        from .. import batcher
        parser = self.create_test_parser()
        batcher.add_arguments(parser)					
        args = ['./bin/import.py', '--db', 'test_batcher', '--from-db', 'postgresql:///cityscene', '--batch-size', '10', '--max-batches', '2']
        options = parser.parse_args(args[1:])							# parsing done in the main function and for all arguments except program name
        self.assertEqual(options.batch_size, 10)

    def test_Get_batcher_args_alline(self):
        from .. import batcher
        args = ['./bin/import.py', '--db', 'test_batcher', '--from-db', 'postgresql:///cityscene', '--batch-size', '10', '--max-batches', '2']
        parser = self.create_test_parser()		
        batcher.add_arguments(parser)
        options = parser.parse_args(args[1:])													 
        result = batcher.get_batcher_args(options)						
        self.assertEqual(result, {'max_batches':2, 'batch_start': 0, 'batch_size':10})


    def test_Get_batcher_args_none(self):
        from .. import batcher
        args = []
        parser = self.create_test_parser()									
        batcher.add_arguments(parser)
        options = parser.parse_args(args[1:])													 
        result = batcher.get_batcher_args(options)						# if input is not specified, default values				
        self.assertEqual(result, {'batch_start': 0, 'batch_size':1000}) 				


    def test_Get_batcher_args_more(self):
        from .. import batcher
        args = ['./bin/import.py', '--db', 'test_batcher', '--from-db', 'postgresql:///cityscene', '--batch-size', '10', '--percentage', '50']
        parser = self.create_test_parser()									
        batcher.add_arguments(parser)
        options = parser.parse_args(args[1:])													 
        result = batcher.get_batcher_args(options)						
        self.assertEqual(result, { 'batch_start': 0, 'batch_size': 10, 'percentage': 50}) 	


class TestRandom(TestCase):
 
    def create_test_parser(self):								
        import argparse
        parser = argparse.ArgumentParser(description='simulates passing arguments to script')
        parser.add_argument('--db', dest='to_db', help="destination database")			
        parser.add_argument('--from-db', dest='from_db', help="source database")			
        return parser


    def test_random_sampler_percentage(self):
        from .. import batcher
        args = ['./bin/import_script.py', '--db', 'test_batcher', '--from-db', 'database', '--batch-size', '10', '--percentage', '50']	
        parser = self.create_test_parser()							
        batcher.add_arguments(parser)	
        options = parser.parse_args(args[1:])													 			
        kw =  batcher.get_batcher_args(options)		
        log=[]
        def end_batch():  
            log.append('X')
        result = batcher.run_in_batches('abcdefghil', end_batch, **kw) 	
        for element in result:              
            log.append(element)
        log_list = ''.join(log)
        self.assertEqual(len(log_list), 6) 							# check that it's yielding the right number of elements (5) + the 'X'


    def test_random_sampler_percentage_2(self):
        from .. import batcher
        args = ['./bin/import_script.py', '--db', 'test_batcher', '--from-db', 'database', '--batch-size', '10', '--percentage', '50', '--seed', '1']	
        parser = self.create_test_parser()							
        batcher.add_arguments(parser)	
        options = parser.parse_args(args[1:])													 			
        kw =  batcher.get_batcher_args(options)		
        log=[]
        def end_batch():  
            log.append('X')
        result = batcher.run_in_batches('abcdefghilmnopqrstuvwxyz', end_batch, **kw) 						
        for element in result:              
            log.append(element)
        log_list = ''.join(log)
        self.assertEqual(len(log_list), 14)							# some batches of 5 + the 'X' + incomplete batch (which may have 2 or 3 elements depending)


    def test_random_sampler_elements(self):
        from .. import batcher
        args = ['./bin/import_script.py', '--db', 'test_batcher', '--from-db', 'database', '--batch-size', '10',  '--percentage', '50', '--seed', '1']
        parser = self.create_test_parser()							
        batcher.add_arguments(parser)		
        options = parser.parse_args(args[1:])													 			
        kw =  batcher.get_batcher_args(options)	
        log=[]
        def end_batch():  
            log.append('X')
        result = batcher.run_in_batches('abcdefghil', end_batch, **kw)			 	
        for element in result:              
            log.append(element)
        log_list = ''.join(log)
        self.assertEqual(log_list, 'cefilX')							# check the elements (knowing the seed, gives always the same result)


    def test_random_sampler_incomplete_2(self):
        from .. import batcher 
        args = ['./bin/import_script.py', '--db', 'test_batcher', '--from-db', 'database', '--batch-size', '10',  '--percentage', '50', '--seed', '1']
        parser = self.create_test_parser()							
        batcher.add_arguments(parser)		
        options = parser.parse_args(args[1:])													 			
        kw =  batcher.get_batcher_args(options)	
        log=[]
        def end_batch():  
            log.append('X')
        result = batcher.run_in_batches('abcdefghilmnopqrstuvwxyz', end_batch, **kw)			 	
        for element in result:              
            log.append(element)
        log_list = ''.join(log)
        self.assertEqual(log_list, 'cefilXoqruvXyX')						# it creates batches of 5 elements (i.e. 50%(10)) and works for incomplete batches


    def test_random_sampler_arguments(self):
        from .. import batcher
        args = ['./bin/import_script.py', '--db', 'test_batcher', '--from-db', 'database', '--batch-size', '10', '--batch-start', '1', '--max-batches', '1', '--percentage', '50', '--seed', '1']
        parser = self.create_test_parser()							
        batcher.add_arguments(parser)		
        options = parser.parse_args(args[1:])													 			
        kw =  batcher.get_batcher_args(options)	
        log=[]
        def end_batch():  
            log.append('X')
        result = batcher.run_in_batches('abcdefghilmnopqrstuvwxyz', end_batch, **kw)			 	
        for element in result:              
            log.append(element)
        log_list = ''.join(log)
        self.assertEqual(log_list, 'oqruvX')							# test other batch parameters  


class FunctionalTest(TestCase):									# To test the whole workflow, similarly to real case

    def create_test_parser(self):								
        import argparse
        parser = argparse.ArgumentParser(description='simulates passing arguments to script')
        parser.add_argument('--db', dest='to_db', help="destination database")			
        parser.add_argument('--from-db', dest='from_db', help="source database")			
        return parser

    def test_all(self):
        from .. import batcher
        args = ['./bin/import_script.py', '--db', 'test_batcher', '--from-db', 'database', '--batch-start', '1', '--batch-size', '3']
        parser = self.create_test_parser()							
        batcher.add_arguments(parser)
        options = parser.parse_args(args[1:])													 
        kw = batcher.get_batcher_args(options)		
        log = []
        def end_batch():                
            log.append('X')
        batcher = batcher.run_in_batches('abcdefg', end_batch, **kw)
        for letter in batcher:
            log.append(letter)
        result = ''.join(log)
        self.assertEqual(result, 'defXgX')								
	
    def test_all_random(self):
        from .. import batcher
        args = ['./bin/import_script.py', '--db', 'test_batcher', '--from-db', 'database', '--batch-size', '9', '--percentage', '30', '--seed', '1']
        parser = self.create_test_parser()							
        batcher.add_arguments(parser)
        options = parser.parse_args(args[1:])													 
        kw = batcher.get_batcher_args(options)		
        log = []
        def end_batch():                
            log.append('X')
        batcher = batcher.run_in_batches('abcdefghilmnopqrstuvwxyz', end_batch, **kw)
        for letter in batcher:
            log.append(letter)
        result = ''.join(log)
        self.assertEqual(result, 'ceiXnptXwyX')
  
