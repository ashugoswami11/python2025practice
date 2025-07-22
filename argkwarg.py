def randomfunc(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is {value}")


list = {"ashu":"data-engineer", "python":"programming", "azure":"cloud"}

randomfunc(**list)