import Lab2.bmi as bmi


def test_bmi_normal_weight():
        weight = 57  
        height = 1.73  
        result = bmi.calculate_bmi(height, weight)
        assert result == 0

def test_bmi_over_weight():
        weight = 120
        height = 1.73
        result = bmi.calculate_bmi(height, weight)
        assert result == 1

def test_bmi_under_weight():
        weight = 50  
        height = 1.75  
        result = bmi.calculate_bmi(height, weight)
        assert result == -1


