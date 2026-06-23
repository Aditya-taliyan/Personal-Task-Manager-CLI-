from task_manager.models import Task

def test_task_creation():
    task = Task("Buy milk", "High", "2026-06-25")
    assert task.title == "Buy milk"
    assert task.priority == "High"
    assert task.done == False

def test_default_priority():
    task = Task("Walk dog")
    assert task.priority == "Medium"

def test_to_dict_structure():
    task = Task("Read book", "Low", "2026-07-01")
    result = task.to_dict()
    assert result["title"] == "Read book"
    assert result["priority"] == "Low"
    assert result["done"] == False