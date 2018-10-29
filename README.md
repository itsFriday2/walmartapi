# walmartapi

OfficialAPI.py
by Friday

script for testing the official Walmart API (walmart labs)

Requires:

python 3.x (I use 3.7.1)
requests (py -m pip install requests)

Before using you need to edit it:

1)  Change the path at the top of the script to the path where it lives on your computer
2)  If you want edit the skulist (by default it comes with 197 SKU's for testing)
3)  You need to create a subfolder called 'searches' - case sensitive
4)  If you want it to pause between requests uncomment time.sleep(1) for a 1 second pause between requests

To use:

Either double click on it or run from a cmd prompt.  I prefer a cmd prompt to see the output.  The output will be saved as a .csv file in the 'searches' subfolder.

