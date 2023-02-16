#!/bin/bash

if [[ -f ../requirements.txt ]]; then
    echo "Installing required packages from requirements.txt..."
    pip install -r ../requirements.txt
    echo "Required packages installed."
else
    echo "Could not find requirements.txt file."
fi

echo "Performing migrations..."
python manage.py migrate --run-syncdb
echo "Migrations performed."