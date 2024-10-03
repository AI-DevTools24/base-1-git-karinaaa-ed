import json

with open("report.json", "r") as file:
    report = json.load(file)

def test_1():
    assert report["grade"] >= 1
    
def test_2():
    assert report["grade"] >= 2
    
def test_3():
    assert report["grade"] >= 3
    
def test_4():
    assert report["grade"] >= 4
    
def test_5():
    assert report["grade"] >= 5
    
def test_6():
    assert report["grade"] >= 6
    
def test_7():
    assert report["grade"] >= 7
    
def test_8():
    assert report["grade"] >= 8
    
def test_9():
    assert report["grade"] >= 9
    
def test_10():
    assert report["grade"] >= 10