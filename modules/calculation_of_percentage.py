def validation(calculation):
    if calculation < 0:
        print("Result must be positive")
        exit()
    return calculation

def calculation(count_people):
    result = int(count_people["count_selected_country"]) * 100 / int(count_people["count_all_countries"])
    return result

def show_calculation_result(result):
    print("The percentage of emigrants is equal to", result)
