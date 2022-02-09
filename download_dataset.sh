# This scripts downloads and unzips the CrowdHuman Dataset!

# check if data directory exists
if [ -d "data/" ] 
then
    cd data/
else
    mkdir data
    cd data/
fi

wget -L https://oregonstate.box.com/shared/static/u4gnvq0cyksjz242ywuo66k9cechmyan -O CrowdHumanDataset.zip

echo ""
echo "Download Complete!"

echo ""
echo "Trying to unzip the dataset..."

# try to unzip the dataset
if ! command -v unzip &> /dev/null
then
    echo "unzip could not be found. please unzip the dataset on your own."
    cd ..
    exit
else
    unzip CrowdHumanDataset.zip
    echo "Successfully unziped dataset!"
fi
