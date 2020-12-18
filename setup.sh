#!/bin/bash   
DATA="data"
PGADMIN="data/pgadmin-data"
PLANKA="data/planka"
POSTGRES="data/postgres"

echo " "
echo "Prepairing Planka data structure..." 

for DIR in $DATA $PGADMIN $PLANKA $POSTGRES
do
    if [ -d "$DIR" ]; then
        # Take action if $DIR exists. #
        echo "WARNING: $DIR directory exisits!"
        echo "    Ensure direcotries are not needed and delete before running agian."
        echo " "
        exit 1 
    else
        echo "    Making $DIR..."
        mkdir $DIR
    fi
done

echo "Directories created and ready for use."
echo " "