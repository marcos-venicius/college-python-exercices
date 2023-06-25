counter=$(ps -eaf --forest | grep python3 malware.py | wc -l)

echo "python processes $counter"
