class countInstances:
    __instance_count = 0

    def __init__(self):
        countInstances.__instance_count +=1

    def get_instance_count():
        return countInstances.__instance_count


O1 = countInstances()
O2 = countInstances()
O3 = countInstances()

print(countInstances.get_instance_count())


    
