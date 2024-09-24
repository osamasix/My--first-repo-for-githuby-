{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "95a5acb6-bd7c-4484-94fa-5af10fa765c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Type your age:  8\n",
      "Are you a US Citizen? (yes/no):  yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No leave cant vote\n"
     ]
    }
   ],
   "source": [
    "def elig_vote():\n",
    "    a = int(input(\"Type your age: \"))\n",
    "    b = input(\"Are you a US Citizen? (yes/no): \")\n",
    "    if a >= 18 and b ==\"yes\":\n",
    "        print(\"Yes! you can vote\")\n",
    "    else: \n",
    "        print(\"No leave cant vote\") \n",
    "elig_vote()\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3d82c7c1-3b36-48e9-9e6e-bd57353fcce2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter password or else!:  lol\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Leave!\n"
     ]
    }
   ],
   "source": [
    "def STORE_PASS():\n",
    "    cp = \"Kamishot\"\n",
    "    up = input(\"Enter password or else!: \")\n",
    "    if up == cp:\n",
    "        print(\"Correct Diddy\")\n",
    "    else:\n",
    "        print(\"Leave!\")\n",
    "STORE_PASS()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "f27bb0d4-b1fb-4292-8d78-b00d6c728063",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a month December\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "December has 30 days\n"
     ]
    }
   ],
   "source": [
    "def lil_month():\n",
    "    month = \"December\"\n",
    "    up = input(\"Enter a month\")\n",
    "    if up == month:\n",
    "        print(f\"{month} has 30 days\")\n",
    "    else:\n",
    "        print(\"wrong month try December maybe?\")\n",
    "lil_month()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "de48c659-f178-442d-82c2-b82895830b9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The sum of number from 1 to 20 is: 210\n"
     ]
    }
   ],
   "source": [
    "def sum_num():\n",
    "    TS = sum(range(1,21))\n",
    "    print(f\"The sum of number from 1 to 20 is: {TS}\")\n",
    "sum_num() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "58ff80a4-e0ca-4d10-a0a6-881918cb3651",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The smallest number in the list is: 1\n"
     ]
    }
   ],
   "source": [
    "def find_small():\n",
    "    num = [3, 9, 1, 6, 2, 8]\n",
    "    small = min(num)\n",
    "    print(f\"The smallest number in the list is: {small}\")\n",
    "find_small()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f4ceb047-5fe7-4cf5-937d-eb8f31b7d7cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Numbers divisible by 11 but not by 2 between 100 and 500:\n",
      "121\n",
      "143\n",
      "165\n",
      "187\n",
      "209\n",
      "231\n",
      "253\n",
      "275\n",
      "297\n",
      "319\n",
      "341\n",
      "363\n",
      "385\n",
      "407\n",
      "429\n",
      "451\n",
      "473\n",
      "495\n"
     ]
    }
   ],
   "source": [
    "def find_num():\n",
    "    print(\"Numbers divisible by 11 but not by 2 between 100 and 500:\")\n",
    "\n",
    "\n",
    "    for num in range(100, 500):\n",
    "        if num % 11 == 0 and num % 2 != 0:\n",
    "            print(num)\n",
    "find_num()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "cfdec473-8768-4ccf-a9d4-afd8a9ab28f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The sum of postive numbers in the list is: 73\n"
     ]
    }
   ],
   "source": [
    "def sum_of_num():\n",
    "    number = [-2, 13, -4, -5, 10, 20, 30, -12]\n",
    "    pos_sum = sum([ num for num in number if num > 0 ])\n",
    "    print(f\"The sum of postive numbers in the list is: {pos_sum}\")\n",
    "sum_of_num()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "4a56b1f8-87d9-4115-9ebe-380d72c8a6ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "10\n",
      "15\n",
      "20\n",
      "25\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "def print_numbers():\n",
    "    for num in range(1, 31):\n",
    "        if num % 5 == 0:\n",
    "            print(num)\n",
    "print_numbers() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "b506c75b-b8ea-48d9-b58d-2d2d881939bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please dont fail me, I cannot do question 10 yes/no no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "okay thankyou\n"
     ]
    }
   ],
   "source": [
    "def Please_dont_fail_me():\n",
    "    a = input(\"Please dont fail me, I cannot do question 10 yes/no\")\n",
    "    b = \"yes\"\n",
    "    if a == b:\n",
    "            print(\"Thankyou Prof!\")\n",
    "    else:\n",
    "        print(\"okay thankyou\")\n",
    "Please_dont_fail_me()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c865bb0-f248-47b7-b601-12e3e655c6b2",
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
