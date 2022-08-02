{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import clear_output\n",
    "\n",
    "def display_board(board):\n",
    "    clear_output()\n",
    "    print('    |   |   ')\n",
    "    print('  '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])\n",
    "    print('----|---|----')\n",
    "    print('  '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])\n",
    "    print('----|---|----')\n",
    "    print('  '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])\n",
    "    print('    |   |   ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    |   |   \n",
      "    |   |  \n",
      "----|---|----\n",
      "    |   |  \n",
      "----|---|----\n",
      "    |   |  \n",
      "    |   |   \n"
     ]
    }
   ],
   "source": [
    "test_board = [' ']*10\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_input():\n",
    "    marker = ''\n",
    "    while not (marker == 'X' or marker == 'O'):\n",
    "        marker = input(' Player 1, Choose X or O: ').upper()\n",
    "    if marker == 'X':\n",
    "        return ('X','O')\n",
    "    else:\n",
    "        return ('O','X')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Player 1, Choose X or O: x\n"
     ]
    }
   ],
   "source": [
    "player1_marker,player2_marker = player_input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'X'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "player1_marker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'O'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "player2_marker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def place_marker(board,marker,position):\n",
    "    board[position] = marker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    |   |   \n",
      "  @ |   |  \n",
      "----|---|----\n",
      "    |   |  \n",
      "----|---|----\n",
      "    |   |  \n",
      "    |   |   \n"
     ]
    }
   ],
   "source": [
    "place_marker(test_board,'@',7)\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_check(board,marker):\n",
    "    return ((board[1] == board[2] == board[3] == marker) or\n",
    "        (board[4] == board[5] == board[6] == marker) or\n",
    "        (board[7] == board[8] == board[9] == marker) or\n",
    "        (board[1] == board[4] == board[7] == marker) or\n",
    "        (board[2] == board[5] == board[8] == marker) or\n",
    "        (board[3] == board[6] == board[9] == marker) or\n",
    "\n",
    "        (board[1] == board[5] == board[9] == marker) or\n",
    "        (board[3] == board[5] == board[7] == marker))\n",
    "        \n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    |   |   \n",
      "  @ |   |  \n",
      "----|---|----\n",
      "    |   |  \n",
      "----|---|----\n",
      "    |   |  \n",
      "    |   |   \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "display_board(test_board)\n",
    "win_check(test_board,'X')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def who_is_first():\n",
    "    first = random.randint(1,2)\n",
    "    \n",
    "    if first == 1:\n",
    "        return 'Player 1'\n",
    "    else:\n",
    "        return 'Player 2'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Player 2'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "who_is_first()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def space_check(board,position):\n",
    "    return board[position] == ' '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def full_board_check(board):\n",
    "         for i in range(1,10):\n",
    "            if space_check(board,i):\n",
    "                return False\n",
    "        \n",
    "         return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_choise_position(board):\n",
    "    \n",
    "    position = 0\n",
    "    \n",
    "    while position not in [1,2,3,4,5,6,7,8,9] and space_check(board,position):\n",
    "        position =int(input('Choose a position (1-9): '))\n",
    "    return position\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def replay():\n",
    "    choise = input('Play again? Y or N').upper()\n",
    "    return choise == 'Y'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Main Part"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    |   |   \n",
      "  O |   |  \n",
      "----|---|----\n",
      "  X | X |  \n",
      "----|---|----\n",
      "    | O |  \n",
      "    |   |   \n"
     ]
    }
   ],
   "source": [
    "print('WELCOME TO TIC TAC TOE')\n",
    "\n",
    "while True:\n",
    "    \n",
    "    \n",
    "    the_board = [' ']*10\n",
    "    player1_marker,player2_marker = player_input()\n",
    "    turn = who_is_first() #####\n",
    "    print('প্রথমে মারবে ' + turn)\n",
    "    print('i')\n",
    "    \n",
    "    \n",
    "    game_on = True\n",
    "    \n",
    "    while game_on:\n",
    "        \n",
    "        \n",
    "        \n",
    "        # player 1 turn\n",
    "        \n",
    "        \n",
    "        \n",
    "        \n",
    "        \n",
    "        if turn == 'Player 1':\n",
    "            \n",
    "            display_board(the_board)\n",
    "            position = player_choise_position(the_board)\n",
    "            place_marker(the_board,player1_marker,position)\n",
    "            \n",
    "            if win_check(the_board,player1_marker):\n",
    "                display_board(the_board)\n",
    "                print('PLAYER 1 HAS WON!!')\n",
    "                break\n",
    "            else:\n",
    "                if full_board_check(the_board):\n",
    "                    display_board(the_board)\n",
    "                    print('DRAW!!')\n",
    "                    break\n",
    "                    \n",
    "                else:\n",
    "                    turn = 'Player 2'\n",
    "                    \n",
    "                ## No tie no win? Then next player's turn\n",
    "                \n",
    "        \n",
    "        else:\n",
    "            ### PLAYER 2 TURN\n",
    "            \n",
    "            display_board(the_board)\n",
    "            position = player_choise_position(the_board)\n",
    "            place_marker(the_board,player2_marker,position)\n",
    "            \n",
    "            if win_check(the_board,player2_marker):\n",
    "                display_board(the_board)\n",
    "                print('PLAYER 2 HAS WON!!')\n",
    "                break\n",
    "            else:\n",
    "                if full_board_check(the_board):\n",
    "                    display_board(the_board)\n",
    "                    print('DRAW!!')\n",
    "                    break\n",
    "                    \n",
    "                else:\n",
    "                    turn = 'Player 1'\n",
    "                    \n",
    "                    \n",
    "            \n",
    "                \n",
    "    if not replay():\n",
    "        break\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
