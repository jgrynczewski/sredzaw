# typy zemienne jako domyślne warości parametów funkcu.
def add_emplloyee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp)

emps = ["Ania", "Ola"]
add_emplloyee("Maciek", emps)
add_emplloyee("Staszek")
add_emplloyee("Magda")
add_emplloyee("Igor")