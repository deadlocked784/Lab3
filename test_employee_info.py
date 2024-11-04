from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():
    result = get_employees_by_age_range(25, 35)
    assert len(result) == 2
    assert all(25 < employee['age'] < 35 for employee in result)

def test_calculate_average_salary():
    average_salary = calculate_average_salary()
    expected_average = sum(employee['salary'] for employee in employee_data) / len(employee_data)
    assert average_salary == expected_average

def test_get_employees_by_dept():
    result = get_employees_by_dept("Sales")
    assert len(result) == 2
    assert all(employee['department'] == "Sales" for employee in result)