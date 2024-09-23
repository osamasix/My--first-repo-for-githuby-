{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "449b5270-21b8-426a-9cbb-723ef8fcd093",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter temp in Celsius:  80\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "80.0C is equal to 176.0F\n"
     ]
    }
   ],
   "source": [
    "cel_temp = float(input(\"enter temp in Celsius: \"))\n",
    "def celsius_to_fahrenheit(celsius):\n",
    "    return (celsius * 9/5) + 32 \n",
    "\n",
    "Fahren_temp = celsius_to_fahrenheit(cel_temp)\n",
    "print(f\"{cel_temp}C is equal to {Fahren_temp}F\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f4670599-cd0e-4ae8-a25d-468be32e54d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number 1:  6\n",
      "Enter number 2:  5\n",
      "Enter number 3:  6\n",
      "Enter number 4:  7\n",
      "Enter number 5:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Sum of the numbers: 31.0\n",
      "Mean of the numbers: 6.2\n"
     ]
    }
   ],
   "source": [
    "# Function to calculate sum and mean of five numbers\n",
    "def calculate_sum_mean():\n",
    "    numbers = []\n",
    "    for i in range(5):\n",
    "        number = float(input(f\"Enter number {i+1}: \"))\n",
    "        numbers.append(number)\n",
    "    \n",
    "    # Calculate the sum\n",
    "    total_sum = sum(numbers)\n",
    "    \n",
    "    # Calculate the mean\n",
    "    mean = total_sum / len(numbers)\n",
    "    \n",
    "    # Print the results\n",
    "    print(f\"\\nSum of the numbers: {total_sum}\")\n",
    "    print(f\"Mean of the numbers: {mean}\")\n",
    "\n",
    "calculate_sum_mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "943c7062-06e4-416e-8ba5-0a30ec4b7529",
   "metadata": {},
   "source": [
    "# function to calculate sum\n",
    "def sum_cube():\n",
    "    #Take 2 numbers as inputs\n",
    "    num1 = float(input(\"enter first number: \"))\n",
    "    num2 = float(inout(\"Enter second number: \"))\n",
    "    #calculate cubes\n",
    "    cube_sum = num1*3 + num2*3\n",
    "#print\n",
    "print(f\"\\nThe sum of {num1} and {num2} is: {cube_sum}\")\n",
    "#call\n",
    "sum_cube() \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "3eb58702-7ed5-4efa-83c9-cfdb7730d683",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the circle radius:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of the circle with 5.0 is: 78.54\n"
     ]
    }
   ],
   "source": [
    "import math \n",
    "def circle_area():\n",
    "    radius = float(input(\"Enter the circle radius: \"))\n",
    "    area = math.pi * (radius ** 2)\n",
    "    print(f\"The area of the circle with {radius} is: {area:.2f}\")\n",
    "circle_area()\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "fc1ce81f-07e8-4253-a85e-9401127c922c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number of days:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 days:\n",
      "168 hours\n",
      "10080 minutes\n",
      "604800 seconds\n"
     ]
    }
   ],
   "source": [
    "def con_day():\n",
    "    days = int(input(\"Enter the number of days: \"))\n",
    "    h = days * 24\n",
    "    m = days * 24 *60\n",
    "    s = days * 60*24*60\n",
    "    print(f\"{days} days:\")\n",
    "    print(f\"{h} hours\")\n",
    "    print(f\"{m} minutes\")\n",
    "    print(f\"{s} seconds\")\n",
    "con_day()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d0d85d20-474d-4fef-8c5b-3a03f8472767",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter your hourly wage:  17\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hourly wage: \n",
      "hourly\n",
      "Hours worked: \n",
      "hours_worked\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many hours did you work this week?  17\n"
     ]
    }
   ],
   "source": [
    "hourly_wage = int(input(\"Please enter your hourly wage: \"))\n",
    "\n",
    "print(\"Hourly wage: \")\n",
    "print(\"hourly\")\n",
    "print(\"Hours worked: \")\n",
    "print(\"hours_worked\")\n",
    "\n",
    "hours_worked = int(input(\"How many hours did you work this week? \"))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9c29b6eb-bf44-4a67-9f60-534d249306f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your weight in kilograms (kg):  9\n",
      "Enter your height in meters (m):  90\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Your Body Mass Index (BMI) is: 0.0011111111111111111\n"
     ]
    }
   ],
   "source": [
    "def bmi():\n",
    " \n",
    "    weight = float(input(\"Enter your weight in kilograms (kg): \"))\n",
    "    height = float(input(\"Enter your height in meters (m): \"))\n",
    "    \n",
    "    bmi = weight / (height ** 2)\n",
    "    \n",
    "\n",
    "    print(f\"\\nYour Body Mass Index (BMI) is: {bmi}\")\n",
    "\n",
    "\n",
    "bmi()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a1df44aa-5898-4b73-b0b7-291c98fc4622",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name dude kameron\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Welcome to python programming kameron \n"
     ]
    }
   ],
   "source": [
    "k = input(\"Enter your name dude\")\n",
    "print(f\"\\nWelcome to python programming {k} \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54cb68cf-3232-44a3-b840-88c966dc6975",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
