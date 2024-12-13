#!/bin/bash

# Time the execution of the function
for i in {1..10}; do
    start_time=$(date +%s%N)  # Capture start time in nanoseconds
    sudo nxbt macro -c mine_xp3.txt -r
    end_time=$(date +%s%N)    # Capture end time in nanoseconds

    # Calculate duration
    elapsed_time=$((end_time - start_time))
    elapsed_time_ms=$((elapsed_time / 1000000))  # Convert to milliseconds

    # Output the result
    echo "Execution time: $elapsed_time_ms milliseconds"
done