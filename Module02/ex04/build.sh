~/miniconda3/bin/conda init bash 
conda create python=3.7 --use-local -y --name tmp_env
conda activate tmp_env
pip install --upgrade pip build
python setup.py sdist
python setup.py bdist_wheel
