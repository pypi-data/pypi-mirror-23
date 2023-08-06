# coding: utf-8

from __future__ import print_function
import unittest, os, sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from ttpassgen import ttpassgen

#test/in.dict generate by: ttpassgen.py -r [123]{3:3} in.dict
class Test_ttpassgen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test_ttpassgen, cls).setUpClass()

        def lc_func():
            if not os.path.exists('testout.dict'): return 0
            with open('testout.dict', 'r') as f:
                return len(f.readlines())
        global lc
        lc = lc_func

        def go_func(rule, dictlist=os.path.join(myPath, 'in.dict'), mode=0, partSize=0, diskCache=500, repeatMode='?', seperator=None, debugMode=1):
            try:
                ttpassgen.cli.main(['-m', mode, '-d', dictlist, '-r', rule, '-g', repeatMode, '-c',
                    diskCache, '-p', partSize, '-s', seperator, '--debug_mode', debugMode, 'testout.dict'])
            except(SystemExit):
                pass
            return lc()
        global go
        go = go_func


    @classmethod
    def tearDownClass(cls):
        super(Test_ttpassgen, cls).tearDownClass()
        lc = None
        go = None
        if os.path.exists('testout.dict'): os.remove('testout.dict')
        if os.path.exists('testout.dict.1'): os.remove('testout.dict.1')
        if os.path.exists('testout.dict.2'): os.remove('testout.dict.2')
        if os.path.exists('testout.dict.3'): os.remove('testout.dict.3')
        

    def test_invalid_options(self):
        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go('$0', mode=233), 0)

        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go(dictlist=None, rule=None), 0)

        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go('[?d]', repeatMode="cc9"), 0)

        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go('$0word233', dictlist=''), 0)

        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go('$99[hello]'), 0)

        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go('$0', dictlist='not_exist.dict'), 0)


    def test_not_exist_output_file(self):
        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go('$0'), 6)
    
    def test_dict_copy_rule(self):
        self.assertEquals(go('$0'), 6)


    def test_charset_rule_no_range(self):
        self.assertEquals(go('[abc]'), 3)


    def test_charset_rule(self):
        self.assertEquals(go('[abc]?'), 4)


    def test_charset_rule_with_range(self):
        self.assertEquals(go('[abc]{2:3}'), 12)

    
    def test_charset_rule_with_global_repeat_mode(self):
        self.assertEquals(go('[abc]{2:3}', repeatMode='*'), 36)


    def test_mask_charset_rule(self):
        self.assertEquals(go('[?d]?'), 11)


    def test_mask_charset_rule_with_range(self):
        self.assertEquals(go('[a?dA]{1:2}'), 144)
        self.assertEquals(go('[?d]{2:2}'), 90)
        self.assertEquals(go('[?d]{2}'), 90)
    

    def test_dict_mark_charset_rule(self):
        self.assertEquals(go('$0[abc]?'), 24)


    def test_word_seperator(self):
        self.assertEquals(go('$0[abc]?', seperator='&#160;'), 1)
        self.assertEquals(go('$0[abc]?', seperator='-------------------------\n'), 24)
    

    def test_multi_dict_mark_charset_rule(self):
        inDict = os.path.join(myPath, 'in.dict')
        in2Dict = os.path.join(myPath, 'in2.dict')
        with open(in2Dict, 'wb') as f:
            content = ['q00', 'q01']
            f.write(('\n'.join(content)).encode('utf-8'))
        self.assertEquals(go('$1$0[abc]?', dictlist="%s,%s"%(inDict, in2Dict)), 48)
        if os.path.exists(in2Dict): os.remove(in2Dict)


    def test_part_size_with_complex_rule(self):
        if os.path.exists('testout.dict.1'): os.remove('testout.dict.1')
        if os.path.exists('testout.dict.2'): os.remove('testout.dict.2')
        if os.path.exists('testout.dict.3'): os.remove('testout.dict.3')

        go('[?d]{1:4:*}$0[?q]$[0123]', partSize=1, debugMode=1)
        totalLine = 0
        with open('testout.dict.1', 'r') as f:
            totalLine += len(f.readlines())
        with open('testout.dict.2', 'r') as f:
            totalLine += len(f.readlines())
        with open('testout.dict.3', 'r') as f:
            totalLine += len(f.readlines())

        #actual value: 1024 * 1, why 24 difference? I like do it>_>
        self.assertTrue(1000 <= os.path.getsize('testout.dict.1') / 1024 <= 1048)
        if os.path.exists('testout.dict.1'): os.remove('testout.dict.1')
        if os.path.exists('testout.dict.2'): os.remove('testout.dict.2')
        if os.path.exists('testout.dict.3'): os.remove('testout.dict.3')
        self.assertEquals(totalLine, 266640)


    def test_multiprocessing_complex_rule(self):
        self.assertEquals(go('[789]{0:3:*}$0[?q]$0', debugMode=0), 1440)
        self.assertEquals(go('[789]{0:3:*}$0[?q]{1:?}$0', debugMode=0), 1440)

    
    def test_dick_cache(self):
        self.assertEquals(go('$0[abc]?', diskCache=0), 24)

    
    def test_part_size(self):
        if os.path.exists('testout.dict.1'): os.remove('testout.dict.1')
        if os.path.exists('testout.dict.2'): os.remove('testout.dict.2')
        if os.path.exists('testout.dict.3'): os.remove('testout.dict.3')

        go('[?l]{1:4}', partSize=1)
        totalLine = 0
        with open('testout.dict.1', 'r') as f:
            totalLine += len(f.readlines())
        with open('testout.dict.2', 'r') as f:
            totalLine += len(f.readlines())
        if len(os.linesep) > 1:
            with open('testout.dict.3', 'r') as f:
                totalLine += len(f.readlines())

        #actual value: 1024 * 1, why 24 difference? I like do it>_>
        self.assertTrue(1000 <= os.path.getsize('testout.dict.1') / 1024 <= 1048)
        if os.path.exists('testout.dict.1'): os.remove('testout.dict.1')
        if os.path.exists('testout.dict.2'): os.remove('testout.dict.2')
        if os.path.exists('testout.dict.3'): os.remove('testout.dict.3')
        self.assertEquals(totalLine, 375076)

    
    def test_wrong_length_in_rule(self):
        if os.path.exists('testout.dict'): os.remove('testout.dict')
        self.assertEquals(go('[789]{0:-3}'), 0)


if __name__ == '__main__':
    unittest.main()