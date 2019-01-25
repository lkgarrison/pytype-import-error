import adjacent_module
from subpackage import foo
from subpackage.helpers import helper_fn

if __name__ == "__main__":
    print("Demonstrates pytype import error")
    helper_fn()
    foo.bar()
    adjacent_module.do_something()
