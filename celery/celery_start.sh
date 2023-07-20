cd /root/app/ecom

# Activate the virtual environment (adjust the path if needed)
source /root/app/env/bin/activate

python -m celery -A labsoft  worker -l info
