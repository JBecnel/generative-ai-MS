import os
from openai import OpenAI
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

client = OpenAI(
  api_key = os.environ['OPENAI_API_KEY']
)

deployment = "gpt-3.5-turbo"

no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"


messages = [{"role": "user", "content": prompt}]  

# make completion
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature=0.9)

# print response
print("Recipes:")
print(completion.choices[0].message.content)


old_prompt_result = completion.choices[0].message.content
prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "

new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature=0)

# print response
print("\n=====Shopping list ======= \n")
print(completion.choices[0].message.content)