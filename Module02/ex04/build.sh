~/miniconda3/bin/conda init bash 
conda create --name tmp_env python=3.7 -y
conda activate tmp_env
pip install --upgrade pip build
python setup.py bdist
# mv ./dist/my-minipack-1.0.0.linux-x86_64.tar.gz ./dist/my_minipack-1.0.0.tar.gz
python setup.py bdist_wheel
