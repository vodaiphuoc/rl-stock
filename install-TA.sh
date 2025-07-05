PREFIX=/kaggle/working
TA_LIBRARY_PATH=$PREFIX/lib
TA_INCLUDE_PATH=$PREFIX/include

wget -q https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib-0.6.4-src.tar.gz
tar zxf ta-lib-0.6.4-src.tar.gz
cd ta-lib-0.6.4 && ./configure --prefix=$PREFIX
cd ta-lib-0.6.4 && make  && sudo make install
export TA_LIBRARY_PATH=$TA_LIBRARY_PATH && \
export TA_INCLUDE_PATH=$TA_INCLUDE_PATH && \
pip install TA-Lib