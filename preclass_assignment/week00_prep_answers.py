{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7559b11e-f25d-4a47-bef5-25da4c557ae5",
   "metadata": {},
   "source": [
    "***Team 17 1st Assignment***"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c90e8a34",
   "metadata": {},
   "source": [
    "**Exercise 1**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "27ab7e9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, world!\n"
     ]
    }
   ],
   "source": [
    "def greet(name):\n",
    "    print(f\"Hello, {name}!\")\n",
    "\n",
    "# Example usage\n",
    "greet('world')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "efe0b97a",
   "metadata": {},
   "source": [
    "**Exercise 2**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b5d1b4d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too small!\n",
      "Just right. :)\n",
      "Too large!\n",
      "Just right. :)\n"
     ]
    }
   ],
   "source": [
    "def goldilocks(bed_length):\n",
    "    if bed_length < 140:\n",
    "        print(\"Too small!\")\n",
    "    elif bed_length > 150:\n",
    "        print(\"Too large!\")\n",
    "    else:\n",
    "        print(\"Just right. :)\")\n",
    "\n",
    "# Example usage\n",
    "goldilocks(139)  # Too small!\n",
    "goldilocks(140)  # Just right. :)\n",
    "goldilocks(151)  # Too large!\n",
    "goldilocks(150)  # Just right. :)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f65239d8",
   "metadata": {},
   "source": [
    "**Exercise 3** "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "374b46c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9]\n"
     ]
    }
   ],
   "source": [
    "def square_list(numbers):\n",
    "    return [num ** 2 for num in numbers]\n",
    "\n",
    "# Example usage\n",
    "print(square_list([1, 2, 3]))  # Output: [1, 4, 9]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4be266e2",
   "metadata": {},
   "source": [
    "**Exercise 4**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "53aa0ca2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 1, 2, 3, 5, 8, 13, 21]\n"
     ]
    }
   ],
   "source": [
    "def fibonacci_stop(max_value):\n",
    "    fib_sequence = [1, 1]\n",
    "    while True:\n",
    "        next_fib = fib_sequence[-1] + fib_sequence[-2]\n",
    "        if next_fib >= max_value:\n",
    "            break\n",
    "        fib_sequence.append(next_fib)\n",
    "    return fib_sequence\n",
    "\n",
    "# Example usage\n",
    "print(fibonacci_stop(30))  # Output: [1, 1, 2, 3, 5, 8, 13, 21]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d14021ec",
   "metadata": {},
   "source": [
    "**Exercise 5**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "59a30dc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-999, 2, 6, 95]\n"
     ]
    }
   ],
   "source": [
    "def clean_pitch(pitch_angles, status_signals):\n",
    "    cleaned_data = [\n",
    "        -999 if (angle < 0 or angle > 90) and status > 0 else angle\n",
    "        for angle, status in zip(pitch_angles, status_signals)\n",
    "    ]\n",
    "    return cleaned_data\n",
    "\n",
    "# Example usage\n",
    "x = [-1, 2, 6, 95]  # \"raw\" pitch angle at four time steps\n",
    "status = [1, 0, 0, 0]  # status signal\n",
    "print(clean_pitch(x, status))  # Output: [-999, 2, 6, 95]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84c9769c",
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
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
