######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest

test_file = "lab7_problem1"
test_inputs = ['lab7_data_problem1']

def test(monkeypatch, capsys):
    global test_file
    global test_inputs
    try:
        exists = os.path.exists(test_file + '.py')
        assert exists == True
        source = __import__(test_file)
    except:
        sys.exit()
    if len(test_inputs) > 0:
        inputs = iter(test_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()

    # Test: Ensure 7 lines of output
    assert len(output) == 7, "Incorrect overall output"

    # Test: Ensure 5 files found
    assert int(output[1]) == 5, "Incorrect number of files found"

    unique_items = [
        'Found Batman! It was in secret_document.txt',
        'Did not find Batman in eggs.txt',
        'Did not find Batman in boring_document.txt',
        'Did not find Batman in spam.txt',
        'Did not find Batman in hello.txt',
    ]

    # Test: Ensure all IPs and user accounts accounted for
    for unique_item in unique_items:
        has_item = False
        for output_line in output[2:7]:
            if output_line.lower() == unique_item.lower(): has_item = True
        assert has_item == True, "Missing required or correct output"

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################