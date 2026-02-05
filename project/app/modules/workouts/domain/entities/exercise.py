from pydantic import BaseModel

class Push_ups(BaseModel):
    title:str = "Отжимания"
    number_of_repeats:int
    time_minutes:int

class Pull_ups(BaseModel):
    title:str = "Подтягивания"
    number_of_repeats:int
    time_minutes:int

class Squats(BaseModel):
    title:str = "Приседания"
    number_of_repeats:int
    time_minutes:int

class Bench_press(BaseModel):
    title:str = "Жим лежа"
    weight:int
    number_of_repeats:int
    time_minutes:int

class Squats_with_weight(BaseModel):
    title:str = "Приседания с весом"
    weight:int
    number_of_repeats:int
    time_minutes:int

class Dips_on_the_bars(BaseModel):
    title:str = "Отжимания на брусьях"
    number_of_repeats:int
    time_minutes:int
