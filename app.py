from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()

# API endpoint and key for Spoonacular API
api_endpoint = "https://api.spoonacular.com/recipes/complexSearch"
api_key = "b389c10cfc2240d2a657d3e363e96779"

class DietInput(BaseModel):
    daily_calories: float
    protein: float
    fat: float
    carbs: float
    sodium: float

class BMRInput(BaseModel):
    age: int
    gender: str
    height: float
    weight: float
    activity_factor: float


@app.get("/")
async def root():
    activity_level_guide = "If you are sendentary, activity level: 1.2; If you lightly active, activity level: 1.375; If you are moderately active, activity level: 1.55; If you are very active, activity level 1.75"
    return {"message": "Work Out Manual", "activity_level_guide": activity_level_guide}


@app.get("/calculate_bmr/{gender}/{weight}/{height}/{age}/{activity_factor}")
async def calculate_bmr(gender: str, weight: float, height: float, age: int, activity_factor: float):
    # return {"gender": gender, "weight": weight, "height": height, "age": age, "activity_factor": activity_factor}
    # return_dict = calculate_bmr(gender, weight, height, age, activity_factor)
    # return {"profile": return_dict}
    bmr_input_dict = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activity_factor": activity_factor
    }

    # Create a new BMRInput object using the dictionary
    bmr_input = BMRInput(**bmr_input_dict)
    # return {"bmr_input": bmr_input}
    if bmr_input.gender == 'male':
        bmr = 88.36 + (13.4 * bmr_input.weight) + (4.8 * bmr_input.height) - (5.7 * bmr_input.age)
    else:
        bmr = 447.6 + (9.2 * bmr_input.weight) + (3.1 * bmr_input.height) - (4.3 * bmr_input.age)
    # return {"bmr": round(bmr, 1)}
    daily_calories = bmr * bmr_input.activity_factor
    protein = round(0.8 * bmr_input.weight, 1)
    fat = round((0.2 * daily_calories) / 9, 1)
    carbs = round((daily_calories - (protein * 4) - (fat * 9)) / 4, 1)
    sodium = round(1500 + (bmr_input.weight / 2.2) * 1.3, 1)
    return {"bmr": round(bmr, 1), "daily_calories": round(daily_calories, 1), 
            "protein": protein, "fat": fat, "carbs": carbs, "sodium": sodium}


@app.get("/suggest_diet/{gender}/{weight}/{height}/{age}/{activity_factor}")
async def suggest_diet(gender: str, weight: float, height: float, age: int, activity_factor: float):
    bmr_input_dict = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activity_factor": activity_factor
    }

    # Create a new BMRInput object using the dictionary
    bmr_input = BMRInput(**bmr_input_dict)
    # return {"bmr_input": bmr_input}
    if bmr_input.gender == 'male':
        bmr = 88.36 + (13.4 * bmr_input.weight) + (4.8 * bmr_input.height) - (5.7 * bmr_input.age)
    else:
        bmr = 447.6 + (9.2 * bmr_input.weight) + (3.1 * bmr_input.height) - (4.3 * bmr_input.age)
    # return {"bmr": round(bmr, 1)}
    daily_calories = bmr * bmr_input.activity_factor
    protein = round(0.8 * bmr_input.weight, 1)
    fat = round((0.2 * daily_calories) / 9, 1)
    carbs = round((daily_calories - (protein * 4) - (fat * 9)) / 4, 1)
    sodium = round(1500 + (bmr_input.weight / 2.2) * 1.3, 1)
    diet_input_dict = {
        "daily_calories": daily_calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs,
        "sodium": sodium
    }
    diet_input = DietInput(**diet_input_dict)
    breakfast_protein = round(0.25 * diet_input.protein, 1)
    breakfast_fat = round(0.25 * diet_input.fat, 1)
    breakfast_carbs = round(0.25 * diet_input.carbs, 1)
    breakfast_sodium = round(0.25 * diet_input.sodium, 1)
    
    lunch_protein = round(0.35 * diet_input.protein, 1)
    lunch_fat = round(0.35 * diet_input.fat, 1)
    lunch_carbs = round(0.35 * diet_input.carbs, 1)
    lunch_sodium = round(0.35 * diet_input.sodium, 1)
    
    dinner_protein = round(0.35 * diet_input.protein, 1)
    dinner_fat = round(0.35 * diet_input.fat, 1)
    dinner_carbs = round(0.35 * diet_input.carbs, 1)
    dinner_sodium = round(0.35 * diet_input.sodium, 1)
    
    snack_protein = round(0.05 * diet_input.protein, 1)
    snack_fat = round(0.05 * diet_input.fat, 1)
    snack_carbs = round(0.05 * diet_input.carbs, 1)
    snack_sodium = round(0.05 * diet_input.sodium, 1)
    
    breakfast_calories = round(diet_input.daily_calories * 0.25)
    lunch_calories = round(diet_input.daily_calories * 0.35)
    dinner_calories = round(diet_input.daily_calories * 0.35)
    snack_calories = round(diet_input.daily_calories * 0.05)
    
    return {"breakfast": {"calories": breakfast_calories, "protein": breakfast_protein, 
                          "fat": breakfast_fat, "carbs": breakfast_carbs, "sodium": breakfast_sodium},
            "lunch": {"calories": lunch_calories, "protein": lunch_protein, 
                      "fat": lunch_fat, "carbs": lunch_carbs, "sodium": lunch_sodium},
            "dinner": {"calories": dinner_calories, "protein": dinner_protein, 
                       "fat": dinner_fat, "carbs": dinner_carbs, "sodium": dinner_sodium},
            "snack": {"calories": snack_calories, "protein": snack_protein, 
                      "fat": snack_fat, "carbs": snack_carbs, "sodium": snack_sodium}}


# @app.get("/suggest_recipes/{gender}/{weight}/{height}/{age}/{activity_factor}")
# async def suggest_recipes(gender: str, weight: float, height: float, age: int, activity_factor: float):
#     bmr_input_dict = {
#         "age": age,
#         "gender": gender,
#         "height": height,
#         "weight": weight,
#         "activity_factor": activity_factor
#     }

#     # Create a new BMRInput object using the dictionary
#     bmr_input = BMRInput(**bmr_input_dict)
#     # return {"bmr_input": bmr_input}
#     if bmr_input.gender == 'male':
#         bmr = 88.36 + (13.4 * bmr_input.weight) + (4.8 * bmr_input.height) - (5.7 * bmr_input.age)
#     else:
#         bmr = 447.6 + (9.2 * bmr_input.weight) + (3.1 * bmr_input.height) - (4.3 * bmr_input.age)
#     # return {"bmr": round(bmr, 1)}
#     daily_calories = bmr * bmr_input.activity_factor
#     protein = round(0.8 * bmr_input.weight, 1)
#     fat = round((0.2 * daily_calories) / 9, 1)
#     carbs = round((daily_calories - (protein * 4) - (fat * 9)) / 4, 1)
#     sodium = round(1500 + (bmr_input.weight / 2.2) * 1.3, 1)
#     diet_input_dict = {
#         "daily_calories": daily_calories,
#         "protein": protein,
#         "fat": fat,
#         "carbs": carbs,
#         "sodium": sodium
#     }
#     diet_input = DietInput(**diet_input_dict)
#     breakfast_calories = round(diet_input.daily_calories * 0.25)
#     lunch_calories = round(diet_input.daily_calories * 0.35)
#     dinner_calories = round(diet_input.daily_calories * 0.35)
#     snack_calories = round(diet_input.daily_calories * 0.05)
    
#     # Suggest breakfast recipes
#     breakfast_params = {
#         "apiKey": api_key,
#         "addRecipeInformation": True,
#         "number": 1,
#         "maxCalories": breakfast_calories,
#         "minProtein": diet_input.protein * 0.2,
#         "minFat": diet_input.fat * 0.2,
#         "minCarbs": diet_input.carbs * 0.2,
#         "minSodium": diet_input.sodium * 0.2,
#         "type": "breakfast"
#     }
#     print(breakfast_params)
#     breakfast_response = requests.get(api_endpoint, params=breakfast_params)
#     print("Breakfast:")
#     print(breakfast_response.json())
#     breakfast_recipe = breakfast_response.json()["results"][0]
    
#     # Suggest lunch recipes
#     lunch_params = {
#         "apiKey": api_key,
#         "addRecipeInformation": True,
#         "number": 1,
#         "maxCalories": lunch_calories,
#         "minProtein": diet_input.protein * 0.3,
#         "minFat": diet_input.fat * 0.3,
#         "minCarbs": diet_input.carbs * 0.3,
#         "minSodium": diet_input.sodium * 0.3,
#         "type": "main course"
#     }
#     lunch_response = requests.get(api_endpoint, params=lunch_params)
#     lunch_recipe = lunch_response.json()["results"][0]
    
#     # Suggest dinner recipes
#     dinner_params = {
#         "apiKey": api_key,
#         "addRecipeInformation": True,
#         "number": 1,
#         "maxCalories": dinner_calories,
#         "minProtein": diet_input.protein * 0.3,
#         "minFat": diet_input.fat * 0.3,
#         "minCarbs": diet_input.carbs * 0.3,
#         "minSodium": diet_input.sodium * 0.3,
#         "type": "main course"
#     }
#     dinner_response = requests.get(api_endpoint, params=dinner_params)
#     dinner_recipe = dinner_response.json()["results"][0]
    
#     # Suggest snack recipes
#     snack_params = {
#         "apiKey": api_key,
#         "addRecipeInformation": True,
#         "number": 1,
#         "maxCalories": snack_calories,
#         "minProtein": diet_input.protein * 0.1,
#         "minFat": diet_input.fat * 0.1,
#         "minCarbs": diet_input.carbs * 0.1,
#         "minSodium": diet_input.sodium * 0.1,
#         "type": "snack"
#     }
#     snack_response = requests.get(api_endpoint, params=snack_params)
#     snack_recipe = snack_response.json()["results"][0]
    
#     return {"breakfast": breakfast_recipe, "lunch": lunch_recipe, "dinner": dinner_recipe, "snack": snack_recipe}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')