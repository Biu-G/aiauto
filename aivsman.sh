#!/bin/bash
for ((i=0;i<1;i++));do
        {
				python3 run_game.py
        }&
done
python3 run_game.py ai
wait

