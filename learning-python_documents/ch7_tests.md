# Testing, Profiling, and Dealing with Exceptions

### Testing application

* `white-box test` : exercise the internals of the code, inspect it down to a very fine level of granularity
* `black-box test` : consider the software under testing as if being within a box, the internals of which are ignored



* ` mocks` : fake objects for test 
  * from version 3.3, it has been included in the standard library under the *unittest* module
* `patching` : the act of replacing a real object or function with a mock
  * The mock library provides the patch tool, which can act as a function or class decorator, and even as a context manager

* `assertion` : a function(or method) that you can use tto verify euqlity between objects, as well as other conditions

```python
tests/test_ch7/test_filter_funcs.py

from unittest import TestCase # 1
from unittest.mock import patch, call # 2
from nose.tools import assert_equal # 3
from ch7.filter_funcs import filter_ints # 4

class FilterIntsTestCase(TestCase): # 5
    @patch('ch7.filter_funcs.is_positive') # 6
    def test_filter_ints(self, is_positive_mock): # 7
        # preparation
        v = [3, -4, 0, 5, 8]
        # execution
        filter_ints(v) # 8
        # verification
        assert_equal(
            [call(3), call(-4), call(0), call(5), call(8)],
            is_positive_mock.call_args_list
        ) # 9
        
# mock을 사용하지 않는 'interface testing'
def test_filter_ints_return_value(self):
    v = [3, -4, 0, -2, 5, 0, 8, -1]
    result = filter_ints(v)
    assert_list_equal([3, 5, 8], result)
```

* Each method of this class starting with `test_`, will be interpreted as a test
*  When we decorate a function using patch, like in our example, we get an extra argument in the test signature (#7), which I like to call as the patched function name, plus a _mock suffix, just to make it clear that the object has been patched (or mocked out).)

```
$ pip install nose

$ nosetests tests/test_ch7/
```



* `Triangulation` 
  * Triangulation is a very powerful technique that teaches us to always try to exercise our code from many different angles, to cover all possible edge cases to expose any problems



* `boundary` & `granularity` (세분함)
  * when we surround the boundary, taking all three areas into account is not enough. We need to do it with the minimum possible granularity.

---

### Exceptions

* Python will watch out for one or more different types of exceptions
  * `try` clause : opens the statement
  * `except` clause : define what to do when an exception is caught
  * `else` clause : executed when the `try` clause is exited without any exception raised
  * `finally` clause : executed regardless of whatever happened in the other clauses

  ```python
  exceptions/multiple.except.py
  try:
      # some code
  except Exception1:
      # react to Exception1
  except (Exception2, Exception3):
      # react to Exception2 and Exception3
  except Exception3:
      # react to Exception3
  ```

* custom exceptions
  * Python build-in exceptions : derives from `BaseException`
  * custom exceptions : should never inherit directly from `baseexception`
    * The reason for it is that handling such an exception will trap also system-exiting exceptions such as SystemExit and KeyboardInterrupt, which derive from BaseException, and this could lead to severe issues
    * Writing an except statement without specifying any exception would catch any exception, therefore exposing your code to the same risks you incur when you derive your custom exceptions from BaseException

---

### Profiling Python

* Profiling : having the application run while keeping track of several different parameters, like the number of times a function is called, the amount of time spent inside it...
* `profile` & `cProfile` 
  * `cProfile` is recommended for most users, it's a C extension with reasonable overhead that makes it suitable for profiling long running programs
  * `profile` is a pure Python module whose interface is imitated by cProfile, but which adds significant overhead to profiled programs
  * 

* `determinist` vs `statistical` profiling
  * `determinist` : all function calls, function returns and exception events are monitored, and precise timings are made for the intervals between these events
  * `statistical` : randomly samples the effective instruction pointer, and deduces where time is being spent
    * less overhead
    * provides only approximate results

