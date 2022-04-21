"""This tests the logging setup and function"""
import os

root = os.path.dirname(os.path.abspath(__file__))
# set the name of the apps log folder to logs
logdir = os.path.join(root, '../app/logs')
# make a directory if it doesn't exist


def test_before_request_logging():
    """This will test the myApp before request logger"""
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/myapp.log')
    # make a file for the new DEBUG request if it doesn't exist
    assert os.path.exists(logfile) is True


def test_austin_debug_func():
    """This is a test for the Austin DEBUG log function"""
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/DEBUG.log')
    # make a file for the new DEBUG request if it doesn't exist
    assert os.path.exists(logfile) is True


def test_kw_request_func():
    """This is a test for the request log function"""
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/request.log')
    # make a file for the new DEBUG request if it doesn't exist
    assert os.path.exists(logfile) is True


def test_after_request_logging():
    """This will test the myApp after request logger"""
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/myapp.log')
    # make a file for the new DEBUG request if it doesn't exist
    assert os.path.exists(logfile) is True
